import sys
from os.path import abspath, join, dirname
from heapq import heapify, heappop, heappush
sys.path.append(abspath(join(dirname(__file__), '..')))
from data.fetch import read_file_to_list

class RAMRun:
    def __init__(self):
        self.clean_data()
        self.dim = 70

    def clean_data(self):
        data = read_file_to_list('/Users/dhruvix/Documents/Personal/aoc/data/day18.txt')
        data = [list(map(int, d.split(','))) for d in data]
        self.bytes = data

    def puzzle1(self, num_bytes=0):
        self.grid = [['.'] * (self.dim + 1) for _ in range(self.dim + 1)]
        for n in range(num_bytes):
            [j, i] = self.bytes[n]
            self.grid[i][j] = '#'
        visited = set()
        hq = [(0, 0, 0)]
        heapify(hq)
        while len(hq):
            path_len, r, c = heappop(hq)
            if (r, c) in visited: continue
            visited.add((r, c))
            if r == self.dim and c == self.dim:
                return path_len
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = r + dr
                nc = c + dc
                if (nr, nc) not in visited and 0 <= nr <= self.dim and 0 <= nc <= self.dim and self.grid[nr][nc] != '#':
                    heappush(hq, (path_len + 1, nr, nc))
        return (self.dim + 1) ** 2 + 1

    def puzzle2(self):
        left, right = 0, len(self.bytes) + 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            val = self.puzzle1(mid)
            if val == (self.dim + 1) ** 2 + 1:
                result = mid
                right = mid - 1
            elif val < (self.dim + 1) ** 2 + 1:
                left = mid + 1
            else:
                right = mid - 1
        return self.bytes[result - 1]

rr = RAMRun()
print(rr.puzzle1(1024))
print(rr.puzzle2())