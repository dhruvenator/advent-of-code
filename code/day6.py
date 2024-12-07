import sys
from os.path import abspath, join, dirname
from itertools import product
sys.path.append(abspath(join(dirname(__file__), '..')))
from data.fetch import read_file_to_list

def clean_data():
    data = read_file_to_list('/Users/dhruvix/Documents/Personal/aoc/data/day6.txt')
    grid = [list(r) for r in data]
    rows = len(grid)
    cols = len(grid[0])
    guard = (-1, -1)
    for r, c in product(range(rows), range(cols)):
        if grid[r][c] == '^':
            guard = (r, c)
            grid[r][c] = '.'
            break
    return grid, rows, cols, guard

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def puzzle1(data=None):
    if not data:
        grid, rows, cols, guard = clean_data()
    else:
        grid, rows, cols, guard = data
    dir = 0
    states = set([(guard[0], guard[1], dir)])
    visited = set([guard])
    loop = False
    while True:
        new_x = guard[0] + dirs[dir][0]
        new_y = guard[1] + dirs[dir][1]
        if new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols:
            break
        elif grid[new_x][new_y] == '.':
            guard = (new_x, new_y)
            if (guard[0], guard[1], dir) in states:
                loop = True
                break
            states.add((guard[0], guard[1], dir))
            visited.add(guard)
        elif grid[new_x][new_y] == '#':
            dir = (dir + 1) % 4
    if data:
        return list(visited), loop
    return len(visited)

def puzzle2():
    num_obstructions = 0
    grid, rows, cols, guard = clean_data()
    guard_path, _ = puzzle1((grid, rows, cols, guard))
    for i, j in guard_path:
        grid[i][j] = '#'
        guard_path, is_loop = puzzle1((grid, rows, cols, guard))
        if is_loop:
            num_obstructions += 1
        grid[i][j] = '.'
    return num_obstructions

print(puzzle1())
print(puzzle2())