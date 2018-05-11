import Player



class TestPlayerTT(Player):

	def __init__(self, playerID, alliance):
		Player.__init__(self, playerID, alliance)

	def castVote(self, failedAttempts):
		return True

	def execMission(self):
		return True

class TestPlayerFF(Player):

	def __init__(self, playerID, alliance):
		Player.__init__(self, playerID, alliance)

	def castVote(self, failedAttempts):
		return False

	def execMission(self):
		return False

class TestPlayerFT(Player):

	def __init__(self, playerID, alliance):
		Player.__init__(self, playerID, alliance)

	def castVote(self, failedAttempts):
		return False

	def execMission(self):
		return True

class TestPlayerTF(Player):

	def __init__(self, playerID, alliance):
		Player.__init__(self, playerID, alliance)

	def castVote(self, failedAttempts):
		return False

	def execMission(self):
		return False
