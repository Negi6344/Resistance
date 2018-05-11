class Player:

	def __init__(self, playerID, alliance):
		self.playerID = playerID
		self.alliance = alliance

	def castVote(self, failedAttempts):
		if (failedAttempts == 4):
			print("4 Failed Attempts: Autovote.\n")
			return 1
		return input("Cast Your Vote (0 or 1):\n")

	def pickTeam(self, numParti):
		team = input("Select a team of " + str(numParti) +"./n")

	def missionVote(self):
		print("Fail(0) or Success(1)\n")
		pass

class ComPlayer(Player):
	"""
	The Player class that is created to represent each player
	"""

	def __init__(self, playerID, alliance):
		Player.__init__(self, playerID, alliance)
		#Resistance = 1, Spy = 0
		self.PV = {}
		#PV = Person Values, a dictionary containing the players opions of all players

class Resistance(ComPlayer):
	"""
	The subclass for Resistance memebers
	"""
	def __init__(self, playerID):
		ComPlayer.__init__(self, playerID, 0)

		
	def castVote(self, team, failedAttempts):
		"""---TO DO---"""
		if (failedAttempts == 4):
			return 1
		teamScore = 0
		for player in team:
			teamScore = teamScore + self.PV[player]
		teamProb = int(teamScore/len(team))
		temp = random.randrange(100)
		# print(temp)
		# print(teamProb)
		if (temp >= teamProb):
			return 0
		else:
			return 1

	def createPV(self, playerList):
		for player in playerList:
			if (player.playerID == self.playerID):
				self.PV[player] = 100;
			else:
				self.PV[player] = 50;

	def updatePV(self, playedRound):
		pass
		# team = playedRound.getFinalMissionTeam()
		# teamCaptain = playedRound.finalTeamKey
		# if self in team:
		# 	winRate = playedRound.teamProb.getInSuccRate()
		# else:
		# 	winRate = playedRound.teamProb.getOutSuccRate()
		# if all(roundResults):
		# 	chanceOfAllRes = 
		# 	for player in team:
		# 		if player is not self:
		# 			if player is teamCaptain:
		# 				self.PV[player] = self.PV[player] * winRate * 
		# 			else:
		# 				self.PV[player] = self.PV[player] * winRate * 


	def pickTeam(self, numParti, round):
		sortedPV = sorted(self.PV.items(), key = lambda x: x[1], reverse = True)
		selectedPlayers = sortedPV[:numParti]
		rtn = []
		for player in selectedPlayers:
			rtn = rtn + [player[0]]
		return rtn

class Spy(ComPlayer):
	"""
	The subclass for Spy memebers
	"""
	def __init__(self, playerID):
		ComPlayer.__init__(self, playerID, 1)
		self.teammates = []
		
	def castVote(self, team):
		"""---TO DO---"""
		return True

	def createPV(self, playerList):
		for player in playerList:
			if (player.playerID == self.playerID):
				self.PV[player] = 100;
			else:
				self.PV[player] = 50;

	def updatePV(self, playerList, playersToBeUpdated):
		"""---TO DO---"""
		pass

	def pickTeam(self, numParti, round):
		"""---TO DO---"""
		# sortedPV = sorted(self.PV.items(), key = x: x[1], reverse = True)
		# selectedPlayers = sortedPV[:numParti]
		# rtn = []
		# for player in selectedPlayers:
			# rtn = rtn + [player[0]]
		# return rtn
		pass