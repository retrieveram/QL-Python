# 短縮形リスト(abbreviation list)
import QuantLib as ql

# Calendar
calJP   =  ql.Japan()
calEU   =  ql.TARGET()
calUS   =  ql.UnitedStates(ql.UnitedStates.FederalReserve)
calUSb  =  ql.UnitedStates(ql.UnitedStates.GovernmentBond)
calUSs  =  ql.UnitedStates(ql.UnitedStates.SOFR)
# DayCounter
dcA365  =  ql.Actual365Fixed()
dcA360  =  ql.Actual360()
dc30    =  ql.Thirty360(ql.Thirty360.BondBasis)
dcAA    =  ql.ActualActual(ql.ActualActual.ISDA)
# T+ days (settle days)
Tp0     =  0
Tp2     =  2
# payment freqency
freqA   =  ql.Annual
freqSA  =  ql.Semiannual
freqD   =  ql.Daily
# 
pdFreqA =  ql.Period(ql.Annual)
pdFreqSA=  ql.Period(ql.Semiannual)
pdFreqD =  ql.Period(ql.Daily)
# schedule
mFLLW   =  ql.ModifiedFollowing
FLLW    =  ql.Following
unADJ   =  ql.Unadjusted
#
dgRULEb =  ql.DateGeneration.Backward
dgRULEf =  ql.DateGeneration.Forward
#
EoMf    =  False
EoMt    =  True
# compound
cmpdCMP =  ql.Compounded
cmpdCNT =  ql.Continuous
cmpdSPL =  ql.Simple
# currency
jpyFX   =  ql.JPYCurrency()