import random
import os

os.system('cls' if os.name == 'nt' else 'clear')
Symbol = ""
board = []
user_name1 = input("What is name of player one?   ")
user_name2 = input("What is name of player two?   ")


def drawBoard():
    print("\n")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("~~~~~~~~~~~")                          
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("~~~~~~~~~~~")
    print(" " + board[1] + " | " + board[2] + " | " + board[3], "\n")

def whoStarts():
      iTurn = random.randint(1, 2)
      if iTurn == 1:
            print(user_name1,("can start."))
            print("You are with X.")
            return "X"

      else:
            print(user_name2,("can start."))
            print("You are with O.")
            return "O"

def doMove(Symbol,move):
      nums = [i for i in range(1, 10)]
      while not move in nums:
            try:
                 print("Choose a between 1 and 9")
                 if Symbol == "O":
                        iTurn = 1
                        while iTurn == 1:
                              move = int(input(": "))
                              if board[move] == " ":
                                    board[move] = Symbol
                                    iTurn -= 1
                              else:
                                    print("Choose an empty bracket!")
                                    drawBoard()
                 else:
                        iTurn = 0
                        while iTurn == 0:
                              move = int(input(": "))
                              if board[move] == " ":
                                    board[move] = Symbol
                                    iTurn += 1
                              else:
                                    print("Choose an empty bracket!")

            except (ValueError, IndexError):
                pass

def isWinner():
      winValues = ([7, 8, 9], [4, 5, 6], [1, 2, 3], [7, 4, 1, ], [8, 5, 2], [9, 6, 3], [7, 5, 3], [9, 5, 1])
      for value in winValues:
            if (board[(value[0])] == board[(value[1])] == board[(value[2])] == "X"):
                  drawBoard()
                  print("You won,",user_name1)
                  rematch()


            elif (board[(value[0])] == board[(value[1])] == board[(value[2])] == "O"):
                  drawBoard()
                  print("You won,",user_name2)
                  rematch()

            else:
                  pass

def rematch():
      global board
      re_match = input("Rematch?(y/n): ")
      if re_match == "y" or re_match == "yes":
            board = [' '] * 10

      else:
            quit()

def isFull():
      global Symbol
      if ' ' in board[1:10]:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nNext player")
            if Symbol == "X":
                  Symbol = "O"
            else:
                  Symbol = "X"
      else:
            print("\nIt's a tie!")
            drawBoard()
            rematch()

while True:
      board = [' '] * 10
      Symbol = whoStarts()
      gameIsOn = True

      while gameIsOn:
            drawBoard()
            move = None
            doMove(Symbol, move)
            if isWinner():
                  drawBoard(board)
                  rematch()

            elif isFull():
                  drawBoard()
                  rematch()