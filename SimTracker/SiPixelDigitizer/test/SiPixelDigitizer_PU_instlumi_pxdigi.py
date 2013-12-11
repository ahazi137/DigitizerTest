import FWCore.ParameterSet.Config as cms

process = cms.Process("Demon")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(1)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100))

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

#Ezeket raktam bele en:
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
#process.load('Configuration.StandardSequences.Reconstruction_cff')

#------>>>>> process.load("Configuration.StandardSequences.Services_cff")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.load("IOMC.RandomEngine.IOMC_cff") ## from Services

####process.load("Validation.TrackerHits.trackerHitsValidation_cff")
process.load("SimTracker.Configuration.SimTracker_cff") ## for Strips
####process.load("Validation.TrackerDigis.trackerDigisValidation_cff")
process.load("SimG4Core.Configuration.SimG4Core_cff")
process.load("SimGeneral.MixingModule.mixNoPU_cfi")
#process.load('SimGeneral.MixingModule.mix_2012_201278_1_cfi')
process.mix.bunchspace = 50
##process.load('SimGeneral.MixingModule.mix_2012_198230_2_cfi')

#----->>> process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("RecoTracker.Configuration.RecoTracker_cff")
process.load("TrackingTools.Configuration.TrackingTools_cff")
process.load("RecoVertex.Configuration.RecoVertex_cff")
process.load("RecoPixelVertexing.Configuration.RecoPixelVertexing_cff")
process.load("RecoLocalTracker.Configuration.RecoLocalTracker_cff")
process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")

####process.load("Validation.TrackerRecHits.trackerRecHitsValidation_cff")
####process.load("SimGeneral.TrackingAnalysis.trackingParticles_cfi")
####process.load("Validation.TrackingMCTruth.trackingTruthValidation_cfi")
####process.load("Validation.RecoTrack.TrackValidation_cff")
####process.load("Validation.RecoTrack.SiTrackingRecHitsValid_cff")

process.load("EventFilter.SiPixelRawToDigi.SiPixelDigiToRaw_cfi")
process.load("EventFilter.SiPixelRawToDigi.SiPixelRawToDigi_cfi") # already in  Conf.StdSeq.RawToDigi below
#----->>> process.load('Configuration.StandardSequences.RawToDigi_cff')
process.siPixelDigis.InputLabel = cms.InputTag("siPixelRawData")

process.load("EventFilter.SiStripRawToDigi.SiStripDigis_cfi")

process.load('Configuration.StandardSequences.L1Reco_cff')
####process.load('Configuration.StandardSequences.Reconstruction_cff') second call
####process.load('Configuration.StandardSequences.Validation_cff')
####process.load('DQMOffline.Configuration.DQMOfflineMC_cff')
####process.load('Configuration.StandardSequences.EndOfProcess_cff')

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
#   'file:/tmp/taroni/STEP2_myRECOSIMEC_1_1_r2n.root'
#    'file:/tmp/taroni/REDIGI_7_2_w2y.root'
    'file:/data/bmarton/Data/MC/198230/REDIGI_9_8_TbQ.root' #Silvia Redigi
#'file:/data/bmarton/Data/NewMC/data/006D547C-3E5F-E111-A78C-002590207E3C.root' #GEN-SIM

)

                            )
import FWCore.PythonUtilities.LumiList as LumiList

#### process.load("RecoTracker.Configuration.RecoTracker_cff")  already in Conf.StdSeq.Reco
process.load("RecoTracker/TrackProducer/TrackRefitters_cff")
process.load("RecoTracker.TransientTrackingRecHit.TransientTrackingRecHitBuilderWithoutRefit_cfi")
process.TrackRefitter.src = "generalTracks"
process.TrackRefitter.TrajectoryInEvent = True
#### process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff') second call
#### process.load('Configuration.StandardSequences.GeometryRecoDB_cff') second call
#### process.load('Configuration.StandardSequences.MagneticField_38T_cff') second call
process.GlobalTag.globaltag = 'START53_V7E::All'

