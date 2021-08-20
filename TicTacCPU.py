#imports
import random
import os
import time
#vars
gameStarted = False
logWriter = open("Logs.txt","a")
moves = []
cpu_turn = False
userPossibleMove = 0
cpuPossibleMove = 0
#Generic Functions
def printToLog(str):
    logWriter.write(str + '\n')
def startGame(id):
    global gameStarted
    gameStarted = True
    logWriter.write("Game Started! ID: " + id + '\n')
    logWriter.write('\n')
    gameLoop()
def endGame(id):
    global gameStarted
    gameStarted = False
    logWriter.write("Game with ID: " + id + " was ended!" + '\n')
    logWriter.write('\n')
#User Functions
def user_move():
    userPossibleMove = input("Enter a number 1-9 to take a spot on the board!: ")
    if userPossibleMove in moves:
        print("That spot is already taken!")
        user_move()
    else:
        moves.append(userPossibleMove)
        printToLog("User Moved!")
        cpu_turn = True
#CPU Functions
def cpu_move():
    cpuPossibleMove = random.randint(1,9)
    if cpuPossibleMove in moves:
        cpuPossibleMove = random.randint(1,9)
        printToLog("CPU Move already existed! Trying Again.")
        cpu_move()
    else:
        moves.append(cpuPossibleMove)
        printToLog("CPU Moved!")
        print("The computer took spot: " + str(cpuPossibleMove))
        cpu_turn = False
#Start Games
def gameStarter():
    idForGame = input("Enter an ID for the game: ")
    startGame(idForGame)
#Main Game Loop
def gameLoop():
    global gameStarted
    while (gameStarted == True):
        if cpu_turn == False:
            user_move()
        if cpu_turn == True:
            cpu_move()

#Main!
gameStarter()
