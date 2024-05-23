# This table receives numPlayers, numEnemies, and numAllies as input
# It then prompts for their name and initiative modifier
# Once values are input,

numPlayers = int(input("How many players in this encounter?\n"))
numEnemies = int(input("How many foes?\n"))
numAllies = int(input("How many allies?\n"))
totalAgents = numPlayers + numEnemies + numAllies

# Create a dictionary assigning Player# to player's name
playerList = {}
if numPlayers > 0:
    for i in range(numPlayers):
        playerList.update({f"Player{i+1}": input(f"Player {i+1}'s name is: \n")})
    print(playerList)

# Create a dictionary assigning Monster# to monster's name
enemyList = {}
if numEnemies > 0:
    for i in range(numEnemies):
        enemyList.update({f"Enemy{i+1}": input(f"Enemy {i+1}'s name is: \n")})
    print(enemyList)

# Create a dictionary assigning Ally# to ally's name
allyList = {}
if numAllies > 0:
    for i in range(numAllies):
        allyList.update({f"Ally{i+1}": input(f"Ally {i+1}'s name is: \n")})
    print(allyList)
