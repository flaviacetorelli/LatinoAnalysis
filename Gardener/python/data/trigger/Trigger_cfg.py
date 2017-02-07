#Trigger = {}

# --------------------------- 2015 ---------------------------------

Trigger['Full2015'] =  { 1  :  { 'begin' : 1 , 'end' : 999999 , 'lumi' :  5.0 ,
                                 'LegEff' :  { 'DoubleEleLegHigPt' : 'HLT_Ele17_12LegHigPt.txt' ,
                                               'DoubleEleLegLowPt' : 'HLT_Ele17_12LegLowPt.txt' ,
                                               'SingleEle'         : 'HLT_Ele23Single.txt'      ,
                                               'DoubleMuLegHigPt'  : 'HLT_DoubleMuLegHigPt.txt' ,
                                               'DoubleMuLegLowPt'  : 'HLT_DoubleMuLegLowPt.txt' ,
                                               'SingleMu'          : 'HLT_MuSingle.txt' ,
                                               'MuEleLegHigPt'     : 'HLT_MuEleLegHigPt.txt' ,
                                               'MuEleLegLowPt'     : 'HLT_MuEleLegLowPt.txt' ,
                                               'EleMuLegHigPt'     : 'HLT_EleMuLegHigPt.txt' ,
                                               'EleMuLegLowPt'     : 'HLT_EleMuLegLowPt.txt' ,
                                             } ,
                                 'DZEff'  :  { 'DoubleEle' : 0.995 ,
                                               'DoubleMu'  : 0.95  ,
                                               'MuEle'     : 1.0   ,
                                               'EleMu'     : 1.0   ,
                                             } ,
                                 'EMTFBug':  False , 
                               },
                       },

# --------------------------- ICHEP2016 ---------------------------------

Trigger['ICHEP2016'] =  { 1  :  { 'begin' : 273158 , 'end' : 274094 , 'lumi' :  0.632 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegHigPt.txt' ,
                                                'DoubleEleLegLowPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegLowPt.txt' ,
                                                'SingleEle'         : 'ICHEP2016fullLumi/HLT_EleSingle.txt' ,
                                                'DoubleMuLegHigPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegHigPt_BeforeRun274094.txt' ,
                                                'DoubleMuLegLowPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegLowPt_BeforeRun274094.txt' ,
                                                'SingleMu'          : 'ICHEP2016fullLumi/HLT_MuSingle_BeforeRun274094.txt' ,
                                                'MuEleLegHigPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegHigPt_BeforeRun274094.txt' ,
                                                'MuEleLegLowPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegLowPt_BeforeRun274094.txt' ,
                                                'EleMuLegHigPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegHigPt_BeforeRun274094.txt' ,
                                                'EleMuLegLowPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegLowPt_BeforeRun274094.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : 0.995 ,
                                                'DoubleMu'  : 1.0   ,
                                                'MuEle'     : 1.0   ,
                                                'EleMu'     : 1.0   ,
                                              } ,
                                  'EMTFBug':  True , 
                                  'DATA'   :  {
                                                'EleMu'     : [  6 , 8  ] ,
                                                'DoubleMu'  : [ 11 , 13 ] ,
                                                'SingleMu'  : [ 42 , 43 ] ,
                                                'DoubleEle' : [ 46 ] ,
                                                'SingleEle' : [ 0  , 56 ] ,
                                              } ,
                                },
                          2  :  { 'begin' : 274094 , 'end' : 999999 , 'lumi' : 11.798  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegHigPt.txt' ,
                                                'DoubleEleLegLowPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegLowPt.txt' ,
                                                'SingleEle'         : 'ICHEP2016fullLumi/HLT_EleSingle.txt' ,
                                                'DoubleMuLegHigPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegHigPt.txt' ,
                                                'DoubleMuLegLowPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegLowPt.txt' ,
                                                'SingleMu'          : 'ICHEP2016fullLumi/HLT_MuSingle.txt' ,
                                                'MuEleLegHigPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegHigPt.txt' ,
                                                'MuEleLegLowPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegLowPt.txt' ,
                                                'EleMuLegHigPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegHigPt.txt' ,
                                                'EleMuLegLowPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegLowPt.txt' ,
                                              } ,
                                  'DZEff'  :  { 'DoubleEle' : 0.995 ,
                                                'DoubleMu'  : 1.0   ,
                                                'MuEle'     : 1.0   ,
                                                'EleMu'     : 1.0   ,
                                              } ,
                                  'EMTFBug':  True , 
                                  'DATA'   :  { 
                                                'EleMu'     : [  6 , 8  ] ,
                                                'DoubleMu'  : [ 11 , 13 ] ,
                                                'SingleMu'  : [ 42 , 43 ] ,
                                                'DoubleEle' : [ 46 ] ,
                                                'SingleEle' : [ 0  , 56 ] ,
                                              } ,
                                },
                        }
        
        


