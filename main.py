from operator import  indexOf
import time


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

    def win(self,letter):
        for row in self.board:
            
            for col in range(len(self.board[0])-3):
                if all([self.board[indexOf(self.board,row)][col+x]==' '+letter+' ' for x in range(4)]):
                    return True
                    
        for col in range(len(self.board[0])):              
            for row in range(len(self.board)-3):
                if all([self.board[row+x][col]==' '+letter+' ' for x in range(4)]):
                    return True

        for row in range(len(self.board)):
            for col in range(len(self.board[0])):        
                if row <= 2 and col <= 3 :
                    if all([self.board[row+x][col+x]==' '+letter+' ' for x in range(4)]):
                        return True
                elif row <= 2 and col <= 6 :    
                    if all([self.board[row+x][col-x]==' '+letter+' ' for x in range(4)]):
                        return True
                elif row > 2 and col <= 3 :        
                    if all([self.board[row-x][col+x]==' '+letter+' ' for x in range(4)]):
                        return True 
                else:
                    if all([self.board[row-x][col-x]==' '+letter+' ' for x in range(4)]):
                        return True 
        return False   





def play(game:Game)->None:
    
    player1 = 'x'
    player2 = 'o'
    
    player =  player1

    while True:
        
        c = int(input('Enter a column number to play:  '))
        while not game.valid_input(c):
            c = int(input('Enter a column number to play:  '))

        game.insert_piece(c,player)
        if game.win(player):
            print(f'Player {player} won')
            break
        if player == player1:
            player = player2
        else:
            player = player1


if __name__=='__main__':
    game = Game(6,7)
    play(game)
     
    






     



