import random
import Player as plr

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

# After 7 players, mission 4 needs at least 2 fails

class GameState:
	"""
	The game class that creates the players, when initiated, and holds the game state
	"""

	def __init__(self, numPlayers=5, comPlayers=0):
		if (numPlayers < 5 or numPlayers > 10):
			raise ValueError("This game is for 5 to 10 players")
		self.numPlayers = numPlayers
		self.currentLeader = 0
		self.round = 1
		self.roundList = []
		#create numPlayers
		self.playerList = []

		#Resistance = 1, Spy = 0
		allianceList = []
		for i in range(numOfGood[self.numPlayers]):
			allianceList = allianceList + [1]
		for i in range(numOfBad[self.numPlayers]):
			allianceList = allianceList + [0]
		random.shuffle(allianceList)
		print(allianceList)


		"""
		manas was here
		"""
		
		# for i in range(self.players):
		# 	print(i)
		# 	if (allianceList[i]):
		# 		newRes = Resistance(i)
		# 		self.playerList = self.playerList + [newRes]
		# 	else:
		# 		newSpy = Spy(i)
		# 		self.playerList = self.playerList + [newSpy]
		# for player in self.playerList:
		# 	player.createPV(self.playerList)

		IDNumber = 0;
		for role in allianceList:
			if IDNumber < numPlayers - comPlayers:
				self.playerList = self.playerList + [plr.player(role,IDNumber)]
			else:
				self.playerList = self.playerList + [plr.makeCom(role,IDNumber)]
			IDNumber = IDNumber + 1

		self.roundList = self.roundList + Round(0, numPlayers)


	def getNumberOfRes(self):
		return numOfGood[self.numPlayers]

	def getNumberOfSpys(self):
		return numOfBad[self.numPlayers]

	def getMissionPlayers(self,round):
		return missionPlayers[self.numPlayers][round - 1]

	def createRound(self, roundID):
		self.roundList = self.roundList + Round(roundID, self.numPlayers)

	def playRound(self):
		gameRound = Round(self.round, self.numPlayers)
		pass

	def isOver(self):
		if len(self.roundList) >= 3:
			count = 0
			for rnd in roundList:
				if not rnd.getResult():
					count = count + 1
			if count > 2:
				return True
		else:
			return False

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
		self.numPlayers = numPlayers
		self.teamProb = ProbRes.TeamProb(roundID, numPlayers)

	def getMissionTeam(self, leaderID):
		return self.teamSelectionDict[leaderID]

	def getFinalMissionTeam(self):
		return self.teamSelectionDict[self.finalTeamKey]
		
	def getTeamVote(self, leaderID):
		return self.teamVoteDict[leaderID]

	def makeVote(self, players, leader, team):
		self.finalTeamKey = leader
		self.teamSelectionDict[leader] = team

		for player in players:
			self.teamVoteDict[player.personID] = player.castVote(team)

		return all(self.teamVoteDict.values)

	def execMission(self, numFails):
		self.missionResults = []
		for player in self.teamSelectionDict[self.finalTeamKey]:
			self.missionResults = self.missionResults + player.execMission(numFails, self.teamSelectionDict[self.finalTeamKey])

	def getNumFails(self):
		count = 0
		for result in self.missionResults:
			if result == False:
				count = count + 1
		return count

	def getResult(self):
		if self.roundID == 4 and self.numPlayers >= 7:
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


