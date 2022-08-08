from unittest.main import MAIN_EXAMPLES
import numpy as np


display = ['*', '!']
adjacent = [[1, 1], [1, 0], [1, -1], [0, 1], [0, -1], [-1, 1], [-1, 0], [-1, -1]]
divide_line = '----------------------------------------'

class Block:
    def __init__(self, x, y, mine=False):
        self.x = x
        self.y = y
        self.mine = mine
        self.type = 0 # 0:*, 1:!, 2:reveal
        self.num = 0
        self.edge = False
        
    def __repr__(self) -> str:
        if self.edge:
            return '='
        elif self.type == 0:
            return '*'
        elif self.type == 1:
            return '!'
        elif self.type == 2:
            if self.mine:
                return 'M'
            else:
                return str(self.num)
        else:
            return 'wrong type of block'
    
    @property
    def change_to_mine(self):
        self.mine = True
        
        
        
class Game:
    def __init__(self, size=9, mine_num=10):
        self.mine_size = size
        self.mine_num = mine_num
        self.size = self.mine_size + 2
        self.status = True # false is game over
        # create a 2D list to store block
        self.blocks = []
        self.remain_block = size * size
        self.remain_mine = self.mine_num
        self.win = False
        
        for i in range(self.size):
            new_list = []
            for j in range(self.size):
                new_block = Block(i, j)
                if i == 0 or j == 0 or i == self.size - 1 or j == self.size - 1:
                    new_block.edge = True
                new_list.append(new_block)
            self.blocks.append(new_list)
        
        # generate random mine
        x_mine = np.random.randint(self.mine_size, size=self.mine_num) + 1
        y_mine = np.random.randint(self.mine_size, size=self.mine_num) + 1
        
        # set block to mine
        for i in range(self.mine_num):
            self.blocks[x_mine[i]][y_mine[i]].change_to_mine
            
        # init number of block
        for i in range(1, self.size - 1):
            for j in range(1, self.size - 1):
                block = self.blocks[i][j]
                adjacent_mine_num = 0
                for x, y in adjacent:
                    if self.blocks[i+x][j+y].mine:
                        adjacent_mine_num += 1
                block.num = adjacent_mine_num
                
    # display the gameboard
    def display(self):
        for list in self.blocks:
            print(list)
    
    # display the answer
    def answer(self):
        for list in self.blocks:
            for block in list:
                block.type = 2
        self.display()
        
    
    # judge if this block is mine
    def if_mine(self, block):
        if block.mine:
            # if it is, game over
            self.status = False
            
    # judge if this block is zero
    # if it is, uncover all around blocks
    def if_zero(self, block):
        block.type = 2
        i, j = block.x, block.y
        if block.num == 0:
            for x, y in adjacent:
                self.click(x+i, y+j)
    
    # click block
    def click(self, x, y):
        block = self.blocks[x][y]
        if block.edge == True:
            return
        if block.type == 2:
            print('You have already clicked this block!')   
            print('Please choose another block')
        elif block.type == 1:
            print('you have flagged this block!')
        else:
            # uncover this block
            block.type = 2
            self.remain_block -= 1
            self.if_mine(block)
            self.if_zero(block)
    
    # flag block
    def flag(self, x, y):
        block = self.blocks[x][y]
        block.type = 1
        
    # unflag block
    def unflag(self, x, y):
        block = self.blocks[x][y]
        block.type = 0
        
    # check game is win or not
    def is_win(self):
        if self.status != False:
            if self.remain_block == self.mine_num:
                self.win = True
                self.status = False

# stream of game
def game_start(size=9, mine_num=10):
    game = Game(size=size, mine_num=mine_num)
    while(game.status):
        game.display()
        print('')
        print('Type "c x y" to click block')
        print('Type "f x y" to flag block')
        print('Type "u x y" to unflag block')
        command = input('Enter your move: ').split()
        if command[0] == 'end':
            print('You have abondoned this game!')
            game.status = False
            continue
        x, y = int(command[1]), int(command[2])
        if 0 < x <= size and 0 < y <= size:
            if command[0] == 'c':
                game.click(x, y)
            if command[0] == 'f':
                game.flag(x, y)
            if command[0] == 'u':
                game.unflag(x, y)
            game.is_win()
        else:
            print('Input wrong answer!')

        print(divide_line)
        print('')
    
    if game.win:
        print('You have win!')
    else:
        print('You have lose!')
    
game_start(size=20, mine_num=20)