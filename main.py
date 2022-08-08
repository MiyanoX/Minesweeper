from unittest.main import MAIN_EXAMPLES
import numpy as np


display = ['*', '!', ' ', 'x']

class Block:
    def __init__(self, mine=False):
        self.display_type = 0
        self.mine = mine
        
        
class Game:
    def __init__(self, size=9, mine_num=10):
        self.size = size
        self.mine_num = mine_num
        
        # generate random mine
        x_mine = np.random.randint(self.size, size=self.mine_num)
        y_mine = np.random.randint(self.size, size=self.mine_num)
        
        