

class CompPlayer:
	"""
	The Player class that is created to represent each player
	"""

	def __init__(self, playerID):
		#Resistance = 1, Spy = 0
		self.playerID = playerID
		self.alliance = 0
		self.PV = {}
		#PV = Person Values, a dictionary containing the players opions of all players

class Resistance(CompPlayer):
	"""
	The subclass for Resistance memebers
	"""
	def __init__(self, playerID):
		Player.__init__(self, playerID)

		
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
		team = playedRound.getFinalMissionTeam()
		teamCaptain = playedRound.finalTeamKey
		if self in team:
			winRate = playedRound.teamProb.getInSuccRate()
		else:
			winRate = playedRound.teamProb.getOutSuccRate()
		if all(roundResults):
			chanceOfAllRes = 
			for player in team:
				if player is not self:
					if player is teamCaptain:
						self.PV[player] = self.PV[player] * winRate * 
					else:
						self.PV[player] = self.PV[player] * winRate * 


	def pickTeam(self, numParti, round):
		sortedPV = sorted(self.PV.items(), key = lambda x: x[1], reverse = True)
		selectedPlayers = sortedPV[:numParti]
		rtn = []
		for player in selectedPlayers:
			rtn = rtn + [player[0]]
		return rtn

class Spy(CompPlayer):
	"""
	The subclass for Spy memebers
	"""
	def __init__(self, playerID):
		Player.__init__(self, playerID)
		self.alliance = 1
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