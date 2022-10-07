from operator import index, indexOf
import time


from matplotlib.widgets import EllipseSelector


class Game:
    def __init__(self,r:int,c:int) -> None:
        self.r = r
        self.c = c
        self.board = [['   ' for i in range(c)] for j in range(r)]
    
    def __str__(self) -> str:
            
        print(' ' +' '.join([ ' '+ str(i)+ ' ' for i in range(1,len(self.board[0])+1)]))
        
        for row in self.board:
            print('+'.join(['---' for i in range(len(row))]).join('++'))
            print('|'.join(['   ' for i in range(len(row))]).join('||'))
            print('|'.join(row).join('||'))
            print('|'.join(['   ' for i in range(len(row))]).join('||'))

        print('+'.join(['---' for i in range(len(row))]).join('++'))
        return ""


    def valid_input(self, c:int) -> bool:
    
        return c <= len(self.board[0]) and self.board[0][c-1] == '   '  

    def insert_piece(self,c:int,letter:str):

        for row in range(len(self.board)-1,-1,-1):
            if self.board[row][c-1] == '   ':
                self.board[row][c-1] = ' '+letter+' '
                break
        print(self)

    def reset_board(self):
        self.__init__(self.r,self.c)         





def user_play(letter:str,game):
    c = len(game.board[0])+1
    time.sleep(1)
    while not game.valid_input(c):
        c = int(input("Enter Column Number:   "))
        print(game)
    time.sleep(1)
    game.insert_piece(c,letter.upper())    

game1 = Game(6,7)


def win(game,letter):
    for row in game.board:
        
        for col in range(len(game.board[0])-3):
            if all([game.board[indexOf(game.board,row)][col+x]==' '+letter+' ' for x in range(4)]):
                return True
                
    for col in range(len(game.board[0])):              
        for row in range(len(game.board)-3):
            if all([game.board[row+x][col]==' '+letter+' ' for x in range(4)]):
                return True

    for row in range(len(game.board)):
        for col in range(len(game.board[0])):        
            if row <= 2 and col <= 3 :
                if all([game.board[row+x][col+x]==' '+letter+' ' for x in range(4)]):
                    return True
            elif row <= 2 and col <= 6 :    
                if all([game.board[row+x][col-x]==' '+letter+' ' for x in range(4)]):
                    return True
            elif row > 2 and col <= 3 :        
                if all([game.board[row-x][col+x]==' '+letter+' ' for x in range(4)]):
                    return True 
            else:
                if all([game.board[row-x][col-x]==' '+letter+' ' for x in range(4)]):
                    return True 
    return False    
     

win(game1,'o')

print(game1)

game1.reset_board()

game1.board[5][0]

for i in range(len(game1.board)):
    print(i)

user_play('x',game1)
user_play('o',game1)






print(game1)

win(game1,'x')



c=7
r=6

test = [[' ('+str(j)+' , '+str(i) +') ' for i in range(c)] for j in range(r)]

for row in test:
    print(row)

# if row < 3 and column <5 check + 1 col + 1 row up to (0,0) -> (2,3)
# if row < 3 and column >5 check -1 col + 1 row (2,3) -> (2,6)
# if row > 3 and column <5 check + 1 col - 1 row (3,0) -> (3,3)
# if row > 3 and column >5 check -1 col - 1 row (3,4) ->
