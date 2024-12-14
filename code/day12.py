import sys
from os.path import abspath, join, dirname
sys.path.append(abspath(join(dirname(__file__), '..')))
from data.fetch import read_file_to_list

class GardenGroups:
    def __init__(self):
        self.clean_data()
        self.rows = len(self.garden)
        self.cols = len(self.garden[0])
        self.visited = set()

    def clean_data(self):
        data = read_file_to_list('/Users/dhruvix/Documents/Personal/aoc/data/day12.txt')
        self.garden = data
    
    def get_plant_perimeter(self, x, y):
        perimeter = 0
        if x == 0 or self.garden[x-1][y] != self.garden[x][y]:
            perimeter += 1
        if x == self.rows - 1 or self.garden[x+1][y] != self.garden[x][y]:
            perimeter += 1
        if y == 0 or self.garden[x][y-1] != self.garden[x][y]:
            perimeter += 1
        if y == self.cols - 1 or self.garden[x][y+1] != self.garden[x][y]:
            perimeter += 1
        return perimeter
    
    def get_corner_count(self, corners):
        corner_count = 0
        for k, v in corners.items():
            if len(v) == 1 or len(v) == 3:
                corner_count += 1
            elif len(v) == 2 and (v[0][0] + v[1][0], v[0][1] + v[1][1]) == (0, 0):
                corner_count += 2
        return corner_count
    
    def cost_bfs(self, x, y, puzzle):
        plant = self.garden[x][y]
        q = [(x, y)]
        area = 0
        perimeter = 0
        corners = {}
        while q:
            (x, y) = q.pop(0)
            self.visited.add((x, y))
            area += 1
            if puzzle == 1: perimeter += self.get_plant_perimeter(x, y)
            else:
                for dx, dy in [(-0.5, -0.5), (-0.5, 0.5), (0.5, -0.5), (0.5, 0.5)]:
                    corners[(x+dx, y+dy)] = corners.get((x+dx, y+dy), []) + [(dx, dy)]
            for (dx, dy) in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                nx, ny = x + dx, y + dy
                if 0<=nx<self.rows and 0<=ny<self.cols and self.garden[nx][ny] == plant and (nx, ny) not in self.visited:
                    q.append((nx, ny))
                    self.visited.add((nx, ny))
        if puzzle == 1:
            return area * perimeter
        else:
            return area * self.get_corner_count(corners)

    def puzzle1(self):
        cost = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) not in self.visited:
                    cost += self.cost_bfs(r, c, 1)
        return cost

    def puzzle2(self):
        cost = 0
        self.visited = set()
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) not in self.visited:
                    cost += self.cost_bfs(r, c, 2)
        return cost

gg = GardenGroups()
print(gg.puzzle1())
print(gg.puzzle2())