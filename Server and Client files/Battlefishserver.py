from socket import *
from time import *
from datetime import *
from random import *
from random import randint

game = True
board = []
for x in range(25):
    board.append(["O"] * 25)

# def server():
# 	s = socket (AF_INET, SOCK_STREAM)
# 	s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# 	s.bind(('', 1250))
# 	s.listen(5)
# 	ts = ('Timestamp {:%Y-%m-%d %H:%M:%S}:'.format(datetime.now()))
# 	f = open('CommunicatingLog.txt', 'w')
# 	openS = True
# 	while True and openS == True:
# 		print ('Waiting for connection...')
# 		clientconn, addr = s.accept()
# 		print ('waiting for authentication..')
# 		username = clientconn.recv(1024).decode()
# 		print ('Connected by', addr)
# 		print ('Authentication recieved')
# 		clientconn.sendall(("Welcome to BattleFish " + username + "." "\n Awaiting player 2. \n please stand by.").encode())
# 		while game == True:
# 			battleFish()



# server()
def battleFish():
	def print_board(board):
	    for row in board:
	        print(" ".join(row))


	print("Let's play Battlefish!")
	print_board(board)

	def random_row(board):
	    return randint(0, len(board) - 1)

	def random_col(board):
	    return randint(0, len(board[0]) - 1)

	#ship_row = random_row(board)
	#ship_col = random_col(board)
	def place_fish(board):
		ship_array = []
		for i in range 14:
			ship_row = random_row(board)
			ship_col = random_col(board)
			ship_array.append(ship_row,ship_col)
		print(ship_array)
	place_fish(board)
	
	for turn in range(0,26):
	    guess_row = int(input("Guess Row:"))
	    guess_col = int(input("Guess Col:"))

	    if guess_row == ship_row and guess_col == ship_col:
	        print("Congratulations! You sunk my battleship!")
	        print_board(board)
	    else:
	        if (guess_row < 0 or guess_row > 25) or (guess_col < 0 or guess_col > 25):
	            print("Oops, that's not even in the ocean.")
	            print_board(board)
	        elif(board[guess_row][guess_col] == "X"):
	            print("You guessed that one already.")
	            print_board(board)
	        else:
	            print("You missed my battleship!")
	            board[guess_row][guess_col] = "X"
	            print_board(board)
	    print("Turn", turn + 1)
	    if turn == 25:
	        print("Game over!")
	        print_board(board)
	        game = False

	# import random

	# board = []

	# for x in range(0,5):
	#     board.append(["O"] * 5)

	# def print_board(board):
	#     for row in board:
	#         print(" ".join(row))

	# print("Let's play Battleship!")
	# print_board(board)

	# def random_row(board):
	#     return random.randint(0,len(board)-1)

	# def random_col(board):
	#     return random.randint(0,len(board[0])-1)

	# ship_row = random_row(board)
	# ship_col = random_col(board)

	# for turn in range(4):
	#     print("Turn: ", turn+1)
	#     guess_row = input("Guess Row: (0-4)")
	#     guess_col = input("Guess Col: (0-4)")

	#     if guess_row == ship_row and guess_col == ship_col:
	#         print("Congratulations! You sunk a battlefish(S)!")
	#         board[ship_row][ship_col] = "S"
	#         print_board(board)
	#         break
	#     else:
	#         if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
	#             print("Oops, that's not even in the ocean.")
	#         elif(board[guess_row][guess_col] == "X"):
	#             print("You guessed that one already.")           
	#         else:
	#             print("You missed a battlefish!")
	#             board[guess_row][guess_col] = "X"
	#             print_board(board)
	#             if turn == 3:
	#                 print("Game Over (S = Battlefish)")
	#                 board[ship_row][ship_col] = "S"
	#                 print_board(board)


def server():
	s = socket (AF_INET, SOCK_STREAM)
	s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	s.bind(('', 1250))
	s.listen(5)
	ts = ('Timestamp {:%Y-%m-%d %H:%M:%S}:'.format(datetime.now()))
	f = open('CommunicatingLog.txt', 'w')
	openS = True
	while True and openS == True:
		print ('Waiting for connection...')
		clientconn, addr = s.accept()
		print ('waiting for authentication..')
		username = clientconn.recv(1024).decode()
		print ('Connected by', addr)
		print ('Authentication recieved')
		clientconn.sendall(("Welcome to BattleFish " + username + "." "\n Awaiting player 2. \n please stand by.").encode())
		while game == True:
			battleFish()

server()