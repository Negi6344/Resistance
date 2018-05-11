


class Player:

	def __init__(self, playerID, alliance):
		self.ID = playerID
		self.alliance = alliance

	def castVote(self, failedAttempts):
		if (failedAttempts == 4):
			print('4 Failed Attempts: Autovote.\n')
			return 1
		return input('Cast Your Vote (0 or 1):\n')

	def pickTeam(self, numParty):
		return input('Select a team of ' + str(numParty) +'./n')

	def execMission(self):
		return input('Fail(0) or Success(1)\n')
		