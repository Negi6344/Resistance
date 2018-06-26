import GameState as GS
import Player as PL

def main():

	#initiate game/ create gamestate
		#players are made
		#roles are given

	myGameState = GS.GameState()

	#round sequencing
		#a leader is chosen (first one is random)
		#leader picks a team
			#stats are updated
			#accepted or 5th team selection 
				#mission success
					#nothing
				#mission fail
					#stats are updated
			#fail
				#leadership rotates and new team is picked
		#check if the game is over
			#over
				#endgame
			#not over
				#go another round
	while (myGameState.isOver() != True):
		#myGameState.playRound()
		currRound = myGameState.getCurrentRound()

		missionStatus = False

		while (missionStatus == False and currRound.numAttempts < 5):
			# Select Leader and Select Team (Print Player List)
			currLeader = myGameState.getCurrentLeader()

			if not PL.isCom(currLeader):
				print('\n')
				for player in myGameState.playerList:
					print(str(player) + '\n')
				print('\n')

			currTeam = currRound.selectTeam(currLeader, myGameState.getNumMissionPlayers(myGameState.round), myGameState.playerList)

		# Each player votes on the Team

			myGameState.printPlayers(currTeam)
			for player in myGameState.playerList:
				currRound.addTeamVote(currLeader, player, player.castVote(currRound.numAttempts, currTeam))

		# Check Vote

			if currRound.checkVote(currLeader):
				missionStatus = True
			else:
				currRound.numAttepts = currRound.numAttempts + 1
			myGameState.nextLeader()

		# Excecute Mission

		currRound.execMission()

		myGameState.printRoundResults()
		myGameState.nextRound()

	







if __name__ == '__main__':
	main()
