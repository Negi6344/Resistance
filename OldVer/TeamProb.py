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

	def __init__(self, players, roundNum):
		numRes = numOfGood[players]
		numOfBad = numOfBad[players]
		teamSize = missionPlayers[players][roundNum-1]
		if (players >= 7) and (roundNum == 4):
			failsNeeded = 2
		else: 
			failsNeeded = 1		

		playerList = []
		for i in range(players):
			playerList = playerList + [i]

		badList = [1,3,6,9]

		possTeam = list(IT.combinations(playerList,teamSize))	

		teamsIn = 0
		for team in possTeam:
			if 0 in team:
				teamsIn = teamsIn + 1		

		

		teamsInFail = 0
		teamsFail = 0
		for team in possTeam:
			bad = 0
			for i in badList:
				if i in team:
					bad = bad + 1
			if bad >= failsNeeded:
				teamsFail = teamsFail + 1
				if 0 in team:
					teamsInFail = teamsInFail + 1


		