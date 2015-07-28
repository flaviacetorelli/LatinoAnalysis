#!/usr/bin/env python

import json
import sys
import ROOT
import optparse
#import hwwinfo
#import hwwsamples
#import hwwtools
import LatinoAnalysis.Gardener.hwwtools as hwwtools
import os.path
import string
import logging
import LatinoAnalysis.Gardener.odict as odict
#from HWWAnalysis.Misc.ROOTAndUtils import TH1AddDirSentry
import traceback
from array import array



# ----------------------------------------------------- ShapeFactory --------------------------------------

class ShapeFactory:
    _logger = logging.getLogger('ShapeFactory')
 
    # _____________________________________________________________________________
    def __init__(self):
        self._stdWgt = 'baseW*puW*effW*triggW'
        self._systByWeight = {}
      
        variables = {}
        self._variables = variables

        cuts = {}
        self._cuts = cuts

        samples = {}
        self._samples = samples

        outputFile = {}
        self._outputFile = outputFile




    # _____________________________________________________________________________
    def __del__(self):
        pass

    # _____________________________________________________________________________
    def getvariable(self,tag,mass,cat):

        if tag in self._variables :
            try:
                theVariable = (self._variables[tag])(mass,cat)
            except KeyError as ke:
                self._logger.error('Variable '+tag+' not available. Possible values: '+', '.join(self._variables.iterkeys()) )
                raise ke
        else :
            theVariable = tag

        return theVariable


    # _____________________________________________________________________________
    def makeNominals(self, inputDir, outputDir, variables, cuts, samples):

        print "======================"
        print "==== makeNominals ===="
        print "======================"
        
        self._variables = variables
        self._samples   = samples
        self._cuts      = cuts
        
        
        self._outputFileName = outputDir+'/plots_'+self._tag+".root"
        print " outputFileName = ", self._outputFileName
        self._outFile = ROOT.TFile.Open( self._outputFileName, 'recreate')
        
        ROOT.TH1.SetDefaultSumw2(True)
        
        selections = "1"

        #---- first create structure in ourput root file
        for cutName in self._cuts :
          print "cut = ", cutName, " :: ", cuts[cutName]
          self._outFile.mkdir (cutName)
          for variableName, variable in self._variables.iteritems():
            self._outFile.mkdir (cutName+"/"+variableName)
            print "variable[name]  = ", variable ['name']
            print "variable[range] = ", variable ['range']
            #for nuisance in self._nuisances :
              #print "nuisance = ", nuisance
              # open the root file

       
        #---- now plot and save into output root file
        for cutName, cut in self._cuts.iteritems():
          print "cut = ", cutName, " :: ", cut
          for variableName, variable in self._variables.iteritems():
            print "variable[name]  = ", variable['name']
            print "variable[range] = ", variable['range']
            self._outFile.cd (cutName+"/"+variableName)
            
            list_of_trees_to_connect = {}
            for sampleName, sample in self._samples.iteritems():
              list_of_trees_to_connect[sampleName] = sample['name']

            inputs = self._connectInputs( list_of_trees_to_connect, inputDir)
            
            for sampleName, sample in self._samples.iteritems():
              print "sample[name]    = ", sample ['name']
              print "sample[weight]  = ", sample ['weight']
              print "sample[weights] = ", sample ['weights']

              # create histogram: already the "hadd" of possible sub-contributions
              outputsHisto = self._draw( variable['name'], variable['range'], sample ['weight'], sample ['weights'], cut, sampleName, inputs[sampleName])

              outputsHisto.Write()
              
              
            # - then disconnect the files
            self._disconnectInputs(inputs)

            #for nuisance in self._nuisances :
              #print "nuisance = ", nuisance
              #for sample in self._samples :
                 #print "sample = ", sample
                 
                 # get the weight
                 # open the root file
                 # plot
                 #self._draw(doalias, rng, selections, output, inputs)
                 # save histogram

                 #print 'Output file:',self._outputFile



    
    # _____________________________________________________________________________
    def _draw(self, var, rng, global_weight, weights, cut, sampleName, inputs):       
        '''
        var           :   the variable to plot
        rng           :   the variable to plot
        global_weight :   the global weight for the samples
        weights       :   the wieghts 'root file' dependent
        cut           :   the selection
        inputs        :   the list of input files for this particular sample
        '''
        
        self._logger.info('Yields by process')
  
        numTree = 0
        hTotal = ROOT.TH1D
        bigName = 'histo_' + sampleName
        for tree in inputs:
          print '    {0:<20} : {1:^9}'.format(sampleName,tree.GetEntries()),
          # new histogram
          shapeName = 'histo_' + sampleName + str(numTree)

          # prepare a dummy to fill
          shape = self._makeshape(shapeName,rng)

          self._logger.debug('---'+sampleName+'---')
          self._logger.debug('Formula: '+var+'>>'+shapeName)
          self._logger.debug('Cut:     '+cut)
          self._logger.debug('ROOTFiles:'+'\n'.join([f.GetTitle() for f in tree.GetListOfFiles()]))

          globalCut = "(" + cut + ") * (" + global_weight + ")"  
          # if weights vector is not given, do not apply file dependent weights
          if len(weights) != 0 :
            # if weight is not given for a given root file, '-', do not apply file dependent weight for that root file
            if weights[numTree] != '-' :
              globalCut = "(" + globalCut + ") * (" +  weights[numTree] + ")" 
            
          entries = tree.Draw( var+'>>'+shapeName, globalCut, 'goff')
          #shape = (ROOT.TH1D*) gDirectory->Get(shapeName)
          print ' >> ',entries,':',shape.Integral()
          
          if (numTree == 0) :
            shape.SetTitle(bigName)
            hTotal = shape
          else :
            hTotal.Add(shape)

          numTree += 1

        return hTotal






    # _____________________________________________________________________________
    @staticmethod
    def _bins2hclass( bins ):
        '''
        Fixed bin width
        bins = (nx,xmin,xmax)
        bins = (nx,xmin,xmax, ny,ymin,ymax)
        Variable bin width
        bins = ([x0,...,xn])
        bins = ([x0,...,xn],[y0,...,ym])  
        '''

        from array import array
        if not bins:
            return name,0
        elif not ( isinstance(bins, tuple) or isinstance(bins,list)):
            raise RuntimeError('bin must be an ntuple or an arrays')

        l = len(bins)
        # 1D variable binning
        if l == 1 and isinstance(bins[0],list):
            ndim=1
            hclass = ROOT.TH1D
            xbins = bins[0]
            hargs = (len(xbins)-1, array('d',xbins))
        elif l == 2 and  isinstance(bins[0],list) and  isinstance(bins[1],list):
            ndim=2
            hclass = ROOT.TH2D
            xbins = bins[0]
            ybins = bins[1]
            hargs = (len(xbins)-1, array('d',xbins),
                    len(ybins)-1, array('d',ybins))
        elif l == 3:
            # nx,xmin,xmax
            ndim=1
            hclass = ROOT.TH1D
            hargs = bins
        elif l == 6:
            # nx,xmin,xmax,ny,ymin,ymax
            ndim=2
            hclass = ROOT.TH2D
            hargs = bins
        else:
            # only 1d or 2 d hist
            raise RuntimeError('What a mess!!! bin malformed!')
        
        return hclass,hargs,ndim

    @staticmethod
    def _bins2dim(bins):
        hclass,hargs,ndim = ShapeFactory._bins2hclass( bins )
        return ndim

    @staticmethod
    def _makeshape( name, bins ):
        hclass,hargs,ndim = ShapeFactory._bins2hclass( bins )
        return hclass(name, name, *hargs)
      
       
 
    # _____________________________________________________________________________
    def _connectInputs(self, samples, inputDir):
        inputs = {}
        treeName = 'latino'
        for process,filenames in samples.iteritems():
          tree = self._buildchain(treeName,[ (inputDir + '/' + f) for f in filenames])
          inputs[process] = tree
          # FIXME: add possibility to add Friend Trees for new variables   
         
        return inputs

    # _____________________________________________________________________________
    def _disconnectInputs(self,inputs):
        for n in inputs.keys():
          #friends = inputs[n].GetListOfFriends()
          #if friends.__nonzero__():
            #for fe in friends:
              #friend = fe.GetTree()
              #inputs[n].RemoveFriend(friend)
              #ROOT.SetOwnership(friend,True)
              #del friend
          # remove the entire list of trees
          del inputs[n]
    
    # _____________________________________________________________________________
    def _buildchain(self,treeName,files):
        listTrees = []
        for path in files:
            self._logger.debug('     '+str(os.path.exists(path))+' '+path)
            if not os.path.exists(path):
                raise RuntimeError('File '+path+' doesn\'t exists')
            tree = ROOT.TChain(treeName)
            tree.Add(path)
            listTrees.append(tree)
        return listTrees



