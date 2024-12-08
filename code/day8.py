import sys
from os.path import abspath, join, dirname
sys.path.append(abspath(join(dirname(__file__), '..')))
from data.fetch import read_file_to_list

def clean_data():
    data = read_file_to_list('/Users/dhruvix/Documents/Personal/aoc/data/day8.txt')
    grid = [list(r) for r in data]
    rows = len(grid)
    cols = len(grid[0])
    antennas = {}
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '.':
                antennas[grid[r][c]] = antennas.get(grid[r][c], []) + [(r, c)]
    return rows, cols, antennas

def puzzle1():
    rows, cols, antennas = clean_data()
    antidotes = set()
    for _, locations in antennas.items():
        for i in range(len(locations)):
            loc1 = locations[i]
            for j in range(i+1, len(locations)):
                loc2 = locations[j]
                dx = loc2[0] - loc1[0]
                dy = loc2[1] - loc1[1]
                anti1 = (loc1[0] - dx, loc1[1] - dy)
                anti2 = (loc2[0] + dx, loc2[1] + dy)
                if 0 <= anti1[0] < rows and 0 <= anti1[1] < cols:
                    antidotes.add(anti1)
                if 0 <= anti2[0] < rows and 0 <= anti2[1] < cols:
                    antidotes.add(anti2)
    return len(antidotes)

def puzzle2():
    rows, cols, antennas = clean_data()
    antidotes = set()
    for _, locations in antennas.items():
        for i in range(len(locations)):
            loc1 = locations[i]
            for j in range(i+1, len(locations)):
                loc2 = locations[j]
                local_antidotes = []
                dx = loc2[0] - loc1[0]
                dy = loc2[1] - loc1[1]
                ax, ay = loc1[0], loc1[1]
                while 0 <= ax < rows and 0 <= ay < cols:
                    local_antidotes.append((ax, ay))
                    ax -= dx
                    ay -= dy
                ax, ay = loc2[0], loc2[1]
                while 0 <= ax < rows and 0 <= ay < cols:
                    local_antidotes.append((ax, ay))
                    ax += dx
                    ay += dy
                for antidote in local_antidotes:
                    antidotes.add(antidote)
    return len(antidotes)

print(puzzle1())
print(puzzle2())