import TeamProbRes as ProbRes

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

class Round:
	"""
	The Round class that stores the information of each round
	"""
	
	def __init__(self, roundID, numPlayers):
		self.roundID = roundID
		self.teamSelectionDict = {}
		self.teamVoteDict = {}
		self.finalTeamKey = None
		self.missionResults = []
		self.teamProb = ProbRes.TeamProb(roundID, numPlayers)

	def getMissionTeam(self, playerID):
		return self.teamSelectionDict[playerID]

	def getFinalMissionTeam(self):
		return self.teamSelectionDict[self.finalTeamKey]
		
	def getTeamVote(self, playerID):
		return self.teamVoteDict[playerID]

	def makeVote(self, players, leader, team):
		self.finalTeamKey = leader
		self.teamSelectionDict[leader] = team
		missionStart = False

		for player in players:
			self.teamVoteDict[player.personID] = player.castVote(team)

		return all(self.teamVoteDict.values)

	def getNumFails(self):
		count = 0
		for result in self.missionResults:
			count = count + 1
		return count

	def getResult(self, numPlayers):
		if roundID == 4 and numPlayers >= 7:
			# failCount = 0
			# for result in self.missionResults:
			# 	if not result:
			# 		failCount = failCount + 1
			if self.getNumFails() >= 2:
				return False
		else:
			if not all(self.missionResults):
				return False
			else:
				return True