if __name__ == '__main__':
    print '''
--------------------------------------------------------------------------------------------------
   ___|   |                               \  |         |                
 \___ \   __ \    _` |  __ \    _ \      |\/ |   _` |  |  /   _ \   __| 
       |  | | |  (   |  |   |   __/      |   |  (   |    <    __/  |    
 _____/  _| |_| \__,_|  .__/  \___|     _|  _| \__,_| _|\_\ \___| _|    
                       _|                                               
--------------------------------------------------------------------------------------------------
'''    
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('--tag'            , dest='tag'            , help='Tag used for the shape file name'           , default=None)
    parser.add_option('--sigset'         , dest='sigset'         , help='Signal samples [SM]'                        , default='SM')
    parser.add_option('--outputDir'      , dest='outputDir'      , help='output directory'                           , default='./')
    parser.add_option('--inputDir'       , dest='inputDir'       , help='input directory'                            , default='./data/')
          
    # read default pargin options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()


    print " configuration file = ", opt.pycfg
    print " lumi =               ", opt.lumi
    
    print " inputDir =           ", opt.inputDir
    print " outputDir =          ", opt.outputDir
 
    

    if not opt.debug:
        pass
    elif opt.debug == 2:
        print 'Logging level set to DEBUG (%d)' % opt.debug
        logging.basicConfig( level=logging.DEBUG )
    elif opt.debug == 1:
        print 'Logging level set to INFO (%d)' % opt.debug
        logging.basicConfig( level=logging.INFO )

      
    factory = ShapeFactory()
    factory._energy    = opt.energy
    factory._lumi      = opt.lumi
    factory._tag       = opt.tag
    
    
    variables = {}
    if os.path.exists(opt.variablesFile) :
      handle = open(opt.variablesFile,'r')
      exec(handle)
      handle.close()
    
    cuts = {}
    if os.path.exists(opt.cutsFile) :
      handle = open(opt.cutsFile,'r')
      exec(handle)
      handle.close()
    
    samples = {}
    if os.path.exists(opt.samplesFile) :
      handle = open(opt.samplesFile,'r')
      exec(handle)
      handle.close()
    
    
    factory.makeNominals( opt.inputDir ,opt.outputDir, variables, cuts, samples)
    
        
        
        
        
        
        
        
        

    #except Exception as e:
        #print '*'*80
        #print 'Fatal exception '+type(e).__name__+': '+str(e)
        #print '*'*80
        #exc_type, exc_value, exc_traceback = sys.exc_info()
        #traceback.print_tb(exc_traceback, file=sys.stdout)
##         traceback.print_tb(exc_traceback, limit=3, file=sys.stdout)
        #print '*'*80
    #finally:
        #print 'Used options'
        #print ', '.join([ '{0} = {1}'.format(a,b) for a,b in opt.__dict__.iteritems()])