# --------------------------- Full2016 ---------------------------------

Trigger['Full2016'] =  { 1  :  { 'begin' : 273158 , 'end' : 274094 , 'lumi' :  0.632 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegHigPt.txt' ,
                                                'DoubleEleLegLowPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegLowPt.txt' ,
                                                'SingleEle'         : 'ICHEP2016fullLumi/HLT_EleSingle.txt' ,
                                                'DoubleMuLegHigPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegHigPt_BeforeRun274094.txt' ,
                                                'DoubleMuLegLowPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegLowPt_BeforeRun274094.txt' ,
                                                'SingleMu'          : 'ICHEP2016fullLumi/HLT_MuSingle_BeforeRun274094.txt' ,
                                                'MuEleLegHigPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegHigPt_BeforeRun274094.txt' ,
                                                'MuEleLegLowPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegLowPt_BeforeRun274094.txt' ,
                                                'EleMuLegHigPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegHigPt_BeforeRun274094.txt' ,
                                                'EleMuLegLowPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegLowPt_BeforeRun274094.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : 1.0   ,
                                                'DoubleMu'  : 1.0   ,
                                                'MuEle'     : 1.0   ,
                                                'EleMu'     : 1.0   ,
                                              } ,
                                  'EMTFBug':  True , 
                                  'DATA'   :  {
                                                'EleMu'     = [  6 , 8  ] ,
                                                'DoubleMu'  = [ 11 , 13 ] ,
                                                'SingleMu'  = [ 44 , 45 ] ,
                                                'DoubleEle' = [ 46 ] ,
                                                'SingleEle' = [ 93  , 112 ] ,
                                              } ,
                                },
                          2  :  { 'begin' : 274094 , 'end' : 277165 , 'lumi' : 15.3515  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegHigPt.txt' ,
                                                'DoubleEleLegLowPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegLowPt.txt' ,
                                                'SingleEle'         : 'ICHEP2016fullLumi/HLT_EleSingle.txt' ,
                                                'DoubleMuLegHigPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegHigPt.txt' ,
                                                'DoubleMuLegLowPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegLowPt.txt' ,
                                                'SingleMu'          : 'ICHEP2016fullLumi/HLT_MuSingle.txt' ,
                                                'MuEleLegHigPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegHigPt.txt' ,
                                                'MuEleLegLowPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegLowPt.txt' ,
                                                'EleMuLegHigPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegHigPt.txt' ,
                                                'EleMuLegLowPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegLowPt.txt' ,
                                              } ,
                                  'DZEff'  :  { 'DoubleEle' : 1.0   ,
                                                'DoubleMu'  : 1.0   ,
                                                'MuEle'     : 1.0   ,
                                                'EleMu'     : 1.0   ,
                                              } ,
                                  'EMTFBug':  True , 
                                  'DATA'   :  { 
                                                'EleMu'     : [  6 , 8  ] ,
                                                'DoubleMu'  : [ 11 , 13 ] ,
                                                'SingleMu'  = [ 44 , 45 ] ,
                                                'DoubleEle' = [ 46 ] ,
                                                'SingleEle' = [ 93  , 112 ] ,
                                              } ,
                                },
                          # https://twiki.cern.ch/twiki/bin/view/CMS/EndcapHighPtMuonEfficiencyProblem                                  
                          3  :  { 'begin' : 277166 , 'end' : 278272 , 'lumi' : 2.114  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegHigPt.txt' ,
                                                'DoubleEleLegLowPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegLowPt.txt' ,
                                                'SingleEle'         : 'ICHEP2016fullLumi/HLT_EleSingle.txt' ,
                                                'DoubleMuLegHigPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegHigPt.txt' ,
                                                'DoubleMuLegLowPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegLowPt.txt' ,
                                                'SingleMu'          : 'ICHEP2016fullLumi/HLT_MuSingle.txt' ,
                                                'MuEleLegHigPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegHigPt.txt' ,
                                                'MuEleLegLowPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegLowPt.txt' ,
                                                'EleMuLegHigPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegHigPt.txt' ,
                                                'EleMuLegLowPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegLowPt.txt' ,
                                              } ,
                                  'DZEff'  :  { 'DoubleEle' : 1.0   ,
                                                'DoubleMu'  : 1.0   ,
                                                'MuEle'     : 1.0   ,
                                                'EleMu'     : 1.0   ,
                                              } ,
                                  'EMTFBug':  False , 
                                  'DATA'   :  { 
                                                'EleMu'     : [  6 , 8  ] ,
                                                'DoubleMu'  : [ 11 , 13 ] ,
                                                'SingleMu'  = [ 44 , 45 ] ,
                                                'DoubleEle' = [ 46 ] ,
                                                'SingleEle' = [ 93  , 112 ] ,
                                              } ,
                                },
                          4  :  { 'begin' : 278273 , 'end' : 281612 , 'lumi' : 9.818  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegHigPt.txt' ,
                                                'DoubleEleLegLowPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegLowPt.txt' ,
                                                'SingleEle'         : 'ICHEP2016fullLumi/HLT_EleSingle.txt' ,
                                                'DoubleMuLegHigPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegHigPt.txt' ,
                                                'DoubleMuLegLowPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegLowPt.txt' ,
                                                'SingleMu'          : 'ICHEP2016fullLumi/HLT_MuSingle.txt' ,
                                                'MuEleLegHigPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegHigPt.txt' ,
                                                'MuEleLegLowPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegLowPt.txt' ,
                                                'EleMuLegHigPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegHigPt.txt' ,
                                                'EleMuLegLowPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegLowPt.txt' ,
                                              } ,
                                  'DZEff'  :  { 'DoubleEle' : 0.95  ,
                                                'DoubleMu'  : 1.0   ,
                                                'MuEle'     : 1.0   ,
                                                'EleMu'     : 1.0   ,
                                              } ,
                                  'EMTFBug':  False , 
                                  'DATA'   :  { 
                                                'EleMu'     : [ 57 , 97 ] ,
                                                'DoubleMu'  : [ 11 , 13 ] ,
                                                'SingleMu'  = [ 44 , 45 ] ,
                                                'DoubleEle' = [ 46 ] ,
                                                'SingleEle' = [ 93  , 112 ] ,
                                              } ,
                                },
                          5  :  { 'begin' : 281613 , 'end' : 284044 , 'lumi' : 8.857  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegHigPt.txt' ,
                                                'DoubleEleLegLowPt' : 'ICHEP2016fullLumi/HLT_DoubleEleLegLowPt.txt' ,
                                                'SingleEle'         : 'ICHEP2016fullLumi/HLT_EleSingle.txt' ,
                                                'DoubleMuLegHigPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegHigPt.txt' ,
                                                'DoubleMuLegLowPt'  : 'ICHEP2016fullLumi/HLT_DoubleMuLegLowPt.txt' ,
                                                'SingleMu'          : 'ICHEP2016fullLumi/HLT_MuSingle.txt' ,
                                                'MuEleLegHigPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegHigPt.txt' ,
                                                'MuEleLegLowPt'     : 'ICHEP2016fullLumi/HLT_MuEleLegLowPt.txt' ,
                                                'EleMuLegHigPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegHigPt.txt' ,
                                                'EleMuLegLowPt'     : 'ICHEP2016fullLumi/HLT_EleMuLegLowPt.txt' ,
                                              } ,
                                  'DZEff'  :  { 'DoubleEle' : 0.95  ,
                                                'DoubleMu'  : 0.95  ,
                                                'MuEle'     : 1.0   ,
                                                'EleMu'     : 1.0   ,
                                              } ,
                                  'EMTFBug':  False , 
                                  'DATA'   :  { 
                                                'EleMu'     : [ 57 , 97 ] ,
                                                'DoubleMu'  : [ 10 , 100] ,
                                                'SingleMu'  = [ 44 , 45 ] ,
                                                'DoubleEle' = [ 46 ] ,
                                                'SingleEle' = [ 93  , 112 ] ,
                                              } ,
                                }, 
                                  
                        }