## process.TimingStudy = cms.EDAnalyzer('TimingStudy',
##                               trajectoryInput = cms.string('TrackRefitter'),
##                               fileName = cms.string("test3.root"),
##                               isMC = cms.untracked.bool(True),
##                               TkTag = cms.untracked.string("TrackRefitter")
## )


process.TimingStudy = cms.EDAnalyzer("TimingStudy",
                                     trajectoryInput = cms.string('TrackRefitter'),
                                     fileName = cms.string("SiPixelDigitizer_pxdigitest100roc.root"),
                                     extrapolateFrom = cms.int32(2),
                                     extrapolateTo = cms.int32(1),
                                     keepOriginalMissingHit = cms.bool(False),
                                     usePixelCPE= cms.bool(True),
                                     #minNStripHits = cms.int32(0),
                                     triggerNames=cms.vstring("HLT_ZeroBias",
                                                              "HLT_Physics",
                                                              "HLT_Random",
                                                              "HLT_PixelTracks_Multiplicity100",
                                                              "HLT_PixelTracks_Multiplicity80",
                                                              "HLT_PixelTracks_Multiplicity125",
                                                              "HLT_PixelTracks_Multiplicity110",
                                                              "HLT_PixelTracks_Multiplicity85",
                                                              "HLT_PixelTracks_Multiplicity70",
                                                              "HLT_PixelTracks_Multiplicity40",
                                                              "HLT_L1Tech_BSC_HighMultiplicity",
                                                              "HLT_JetE30_NoBPTX",
                                                              "HLT_JetE30_NoBPTX_NoHalo",
                                                              "HLT_JetE30_NoBPTX3BX_NoHalo",
                                                              "HLT_JetE50_NoBPTX3BX_NoHalo",
                                                              "HLT_60Jet10",
                                                              "HLT_70Jet10",
                                                              "HLT_70Jet13",
                                                              "HLT_L1Tech_BSC_minBias",
                                                              "HLT_MinBias"),#Any MinBias triggers starting like this
                                     mcLumiScale = cms.double(221.95)
)


from SimTracker.SiPixelDigitizer.PixelDigi_cfi import *
#process.simSiPixelDigis.ThresholdInElectrons_FPix = 3000.0
#process.simSiPixelDigis.ThresholdInElectrons_BPix = 3000.0

process.simSiPixelDigis.AddPixelInefficiency = -100
process.simSiPixelDigis.thePixelColEfficiency_BPix1 = cms.double(0.999)
process.simSiPixelDigis.thePixelColEfficiency_BPix2 = cms.double(1.0)
process.simSiPixelDigis.thePixelColEfficiency_BPix3 = cms.double(1.0)

process.simSiPixelDigis.thePixelEfficiency_BPix1 = cms.double(1.0)
process.simSiPixelDigis.thePixelEfficiency_BPix2 = cms.double(1.0)
process.simSiPixelDigis.thePixelEfficiency_BPix3 = cms.double(1.0)

process.simSiPixelDigis.theBPix1LadderEfficiency = cms.vdouble(
    0.97963,
    0.971863,
    0.975178,
    0.968154,
    0.972828,
    0.973056,
    0.976997,
    0.975153,
    0.981202,
    0.979234,
    0.984533,
    0.981061,
    0.985368,
    0.983221,
    0.983094,
    0.984578,
    0.98389,
    0.981607,
    0.981074,
    0.976099
)

process.simSiPixelDigis.theBPix1ModuleEfficiency = cms.vdouble(
    1.00323,
    1.00074,
    0.977744,
    0.783408
)

process.simSiPixelDigis.theBPix1PUEfficiency = cms.vdouble(
    1.01997,
    -4.03709e-07,
    -1.26739e-09
)


