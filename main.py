def sum(a,b,c):
    return a+b+c

def printBoard(xState,zState):

    o0 = 'X' if xState[0] else ('O' if zState[0] else '0')
    o1 = 'X' if xState[1] else ('O' if zState[1] else '1')
    o2 = 'X' if xState[2] else ('O' if zState[2] else '2')
    o3 = 'X' if xState[3] else ('O' if zState[3] else '3')
    o4 = 'X' if xState[4] else ('O' if zState[4] else '4')
    o5 = 'X' if xState[5] else ('O' if zState[5] else '5')
    o6 = 'X' if xState[6] else ('O' if zState[6] else '6')
    o7 = 'X' if xState[7] else ('O' if zState[7] else '7')
    o8 = 'X' if xState[8] else ('O' if zState[8] else '8')

    print(f" {o0} | {o1} | {o2} ")
    print(f"---|---|---")
    print(f" {o3} | {o4} | {o5} ")
    print(f"---|---|---")
    print(f" {o6} | {o7} | {o8} ")

def checkWin(xState, zState):
    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3 :
            printBoard(xState,zState)
            print("X won the match !")
            return 1

        if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3 :
            printBoard(xState,zState)
            print("O won the match !")
            return 0
    
    return -1 

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0 , 0, 0, 0]       #x-axis                                    
    zState = [0, 0, 0, 0, 0, 0 , 0, 0, 0]       #y-axis
    turn = 1                                 #1 for X and 0 for O                                        
    print("Welcome to Tic Tac Toe")
    count = 0 
    play = True
    while(play):
        printBoard(xState,zState)
        count +=1
        if (turn == 1 ):
            print("X's Chance")
            value = int(input("Please enter a value: "))
            xState[value] = 1
        else:
            print("O's Chance")
            value = int(input("Please enter a value: "))
            zState[value] = 1
        cwin = checkWin(xState, zState)
        if cwin != -1 :
            print("Match Over")
            play = False
        if count == 9:
            print("opps!")
            qu = input("Want to play again: Y/N ? = ")
            if qu == 'Y':
                play = True
            else:
                play = False
        turn = 1 - turn
    
        



""" 
1.if __name__: when we are going to run our python pgm then we can make sure whenever it gets imporeted then only function are going to import 
code will not be excuted. If you don't code then also your code is going to work 
2. Then we are going to make  some utility functions
3.when it is X's chance it will tell from 0-7 where it wants to go for that we will use printBoard
4.we will use f string which will like like board 
5.we will put printBoard in while loop
    print(f" 0 | 1 | 2 ")
    print(f"---|---|---")
    print(f" 3 | 4 | 5 ")
    print(f"---|---|---")
    print(f" 6 | 7 | 8 ")

6.when turn = 1 then its X's chance so we will ask input(value i.e index) and make xState = 1 
in else its O's chance so take input and make zState = 1
7. we will pass x and y state to printBoard
in the board we want to write O/X so for that we will make one expression
if xState[0]==0 : print X else if zstate[0] == 1 : O

Turnary operator:
1 if 1 else 0 : 1 
11 if 1 else 0 : 11  if true then print 11 else 0 
11 if 0 else 220 : 220 


8. to check winner we wil code checkWin function pass x and z state
xwin has all possible combination for winnining 
we run one for loop in that we will check 
xState[0]+[1]+[2] == 3 then win 
"""