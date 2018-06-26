import random

# Alliance ID's

# Resistance Memebers (Positive)
ResID = 1

# Spy Members (Negative)
SpyID = -1


class Player:

	def __init__(self, playerID, alliance, name = None):
		self.ID = playerID
		self.alliance = alliance
		if name is None:
			self.name = 'Player ' + str(playerID) + "   " + str(alliance)
		else:
			self.name = name

	def __str__(self):
		return self.name

	def getID(self):
		return self.ID

	def getAlliance(self):
		return self.alliance

	def castVote(self, failedAttempts, teamList):
		if (failedAttempts == 4):
			print('4 Failed Attempts: Autovote.\n')
			return 1
		return input(self.name + ': Cast Your Vote (0 or 1):\n')

	def pickTeam(self, numTeam, playerList):
		# Input is a list of IDNumbers that will be converted
		# to a list of Players that will be returned
		selectedPlayerIDs = input(self.name + ': Select a team of ' + str(numTeam) +'.\n') 
		
		selectedPlayers = []
		for ID in selectedPlayerIDs:
			selectedPlayers = selectedPlayers + [playerList[ID]]

		return selectedPlayers


	def execMission(self, teamList):
		return input(self.name + ': Fail(0) or Success(1)\n')



class ComPlayer(Player):

	def __init__(self, playerID, alliance, name = None):
		Player.__init__(self, playerID, alliance, name = None)
	# 	self.PV = {}

	# def initPV(self, playerList):
	# 	for player in playerList:
	# 		if player == self:
	# 			self.PV[self] = 100
	# 		else:
	# 			self.PV[player] = 50

	def castVote(self, failedAttempts, teamList):
		if (failedAttempts == 4):
			return 1
		return 1

	def pickTeam(self, numTeam, playerList):
		# TODO
		return random.sample(playerList, numTeam)

	def execMission(self, teamList):
		return 1



class ComRes(ComPlayer):

	def __init__(self, playerID, alliance=1, name = None):
		ComPlayer.__init__(self, playerID, 1, name = None)


class ComSpy(ComPlayer):

	def __init__(self, playerID, alliance=-1, name = None):
		ComPlayer.__init__(self, playerID, -1, name = None)

	def castVote(self, failedAttempts, teamList):
		if (failedAttempts == 4):
			return 1
		return 1

	def pickTeam(self, numTeam, playerList):
		# TODO
		return random.sample(playerList, numTeam)

	def execMission(self, teamList):
		return 0

	def howManyAllies(self, teamList):
		count = 0
		for player in teamList:
			if player.getAlliance() < 0:
				count = count + 1
		return count

def createComPlayer(playerID, alliance, name = None):
	if (playerID == -1):
		return ComSpy(playerID, alliance, name)
	else:
		return ComPlayer(playerID, alliance, name)

def isCom(player):
	return isinstance(player, ComPlayer)

# A = ComPlayer(0,1)
# B = ComPlayer(1,1)

# A.initPV([A,B])
# print(A.PV)
# print(list(reversed(sorted(A.PV, key=A.PV.get))))