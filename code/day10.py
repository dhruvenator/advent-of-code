import sys
from os.path import abspath, join, dirname
sys.path.append(abspath(join(dirname(__file__), '..')))
from data.fetch import read_file_to_list

class HoofIt:
    def __init__(self):
        self.clean_data()
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

    def clean_data(self):
        data = read_file_to_list('/Users/dhruvix/Documents/Personal/aoc/data/day10.txt')
        self.start_points = []
        self.grid = [list(map(int, list(row))) for row in data]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 0:
                    self.start_points.append((i, j))

    def get_num_trail_heads(self, sx, sy, puzzle):
        dfs = [(sx, sy)]
        visited_9s = set()
        _9_count = 0
        while dfs:
            (x, y) = dfs.pop(0)
            if self.grid[x][y] == 9:
                if puzzle == 1 and (x, y) not in visited_9s:
                    visited_9s.add((x, y))
                    _9_count += 1
                if puzzle == 2:
                    _9_count += 1
            for (dx, dy) in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                nx, ny = x + dx, y + dy
                if 0<=nx<self.rows and 0<=ny<self.cols and self.grid[nx][ny] == 1 + self.grid[x][y]:
                    dfs.append((nx, ny))
        return _9_count

    def puzzle1(self):
        trail_heads = 0
        for sx, sy in self.start_points:
            trail_heads += self.get_num_trail_heads(sx, sy, 1)
        return trail_heads

    def puzzle2(self):
        trail_heads = 0
        for sx, sy in self.start_points:
            trail_heads += self.get_num_trail_heads(sx, sy, 2)
        return trail_heads

hi = HoofIt()
print(hi.puzzle1())
print(hi.puzzle2())