process.simSiPixelDigis.DeadModules = cms.VPSet(cms.PSet(Dead_detID = cms.int32(302059800), Module = cms.string("whole"))
                                                ,cms.PSet(Dead_detID = cms.int32(302059032), Module = cms.string("whole"))
                                                ,cms.PSet(Dead_detID = cms.int32(302059036), Module = cms.string("tbmA"))
                                               # ,cms.PSet(Dead_detID = cms.int32(302059040), Module = cms.string("whole"))
                                               #,cms.PSet(Dead_detID = cms.int32(302059040),  Module = cms.string("none"), Dead_RocID = cms.int32(6)) #lay1_lad-9_mod4
                                               # ,cms.PSet(Dead_detID = cms.int32(302057744), Module = cms.string("tbmB"), Dead_RocID = cms.int32(3))
                                                )

#BPix_BpO_SEC8_LYR1_LDR9_MOD2 
#process.simSiPixelDigis.DeadModules = cms.PSet(
#    Module = cms.string("whole"),
#    Dead_detID = cms.int32(302059032)
#    )

#process.simSiPixelDigis = cms.PSet(
#    errortype = cms.string('tbmA'),
#    detid = cms.uint32(302059032)
#    )

#process.simSiPixelDigis = cms.PSet(
#    errortype = cms.string('none'),
#    detid = cms.uint32(302059032),
#    badroclist = cms.vuint32(7)
#    )

#Path-ok amit en raktam bele
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
#process.reconstruction_step = cms.Path(process.reconstruction)
#az eredeti Path-ok 5 #-el vannak jelolve
#process.p1 = cms.Path(process.mix*process.simSiPixelDigis)
#####process.digis = cms.Path(process.randomEngineStateProducer*process.mix*process.simSiPixelDigis)
####process.digis = cms.Path(process.mix*process.simSiPixelDigis*process.pixelDigisValid)
## process.rechits = cms.Sequence(process.pixeltrackerlocalreco*process.siStripMatchedRecHits*process.pixRecHitsValid)
## process.tracks = cms.Sequence(process.offlineBeamSpot*process.recopixelvertexing*process.trackingParticles*process.trackingTruthValid*process.ckftracks*process.trackerRecHitsValidation)
## process.trackinghits = cms.Sequence(process.offlineBeamSpot*process.TrackRefitter*process.trackingRecHitsValid)
## #process.p1 = cms.Path(process.mix*process.simSiPixelDigis)
process.p = cms.Path(
    process.TrackRefitter*process.TimingStudy
)

## process.TFileService = cms.Service("TFileService",
##      fileName = cms.string('simpleAnalysis_rerecoMC.root')
## )



# Other statements
#####process.mix.playback = True
process.RandomNumberGeneratorService.restoreStateLabel=cms.untracked.string("randomEngineStateProducer")
#process.GlobalTag.globaltag = 'START53_V7E::All'
#process.GlobalTag.globaltag = 'START53_V7A::All'

# Path and EndPath definitions
#----->>>> process.raw2digi_step = cms.Path(process.siPixelRawData*process.RawToDigi)
#####process.raw2digi_step = cms.Path(process.siPixelRawData*process.siPixelDigis*process.siStripDigis)
#####process.L1Reco_step = cms.Path(process.L1Reco)
#----->>>>> process.reconstruction_step = cms.Path(process.reconstruction)
process.reconstruction_step = cms.Path(process.trackerlocalreco*process.offlineBeamSpot*process.recopixelvertexing*process.ckftracks*process.vertexreco)
#process.endjob_step = cms.EndPath(process.endOfProcess)
##process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

#process.out = cms.OutputModule( "PoolOutputModule",
#outputCommands = cms.untracked.vstring(
#'keep *', 
#'keep *_laserAlignmentT0Producer_*_*'
#),
#fileName = cms.untracked.string( 'ReRecomix.root' )
#)
#process.outpath = cms.EndPath(process.out)

# Schedule definition
#process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.RECOSIMoutput_step)
###process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.p,process.outpath) 

#process.schedule = cms.Schedule(process.digis,process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.p,process.outpath) 
#####process.schedule = cms.Schedule(process.digis,process.rawdigi_step,process.L1Reco_step,process.reconstruction_step,process.p) 
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step,process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.p)




















