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
print(" ")
players = input("How many players?\n")
print(" ")
roundNum = input("What round is it?\n")
print(" ")

numRes = numOfGood[players]
teamSize = missionPlayers[players][roundNum-1]
if (players >= 7) and (roundNum == 4):
	failsNeeded = 2
else: 
	failsNeeded = 1

playerList = []
for i in range(players):
	playerList = playerList + [i]

badList = [1,3,6,9]

possTeam = list(IT.combinations(playerList,teamSize))

print("---------------------------------------------------\n")
print("Number of possible teams: " + str(len(possTeam)) + "\n")

teamsIn = 0
for team in possTeam:
	if 0 in team:
		teamsIn = teamsIn + 1

print("Number of teams you are in: " + str(teamsIn) + "\n")

teamsInFail = 0
teamsFail = 0
teamsWO = 0
teamsWOSucc = 0
for team in possTeam:
	bad = 0
	if 0 not in team:
		teamsWO = teamsWO + 1
	for i in badList:
		if i in team:
			bad = bad + 1
	if bad >= failsNeeded:
		teamsFail = teamsFail + 1
		if 0 in team:
			teamsInFail = teamsInFail + 1
	elif 0 not in team and bad < failsNeeded:
		teamsWOSucc = teamsWOSucc + 1

print("Number of teams that can fail: " + str(teamsFail) + "\n")
print("Number of teams you are in and can fail: " + str(teamsInFail) + "\n")
print("Success rate with you in it: " + str(float(teamsIn-teamsInFail)/teamsIn) + "\n")
print("Overall complete success rate: " + str(1 - (float(teamsFail)/len(possTeam))) + "\n")
print("Number of teams w/o you: " + str(teamsWO) + "\n")
print("Number of teams that complete success w/o you: " + str(teamsWOSucc) + "\n")
print("Overall complete success rate: " + str(float(teamsWOSucc)/teamsWO) + "\n")

print("-----------------------------------------------------\n")