import itertools as IT

numOfGood = {
	5:3,
	6:4,
	7:4,
	8:5,
	9:7,
	10:6,
}

numOfBad = {
	5:2,
	6:2,
	7:3,
	8:3,
	9:3,
	10:4,
}

missionPlayers = {
	5:[2,3,2,3,3],
	6:[2,3,4,3,4],
	7:[2,3,3,4,4],
	8:[3,4,4,5,5],
	9:[3,4,4,5,5],
	10:[3,4,4,5,5],
}

class TeamProb:

	def __init__(self, roundNum, numPlayers):
		numRes = numOfGood[numPlayers]
		teamSize = missionPlayers[numPlayers][roundNum-1]
		if (numPlayers >= 7) and (roundNum == 4):
			failsNeeded = 2
		else: 
			failsNeeded = 1		

		playerList = []
		for i in range(numPlayers):
			playerList = playerList + [i]

		badList = [1,3,6,9]

		possTeam = list(IT.combinations(playerList,teamSize))	

		teamsIn = 0
		for team in possTeam:
			if 0 in team:
				teamsIn = teamsIn + 1		

		

		teamsInFail = 0
		teamsFail = 0
		teamsWO = 0
		teamsWOSucc = 0
		for team in possTeam:
			bad = 0
			if 0 not in team:
				teamsWO = teamsWO + 1
			for i in badList:
				if i in team:
					bad = bad + 1
			if bad >= failsNeeded:
				teamsFail = teamsFail + 1
				if 0 in team:
					teamsInFail = teamsInFail + 1
			elif 0 not in team and bad < failsNeeded:
				teamsWOSucc = teamsWOSucc + 1

		self.numPossTeams = len(possTeam)
		self.numTeamsSucc = len(possTeam) - teamsFail
		self.numTeamsIn = teamsIn
		self.numTeamsInWin = teamsIn - teamsInFail
		self.numTeamsOut = teamsWO
		self.numTeamsWOSucc = teamsWOSucc


	def getSuccRate(self):
		return (float(self.numTeamsSucc)/self.numPossTeams)

	def getInSuccRate(self):
		return float(self.numTeamsInWin)/self.numTeamsIn

	def getOutSuccRate(self):
		return float(self.numTeamsInWin)/self.numTeamsIn
		