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





def user_play(letter:str,game):
    c = len(game.board[0])+1
    time.sleep(1)
    while not game.valid_input(c):
        c = int(input("Enter Column Number:   "))
        print(game)
    time.sleep(1)
    game.insert_piece(c,letter.upper())    

game1 = Game(6,7)

print(game1)


while True:

    user_play('x',game1)
    user_play('o',game1)
