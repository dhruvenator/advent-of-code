import sys
from os.path import abspath, join, dirname
sys.path.append(abspath(join(dirname(__file__), '..')))
from data.fetch import read_file_to_list

class RaceCondition:
    def __init__(self):
        self.clean_data()

    def clean_data(self):
        data = read_file_to_list('/Users/dhruvix/Documents/Personal/aoc/data/day20.txt')
        self.racetrack = [list(x) for x in data]
        self.rows = len(self.racetrack)
        self.cols = len(self.racetrack[0])
        self.dist = [[-1] * self.cols for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                if self.racetrack[r][c] == 'E':
                    self.end = (r, c)
                if self.racetrack[r][c] == 'S':
                    self.start = (r, c)
                    self.dist[r][c] = 0
        q = [self.start]
        while q:
            r, c = q.pop(0)
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= self.rows or nc >= self.cols: continue
                if self.racetrack[nr][nc] == '#': continue
                if self.dist[nr][nc] == -1:
                    self.dist[nr][nc] = self.dist[r][c] + 1
                    q.append((nr, nc))

    def puzzle1(self, time_saved=0):
        cheat_count = 0
        time_saved += 2
        visited = set()
        for r in range(self.rows):
            for c in range(self.cols):
                if self.dist[r][c] == -1: continue
                for dr, dc in [(0, 2), (0, -2), (2, 0), (-2, 0)]:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= self.rows or nc >= self.cols: continue
                    if self.dist[nr][nc] == -1: continue
                    if (r, c, nr, nc) in visited or (nr, nc, r, c) in visited: continue
                    if abs(self.dist[r][c] - self.dist[nr][nc]) >= time_saved:
                        cheat_count += 1
                        visited.add((r, c, nr, nc))
        return cheat_count

    def puzzle2(self, time_saved=0, cheat_dist=2):
        cheat_count = 0
        visited = set()
        for r in range(self.rows):
            for c in range(self.cols):
                if self.dist[r][c] == -1: continue
                for radius in range(2, cheat_dist + 1):
                    for dr in range(radius + 1):
                        dc = radius - dr
                        dx = {(dr, dc), (dr, -dc), (-dr, dc), (-dr, -dc)}
                        for dr, dc in dx:
                            nr, nc = r + dr, c + dc
                            if nr < 0 or nc < 0 or nr >= self.rows or nc >= self.cols: continue
                            if self.dist[nr][nc] == -1: continue
                            if (r, c, nr, nc) in visited or (nr, nc, r, c) in visited: continue
                            if abs(self.dist[r][c] - self.dist[nr][nc]) >= time_saved + radius:
                                cheat_count += 1
                                visited.add((r, c, nr, nc))
        return cheat_count

rc = RaceCondition()
print(rc.puzzle1(100))
print(rc.puzzle2(100, 20))