#Welcome
print("Welcome to Xs and Os! Xs and Os is a tic tac toe game coded entirely in Python!")
start = input("Do you want to play? y/n ")
while start.upper() != "Y" and start.upper() != "N":
    start = input("What?! You have to enter Y or N!")

if start.upper() == "Y":
    #--------------Global varibles--------------#
    #Game Board
    board = ["-","-","-","-","-","-","-","-","-"]
    #Is game still going
    game_still_going = True
    #Game winner
    winner = None
    #Who's Turn is it
    current_player = "X"

#Play game or quit
    def DisplayBoard():
        print("\n")
        print(board[0] + " | " + board[1] + " | " + board[2] + "   " + "1" + " | " + "2"  + " | " + "3" )
        print(board[3] + " | " + board[4] + " | " + board[5] + "   " + "4" + " | " + "5"  + " | " + "6" )
        print(board[6] + " | " + board[7] + " | " + board[8] + "   " + "7" + " | " + "8"  + " | " + "9" )
        print("\n")

    def PlayGame():
        DisplayBoard()
        while game_still_going:
            HandleTurn(current_player)
            check_if_game_over()
            flip_player()
        #Show who won or if it is a tie
        if winner == "X" or winner == "O":
            print(winner +" has won the game!")
        else:
            print("It's a tie!")

    def HandleTurn(player):
        #Ask for position
        print("It is " + player + "'s turn")
        position = input("Choose a position from 1-9: ")

        while position not in ["1","2","3","4","5","6","7","8","9"] or board[int(position) - 1] != "-":
            if position not in ["1","2","3","4","5","6","7","8","9"]:
                position = input("Invalid position. Please choose a position from 1-9: ")
            else:
                position = input("Position already taken. Please choose another position from 1-9: ")

        board[int(position) - 1] = player
        DisplayBoard()

    def check_if_game_over():
        check_for_winner()
        check_if_tie()

    def check_for_winner():
        CheckRows()
        CheckColumns()
        CheckDiagonals()

    def CheckRows():
        #Set up global varibles
        global game_still_going
        global winner
        #Check if rows have same value and aren't empty
        row_1 = board[0] == board[1] == board[2] != "-"
        row_2 = board[3] == board[4] == board[5] != "-"
        row_3 = board[6] == board[7] == board[8] != "-"
        #Stop game if row winner
        if row_1 or row_2 or row_3:
            game_still_going = False
        #Reveal winner
        if row_1:
            winner = board[0]
        elif row_2:
            winner = board[3]
        elif row_3:
            winner = board[6]
        return

    def CheckColumns():
        #Set up global varibles
        global game_still_going
        global winner
        #Check if rows have same value and aren't empty
        column_1 = board[0] == board[3] == board[6] != "-"
        column_2 = board[1] == board[4] == board[7] != "-"
        column_3 = board[2] == board[5] == board[8] != "-"
        #Stop game if row winner
        if column_1 or column_2 or column_3:
            game_still_going = False
        #Reveal winner
        if column_1:
            winner = board[0]
        elif column_2:
            winner = board[1]
        elif column_3:
            winner = board[2]
        return

    def CheckDiagonals():
        #Set up global varibles
        global game_still_going
        global winner
        #Check if rows have same value and aren't empty
        diagonal_1 = board[0] == board[4] == board[8] != "-"
        diagonal_2 = board[2] == board[4] == board[6] != "-"
        #Stop game if row winner
        if diagonal_1 or diagonal_2:
            game_still_going = False
        #Reveal winner
        if diagonal_1:
            winner = board[0]
        elif diagonal_2:
            winner = board[2]
        return

    def check_if_tie():
        #Set up global varibles
        global game_still_going
        #Check if - is in board
        if "-" not in board:
            game_still_going = False

    def flip_player():
        #Set up global varibles
        global current_player
        #Swap player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    PlayGame()

else:
    print("\nSad to see you go! Bye! :(")
    exit()
