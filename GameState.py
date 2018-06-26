import random
import Player as plr
import itertools as IT


# Game Parameters Based on the rules of the game

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
		self.leaderPointer = random.choice(range(numPlayers))
		self.round = 0
		self.roundList = []

		#create players
		self.playerList = []

		#Assign Roles
		#Resistance members = 1
		#Spy memebers = -1
		self.allianceList = []
		for i in range(numOfGood[self.numPlayers]):
			self.allianceList = self.allianceList + [plr.ResID]
		for i in range(numOfBad[self.numPlayers]):
			self.allianceList = self.allianceList + [plr.SpyID]
		random.shuffle(self.allianceList)

		IDNumber = 0;
		for role in self.allianceList:
			if IDNumber < numPlayers - comPlayers:
				self.playerList = self.playerList + [plr.Player(IDNumber, role)]
			else:
				self.playerList = self.playerList + [plr.createComPlayer(IDNumber, role)]
			IDNumber = IDNumber + 1

		self.roundList = [Round(0,numPlayers)]
		print(self.playerList)

	def getNumRes(self):
		return numOfGood[self.numPlayers]

	def getNumSpy(self):
		return numOfBad[self.numPlayers]

	def getNumMissionPlayers(self, roundNum):
		return missionPlayers[self.numPlayers][roundNum]

	def nextLeader(self):
		self.leaderPointer = self.leaderPointer + 1
		if self.leaderPointer >= self.numPlayers:
			self.leaderPointer = 0

	def getMissionPlayers(self, roundNum):
		return missionPlayers[self.numPlayers][roundNum]

	def getCurrentRound(self):
		return self.roundList[self.round]

	def getCurrentLeader(self):
		return self.playerList[self.leaderPointer]

	def printPlayers(self, playerList):
		print('\n')
		for player in playerList:
			print(str(player) + '\n')

	def nextRound(self):
		self.round = self.round + 1
		self.roundList = self.roundList + [Round(self.round, self.numPlayers)]

	def playRound(self):
		currRound = self.roundList[self.round]

		missionStatus = False
		while (missionStatus == False and currRound.numAttempts < 5):
		# Select Leader and Select Team (Print Player List)
			currLeader = self.playerList[self.leaderPointer]

			# if isinstance(currLeader, plr.ComPlayer):
			if True:
				print('\n')
				for player in self.playerList:
					print(str(player) + '\n')
				print('\n')

			currTeam = currRound.selectTeam(currLeader, self.getNumMissionPlayers(self.round), self.playerList)

		# Each player votes on the Team

			self.printPlayers(currTeam)
			for player in self.playerList:
				currRound.addTeamVote(currLeader, player, player.castVote(currRound.numAttempts, currTeam))

		# Check Vote

			if currRound.checkVote(currLeader):
				missionStatus = True
			else:
				currRound.numAttepts = currRound.numAttempts + 1
			self.nextLeader()

		# Excecute Mission

		currRound.execMission()

	def isOver(self):
		if (self.round == 4 and self.roundList[4] != []):
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

	def printRoundResults(self):
		results = []
		for rnd in self.roundList:
			results = results + [rnd.getResult()]
		print(results)

	def printWinner(self):
		results = []
		count = 0
		for rnd in self.roundList:
			if rnd.getResult():
				count = count + 1
		if (count >= 3):
			print("The Resistance Wins!")
		print("The Spies Win!")
		


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
		self.numAttempts = 0

	def getMissionTeam(self, leader):
		return self.teamSelectionDict[leader]

	def getFinalMissionTeam(self):
		return self.teamSelectionDict[self.finalTeamLeader]

	def getTeamVote(self, leader):
		return self.teamVoteDict[leader]

	def addTeamVote(self, Leader, Voter, Vote):
		if Leader not in self.teamVoteDict.keys():
			self.teamVoteDict[Leader] = {}
		self.teamVoteDict[Leader][Voter] = Vote

	def checkVote(self, Leader):
		count = 0
		for vote in self.teamVoteDict[Leader].values():
			if vote:
				count = count + 1
			else:
				count = count -1
		if count > 0:
			return True
		return False

	def selectTeam(self, leader, numTeam, playerList):
		self.finalTeamLeader = leader
		self.teamSelectionDict[leader] = leader.pickTeam(numTeam, playerList)
		return self.teamSelectionDict[leader]
		
	def execMission(self):
		self.missionResults = []
		for player in self.teamSelectionDict[self.finalTeamLeader]:
			self.missionResults = self.missionResults + [player.execMission(self.teamSelectionDict[self.finalTeamLeader])]

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