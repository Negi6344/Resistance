import random
import Player as plr
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

# If 7+ players, mission 4 needs at least 2 fails

class GameState:

	def __init__(self, numPlayers = 5, comPlayers = 0):
		if (numPlayers < 5 or numPlayers > 10):
			raise ValueError('This game requires 5 to 10 players')
		self.numPlayers = numPlayers
		self.leaderPointer = 0
		self.round = 0
		self.roundList = []

		#create players
		self.playerList = []

		#Resistance members = 1
		#Spy memebers = 0
		self.allianceList = []
		for i in range(numOfGood[self.numPlayers]):
			self.allianceList = self.allianceList + [1]
		for i in range(numOfBad[self.numPlayers]):
			self.allianceList = self.allianceList + [0]
		random.shuffle(self.allianceList)

		IDNumber = 0;
		for role in self.allianceList:
			if IDNumber < numPlayers - comPlayers:
				self.playerList = self.playerList + [plr.Player(role,IDNumber)]
			# else:
			# 	self.playerList = self.playerList + [plr.makeCom(role,IDNumber)]
			IDNumber = IDNumber + 1

		self.roundList = [Round(0,numPlayers)]

	def getNumRes(self):
		return numOfGood[self.numPlayers]

	def getNumSpy(self):
		return numOfBad[self.numPlayers]

	def getMissionPlayers(self, roundNum):
		return missionPlayers[self.numPlayers][roundNum]

	def nextRound(self):
		if self. round <= 3:
			self.round = self.round + 1
			self.roundList = self.roundList + [Round(self.round, self.numPlayers)]

	def playRound(self):
		self.roundList[self.round].play()

	def isOver(self):
		if self.round == 4 and self.roundList[4] != []:
			return True
		if len(self.roundList) >= 3:
			succCount = 0
			failCount = 0
			for rnd in self.roundList:
				if rnd.getResult():
					succCount = succCount + 1
				else:
					failCount = failCount + 1
			if succCount > 2 or failCount > 2:
				return True
			else:
				return False
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
		self.finalTeamLeader = None
		self.missionResults = []
		self.numPlayers = numPlayers
		self.numAttepts = 0

	def getMissionTeam(self, leader):
		return self.teamSelectionDict[leader]

	def getFinalMissionTeam(self):
		return self.teamSelectionDict[self.finalTeamLeader]
		
	def getTeamVote(self, leader):
		return self.teamVoteDict[leader]

	def selectTeam(self, leader, numParty):
		self.finalTeamLeader = leader
		self.teamSelectionDict[leader] = leader.pickTeam(numParty)
		
	def execMission(self, numFailAttempts):
		self.missionResults = []
		for player in self.teamSelectionDict[self.finalTeamLeader]:
			self.missionResults = self.missionResults + player.execMission()

	def getNumFails(self):
		count = 0
		for result in self.missionResults:
			if result == False:
				count = count + 1
		return count

	def getResult(self):
		if self.roundID == 3 and self.numPlayers >= 7:
			if self.getNumFails() >= 2:
				return False
		else:
			if not all(self.missionResults):
				return False
		return True