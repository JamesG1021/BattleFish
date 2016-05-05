from socket import *
from time import *
from datetime import *
from random import *
#from random import randint

#game = True
board = []
guesses = []
ship_array = []
hits = []
# for x in range(25):
#     board.append(["O"] * 25)


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

def server():
    #game = True

    s = socket(AF_INET,SOCK_STREAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(('',50000))
    s.listen(100)
    ts = ('Timestamp {:%Y-%m-%d %H:%M:%S}:'.format(datetime.now()))
    f = open('CommunicatingLog.txt','w')
    openS = True
    # while True and openS == True:
    #     print('Waiting for connection...')
    #     for i in range(2):
    #         clientconn,addr = s.accept()
    #         print('Waiting for authentication..')
    #         username = clientconn.recv(1024).decode()
    #         print('Connected by',addr)
    #         print('Authentication recieved')
    #         clientconn.sendall(("Welcome to BattleFish " + username + "." " \n Please stand by.").encode())
    #     # while game == True:
    #     #clientconn.close()
    def battleFish():
        game = True
        for x in range(25):
            board.append(["O"] * 25)

        def print_board(board):
            for row in board:
                boardRow = (" ".join(row))
                # clientconn.send(boardRow.encode())
                print (boardRow)

        print("Let's play Battlefish!")
        print_board(board)

        def emptyBoard(board):
            del board[:]

        def random_row(board):
            return randint(0,len(board) - 1)

        def random_col(board):
            return randint(0,len(board[0]) - 1)

            # ship_row = random_row(board)
            # ship_col = random_col(board)

        def place_fish(board):
            for i in range(14):
                ship_row = random_row(board)
                ship_col = random_col(board)
                ship_array.append([ship_row,ship_col])
            print(ship_array)

        place_fish(board)

        #for turn in range(0,10):
        turn = 1
        score = 0
        while game == True:

            for turn in range(12):
                # guess_row = int(input("Guess Row:"))
                # guess_col = int(input("Guess Col:"))
                guess_row = clientconn.recv(1024).decode()
                guess_col = clientconn.recv(1024).decode()
                print("Turn: ",turn + 1)

                if turn == 11:
                    gameOver = "Game Over!"
                    clientconn.send(gameOver.encode())
                    print("\nHere is the final board after the game has finished!")
                    print_board(board)
                    emptyBoard(board)
                    scoreSend = str(score)
                    clientconn.send(scoreSend.encode())
                    game = False
                elif [int(guess_row),int(guess_col)] in ship_array:
                    congrats = "Congratulations! You sunk a battlefish!"
                    clientconn.send(congrats.encode())
                    board[int(guess_row)][int(guess_col)] = "H"
                    ship_array.remove([int(guess_row),int(guess_col)])
                    hits.append([int(guess_row),int(guess_col)])
                    print_board(board)
                    score += 1
                elif [int(guess_row),int(guess_col)] in hits:
                    alreadyHit = "That fish has already been sunk!!"
                    clientconn.send(alreadyHit.encode())
                    print_board(board)
                elif (int(guess_row) < 0 or int(guess_row) > 25) or (int(guess_col) < 0 or int(guess_col) > 25):
                    missedBoard = "Oops, that's not even in the ocean."
                    clientconn.send(missedBoard.encode())
                    # print_board(board)
                elif (board[int(guess_row)][int(guess_col)] == "X"):
                    alreadyGuessed = "You guessed that one already."
                    clientconn.send(alreadyGuessed.encode())
                    print_board(board)
                else:
                    missed = "You missed my battlefish!"
                    clientconn.send(missed.encode())
                    board[int(guess_row)][int(guess_col)] = "X"
                    print_board(board)
                turn += 1
        #print("Turn",turn + 1)

    # battleFish()

    # if turn == 25:
    # 	print("Game over!")
    # 	print_board(board)
    # 	game = False

    # s = socket(AF_INET,SOCK_STREAM)
    # s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    # s.bind(('',1250))
    # s.listen(5)
    # ts = ('Timestamp {:%Y-%m-%d %H:%M:%S}:'.format(datetime.now()))
    # f = open('CommunicatingLog.txt','w')
    # openS = True
    while True and openS == True:
        print('Waiting for connection...')
        for i in range(1):
            clientconn,addr = s.accept()
            print('Waiting for authentication..')
            username = clientconn.recv(1024).decode()
            print('Connected by',addr)
            print('Authentication received')
            clientconn.sendall(
            ("Welcome to BattleFish " + username + ".").encode())
        battleFish()
        # while game == True:

server()

