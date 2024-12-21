import sys
from os.path import abspath, join, dirname
from heapq import heapify, heappop, heappush
from copy import deepcopy
sys.path.append(abspath(join(dirname(__file__), '..')))
from data.fetch import read_file_to_list

class ReindeerMaze:
    def __init__(self):
        self.clean_data()

    def clean_data(self):
        data = read_file_to_list('/Users/dhruvix/Documents/Personal/aoc/data/day16.txt')
        self.maze = [list(x) for x in data]
        self.rows = len(self.maze)
        self.cols = len(self.maze[0])
        for r in range(self.rows):
            for c in range(self.cols):
                if self.maze[r][c] == 'E':
                    self.end = (r, c)
                if self.maze[r][c] == 'S':
                    self.start = (r, c)
    
    def print_maze(self, marked):
        maze = deepcopy(self.maze)
        for r, c in marked:
            maze[r][c] = 'O'
        for g in maze:
            print(''.join(g))

    def puzzle1(self):
        hq = [(0, self.start[0], self.start[1], 0, 1)]
        heapify(hq)
        visited = set()
        while len(hq):
            cost, r, c, dr, dc = heappop(hq)
            if self.maze[r][c] == 'E':
                return cost
            visited.add((r, c, dr, dc))
            x = (cost + 1, r + dr, c + dc, dr, dc)
            y = (cost + 1001, r - dc, c - dr, -dc, -dr)
            z = (cost + 1001, r + dc, c + dr, dc, dr)
            for ele in [x, y, z]:
                if self.maze[ele[1]][ele[2]] != '#' and (ele[1], ele[2], ele[3], ele[4]) not in visited: heappush(hq, ele)

    def puzzle2(self):
        hq = [(0, self.start[0], self.start[1], 0, 1, [self.start])]
        sitting_positions = set()
        min_cost = 1000 * self.rows * self.cols
        heapify(hq)
        visited = set()
        while len(hq):
            cost, r, c, dr, dc, track = heappop(hq)
            visited.add((r, c, dr, dc))
            if self.maze[r][c] == 'E':
                min_cost = min(cost, min_cost)
                if cost == min_cost:
                    sitting_positions.update(set(track))
                else:
                    break
            x = (cost + 1, r + dr, c + dc, dr, dc, track + [(r + dr, c + dc)])
            y = (cost + 1001, r - dc, c - dr, -dc, -dr, track + [(r - dc, c - dr)])
            z = (cost + 1001, r + dc, c + dr, dc, dr, track + [(r + dc, c + dr)])
            for ele in [x, y, z]:
                if self.maze[ele[1]][ele[2]] != '#' and (ele[1], ele[2], ele[3], ele[4]) not in visited: heappush(hq, ele)
        return len(sitting_positions)

rm = ReindeerMaze()
print(rm.puzzle1())
print(rm.puzzle2())