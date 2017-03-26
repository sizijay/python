def currentRuns(currentRunRate,remainingOvers):
	return (20-remainingOvers)*currentRunRate	

def projectedScore(currentRunRate,runRate,remainingOvers):
	return runRate*remainingOvers + currentRuns(currentRunRate,remainingOvers)
rr = int(raw_input("please enter the current run rate:"))
projectedrunRate = int(raw_input("Enter a runrate to calculate projected score rate:"))
overs = int(raw_input("Enter a number of overs to go:"))
print projectedScore(rr,projectedrunRate,overs)
