import pygame
from screen import Screen

class Get_Indexes:
    def get_rows():
        row_list = []
        for col in range(6):
            for row in range(4):
                index = col * 7 + row 
                #print(index)
                if ((index) // 7) == ((index + 1) // 7) == \
                ((index + 2) // 7) ==  ((index + 3) // 7):
                    row_list.append([index,index + 1,index + 2,index + 3])

        return row_list
    
    def get_cols():
        col_list = []
        for index in range(21):
            col_list.append([index,index + 7, index + 14, index + 21])

        return col_list
    
    def get_neg_diags():
        diag_list = []
        for index in range(18):
            if (index // 7 == ((index + 8) // 7 - 1) == \
                ((index + 16) // 7 - 2) == ((index + 24) // 7 - 3)):
                diag_list.append([index,index + 8, index + 16, index + 24])
                
        return diag_list
    
    def get_pos_diags():
        diag_list = []
        for index in range(21):
            if (index // 7 == ((index + 6) // 7 - 1) == \
                ((index + 12) // 7 - 2) == ((index + 18) // 7 - 3)):
                diag_list.append([index,index + 6, index + 12, index + 18])
                
        return diag_list

class Board:
    def __init__(self):
        self.board_list : list = []
        for num in range(42): self.board_list.append(num + 1)

    def print_board(self):
        print()
        print('  ',end='')
        for i in range(7): print(i + 1,end='   ')
        print()
        print('  ',end='')
        for _ in range(7): print('\u2193',end='   ')
        print()

        ldone = 0
        for spot in self.board_list[::-1]:
            if ldone == 0:
                print('| ',end='')
                ldone += 1

        #Printing the colored chip or the empty space
            if isinstance(spot, int): print(' ',end='')
            else: print(spot,end='')

            if ldone == 7:
                print(' | ')
                ldone = 0

            else:
                print(' | ',end='')
                ldone += 1    

    @property
    def legal_moves(self):
        return [8 - ((i % 7) + 1) for i in [41,40,39,38,37,36,35] if isinstance(self.board_list[i],int)]

def run(board : Board):
    pass

if __name__ == '__main__':
    board = Board()
    screen = Screen(400,400,'Connect 4')
    pygame.init()
    run(board)