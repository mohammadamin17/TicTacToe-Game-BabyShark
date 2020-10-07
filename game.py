from pandas import *

print("Tic Tac Toe Game - Baby Shark Edition\n")

#The tic tac toe board is below, players will take turns putting their shark characters in the empty 5 character strings using a redefine variable arguement

ttt =[["+","-----","+","-----","+","-----","+"],
      ["|","     ","|","     ","|","     ","|"],
      ["+", "-----", "+", "-----", "+", "-----", "+"],
      ["|", "     ", "|", "     ", "|", "     ", "|"],
      ["+","-----","+","-----","+","-----","+"],
      ["|","     ","|","     ","|","     ","|"],
      ["+", "-----", "+", "-----", "+", "-----", "+"]]

game = " " #default placeholder variable until winner or draw is decided
turn = 1 #defining variable start
player = "" #dummy placeholder
print(DataFrame(ttt), "\n")

#while game has no conclusion (draw or win), keep looping turns

while game==" ":

    if turn == 10:
        game="Draw" #hard stop on game after 9 turns and no winner is decided
        break
    elif (turn%2)>0: #to alternate players every turn there is an arugement at the end of the loop, refer to line 59
        player="Baby shark <>< "
    else: player="Mama Shark <:)<"

    print("Your turn, " + player + ", please enter your row and column positions below!\n")

    tttrow="none" #defining variable as well as to reset loops below
    tttcol="none" #defining variable as well as to reset loops below

    #while loop runs unless valid entry is inputted
    while tttrow == "none":
        tttrow_string = input("Row Input (Top/Middle/Bottom):")
        if tttrow_string == "Top" or tttrow_string == "top":
            tttrow = 1
        elif tttrow_string == "Middle" or tttrow_string ==  "middle":
            tttrow = 3
        elif tttrow_string == "Bottom" or tttrow_string == "bottom":
            tttrow = 5

    #while loop runs unless valid entry is inputted
    while tttcol == "none":
        tttcol_string = input("Column Input (Left/Middle/Right):")
        if tttcol_string == "Left" or tttcol_string =="left":
            tttcol = 1
        elif tttcol_string == "Middle" or tttcol_string =="middle":
            tttcol = 3
        elif tttcol_string == "Right" or tttcol_string == "right":
            tttcol = 5

    #if move is correct, play move and continue, if not, try again
    if ttt[tttrow][tttcol] == "     ":
        ttt[tttrow][tttcol] = player[-4:]
        turn += 1  # every complete successful turn goes into the next loop iteration, giving the other player a turn, refer to line 27
        print("\n", DataFrame(ttt), "\n")
    else: print("\n", "*** You can't take this cell, please try again ***\n")

    if (ttt[1][1] == ttt[1][3] == ttt[1][5] == player[-4:]) or (ttt[1][1] == ttt[3][1] == ttt[5][1] == player[-4:]) or (ttt[3][1] == ttt[3][3] == ttt[3][5] == player[-4:]) or (ttt[1][3] == ttt[3][3] == ttt[5][3] == player[-4:]) or (ttt[5][1] == ttt[5][3] == ttt[5][5] == player[-4:]) or (ttt[1][5] == ttt[3][5] == ttt[5][5] == player[-4:]) or (ttt[1][1] == ttt[3][3] == ttt[5][5] == player[-4:]) or (ttt[1][5] == ttt[3][3] == ttt[5][1] == player[-4:]):
        game = "Won"
        print(f"{player[:10]} doo, doo, doo, doo, doo, doo\n" * 3, player) #baby shark song for winner

if game=="Draw!":
    print(game) #game ends as draw on the end of the 10th turn if loop n = 9 ends with no winner
