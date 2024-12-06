import sys
from os.path import abspath, join, dirname
sys.path.append(abspath(join(dirname(__file__), '..')))
from data.fetch import read_file_to_list

class CeresSearch:
    def __init__(self, key1, key2):
        self.key1 = key1
        self.key2 = key2
        self.grid = self.clean_data()
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

    def clean_data(self):
        data = read_file_to_list('/Users/dhruvix/Documents/Personal/aoc/data/day4.txt')
        return [list(row) for row in data]
    
    def _directional_string(self, x, y, dx, dy, dist):
        extracted = []
        for i in range(dist):
            nx = x + i*dx
            ny = y + i*dy
            if nx in list(range(self.rows)) and ny in list(range(self.cols)):
                extracted.append(self.grid[nx][ny])
            else:
                break
        return ''.join(extracted)

    def _octa_search(self, i, j):
        strings = []
        deltas = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        for (dx, dy) in deltas:
            strings.append(self._directional_string(i, j, dx, dy, len(self.key1)))
        return len([s for s in strings if s==self.key1])
    
    def _x_search(self, i, j):
        fs1 = self._directional_string(i, j, 1, 1, len(self.key2)//2+1)[::-1]
        fs2 = self._directional_string(i, j, -1, -1, len(self.key2)//2+1)
        bs1 = self._directional_string(i, j, -1, 1, len(self.key2)//2+1)[::-1]
        bs2 = self._directional_string(i, j, 1, -1, len(self.key2)//2+1)
        fs = fs1[:-1] + fs2
        bs = bs1[:-1] + bs2
        xfs = fs == self.key2 or fs == self.key2[::-1]
        xbs = bs == self.key2 or bs == self.key2[::-1]
        return xfs and xbs

    def puzzle1(self):
        key1_occurrances = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == self.key1[0]:
                    key1_occurrances += self._octa_search(i, j)
        return key1_occurrances        
    
    def puzzle2(self):
        if len(self.key2) % 2 != 1: return 0
        key2_occurrances = 0
        ml = self.key2[len(self.key2)//2]
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == ml:
                    key2_occurrances += self._x_search(i, j)
        return key2_occurrances 

cs = CeresSearch('XMAS', 'MAS')
print(cs.puzzle1())
print(cs.puzzle2())