import sys
from os.path import abspath, join, dirname
sys.path.append(abspath(join(dirname(__file__), '..')))
from data.fetch import read_file_to_list

class WarehouseWoes:
    def __init__(self):
        self.clean_data()
        self.dirs = {
            '>': [0, 1],
            'v': [1, 0],
            '<': [0, -1],
            '^': [-1, 0]
        }

    def clean_data(self):
        data = read_file_to_list('/Users/dhruvix/Documents/Personal/aoc/data/day15.txt')
        split_pos = data.index('')
        self.grid = [list(x) for x in data[:split_pos]]
        self.moves = ''.join(data[split_pos + 1:])
        self.find_robot_pos()
    
    def find_robot_pos(self):
        self.robot = None
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == '@':
                    self.robot = (i, j)
                    break
            if self.robot: break

    def double_grid(self):
        new_grid = []
        def double(title):
            if title == '#': return '##'
            elif title == 'O': return '[]'
            elif title == '.': return '..'
            elif title == '@': return '@.'
        for g_row in self.grid:
            new_row = [double(r) for r in g_row]
            new_grid.append(list(''.join(new_row)))
        self.grid = new_grid
        self.find_robot_pos()
    
    def print_grid(self, move):
        print(move * 25)
        for g in self.grid:
            print(''.join(g))
    
    def move_robot_1(self, dx, dy):
        rx, ry = self.robot
        if self.grid[rx + dx][ry + dy] == '#':
            return
        if self.grid[rx + dx][ry + dy] == '.':
            self.grid[rx][ry] = '.'
        elif self.grid[rx + dx][ry + dy] == 'O':
            x, y = rx + dx, ry + dy
            while self.grid[x][y] == 'O':
                x += dx
                y += dy
            if self.grid[x][y] == '#':
                return
            self.grid[x][y] = 'O'
            self.grid[rx][ry] = '.'
        self.grid[rx + dx][ry + dy] = '@'
        self.robot = (rx + dx, ry + dy)
    
    def move_boxes(self, dx, box_locations):
        if dx < 0:
            box_locations = sorted(box_locations)
        else:
            box_locations = sorted(box_locations, reverse=True)
        for bx, by in box_locations:
            self.grid[bx + dx][by] = self.grid[bx][by]
            self.grid[bx][by] = '.'

    def can_move_boxes(self, dx):
        rx, ry = self.robot
        visited = {(rx + dx, ry)}
        q = [(rx + dx, ry)]
        while q:
            ex, ey = q.pop(0)
            if self.grid[ex][ey] == '[' and (ex, ey + 1) not in visited:
                q.append((ex, ey + 1))
                visited.add((ex, ey + 1))
            elif self.grid[ex][ey] == ']' and (ex, ey - 1) not in visited:
                q.append((ex, ey - 1))
                visited.add((ex, ey - 1))
            if self.grid[ex + dx][ey] == '#':
                return False, None
            elif self.grid[ex + dx][ey] in ['[', ']']:
                q.append((ex + dx, ey))
                visited.add((ex + dx, ey))
        return True, visited
    
    def move_robot_2(self, dx, dy):
        rx, ry = self.robot
        if self.grid[rx + dx][ry + dy] == '#':
            return
        if self.grid[rx + dx][ry + dy] == '.':
            self.grid[rx][ry] = '.'
        elif dx == 0:
            x, y = rx + dx, ry + dy
            while self.grid[x][y] in ['[', ']']:
                x += dx
                y += dy
            if self.grid[x][y] == '#':
                return
            new_row = list(self.grid[x])
            new_row.pop(y)
            new_row.insert(ry, '.')
            self.grid[x] = list(new_row)
        else:
            can_move, object_locations = self.can_move_boxes(dx)
            if can_move:
                self.move_boxes(dx, list(object_locations))
                self.grid[rx][ry] = '.'
            else:
                return
        self.grid[rx + dx][ry + dy] = '@'
        self.robot = (rx + dx, ry + dy)

    def puzzle1(self):
        # self.print_grid('-')
        GPS_sum = 0
        for move in self.moves:
            dir = self.dirs[move]
            self.move_robot_1(dir[0], dir[1])
            # self.print_grid(move)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 'O':
                    GPS_sum += (100 * i + j)
        return GPS_sum

    def puzzle2(self):
        self.clean_data()
        self.double_grid()
        # self.print_grid('=')
        GPS_sum = 0
        for move in self.moves:
            dir = self.dirs[move]
            self.move_robot_2(dir[0], dir[1])
            # self.print_grid(move)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == '[':
                    GPS_sum += (100 * i + j)
        return GPS_sum

ww = WarehouseWoes()
print(ww.puzzle1())
print(ww.puzzle2())