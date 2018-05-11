import unittest
import GameState as gs
import Player as plr

gs5 = gs.GameState(5)
gs7 = gs.GameState(7)

class GameStateCase(unittest.TestCase):
	
	def test_few_players(self):
		self.assertRaises(ValueError, gs.GameState, 4)

	def test_many_players(self):
		self.assertRaises(ValueError, gs.GameState, 11)

	def test_alliance_creation(self):
		self.assertItemsEqual(gs5.allianceList, [0 , 0, 1, 1, 1])

	def test_alliance_creation1(self):
		self.assertItemsEqual(gs7.allianceList, [0 , 0, 0, 1, 1, 1, 1])	

	def test_player_creation(self):
		for player in gs5.playerList:
			self.assertIsInstance(player, plr.Player)

	def test_nextRound(self):
		gsTemp = gs.GameState(10)
		self.assertEqual(gsTemp.round, 0)
		self.assertEqual(len(gsTemp.roundList), 1)
		gsTemp.nextRound()
		self.assertEqual(gsTemp.round, 1)
		self.assertEqual(len(gsTemp.roundList), 2)
		for i in range(5):
			gsTemp.nextRound()
		self.assertEqual(gsTemp.round, 4)
		self.assertEqual(len(gsTemp.roundList), 5)


	def test_isOver(self):
		gsTemp5 = gs.GameState(5)
		gsTemp5Fail = gs.GameState(5)
		gsTemp10 = gs.GameState(10)
		gsTemp10Fail = gs.GameState(10)
		self.assertEqual(gsTemp5.isOver(), False)
		self.assertEqual(gsTemp5Fail.isOver(), False)
		self.assertEqual(gsTemp10.isOver(),False)
		self.assertEqual(gsTemp10Fail.isOver(),False)

		#Round1
		gsTemp5.roundList[0].missionResults = [True,True]
		gsTemp5Fail.roundList[0].missionResults = [True,True]
		gsTemp10.roundList[0].missionResults = [True,True,True]
		gsTemp10Fail.roundList[0].missionResults = [True,True,True]
		self.assertEqual(gsTemp5.isOver(), False)
		self.assertEqual(gsTemp5Fail.isOver(), False)
		self.assertEqual(gsTemp10.isOver(),False)
		self.assertEqual(gsTemp10Fail.isOver(),False)
		gsTemp5.nextRound()
		gsTemp5Fail.nextRound()
		gsTemp10.nextRound()
		gsTemp10Fail.nextRound()

		#Round2
		gsTemp5.roundList[1].missionResults = [True,True,True]
		gsTemp5Fail.roundList[1].missionResults = [True,True,False]
		gsTemp10.roundList[1].missionResults = [True,True,False,True]
		gsTemp10Fail.roundList[1].missionResults = [True,True,False,True]
		self.assertEqual(gsTemp5.isOver(), False)
		self.assertEqual(gsTemp5Fail.isOver(), False)
		self.assertEqual(gsTemp10.isOver(),False)
		self.assertEqual(gsTemp10Fail.isOver(),False)
		gsTemp5.nextRound()
		gsTemp5Fail.nextRound()
		gsTemp10.nextRound()
		gsTemp10Fail.nextRound()

		#Round3
		gsTemp5.roundList[2].missionResults = [True,True]
		gsTemp5Fail.roundList[2].missionResults = [True,False]
		gsTemp10.roundList[2].missionResults = [True,True,False,True]
		gsTemp10Fail.roundList[2].missionResults = [True,True,False,True]
		self.assertEqual(gsTemp5.isOver(), True)
		self.assertEqual(gsTemp5Fail.isOver(), False)
		self.assertEqual(gsTemp10.isOver(),False)
		self.assertEqual(gsTemp10Fail.isOver(),False)
		gsTemp5Fail.nextRound()
		gsTemp10.nextRound()
		gsTemp10Fail.nextRound()

		#Round4
		gsTemp5Fail.roundList[3].missionResults = [True,True,False]
		gsTemp10.roundList[3].missionResults = [True,True,False,True,True]
		gsTemp10Fail.roundList[3].missionResults = [True,True,False,False,True]
		self.assertEqual(gsTemp5Fail.isOver(), True)
		self.assertEqual(gsTemp10.isOver(),False)
		self.assertEqual(gsTemp10Fail.isOver(),True)
		gsTemp10.nextRound()

		#Round5
		gsTemp10.roundList[4].missionResults = [True,True,True,True,True]
		self.assertEqual(gsTemp10.isOver(),True)


Res = plr.Player(0,1)
Spy = plr.Player(1,0)
class PlayerCase(unittest.TestCase):
	
	def test_ID(self):
		self.assertEqual(Res.ID, 0)

	def test_alliance(self):
		self.assertEqual(Spy.alliance, 0)

	# def test_castVote(self):
	# 	self.assertEqual(Spy.castVote(1), 1)

	def test_castVote_4_fails(self):
		self.assertEqual(Spy.castVote(4), 1)

class RoundCase(unittest.TestCase):

	def execMission(self):
		pass

		
		
if __name__ == '__main__':
    unittest.main()