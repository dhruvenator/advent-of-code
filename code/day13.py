import sys
from os.path import abspath, join, dirname
import re
sys.path.append(abspath(join(dirname(__file__), '..')))
from data.fetch import read_file_to_list

def clean_data():
    data = read_file_to_list('/Users/dhruvix/Documents/Personal/aoc/data/day13.txt')
    button_pattern = r'Button (\w): X\+(\d+), Y\+(\d+)'
    prize_pattern = r'Prize: X=(\d+), Y=(\d+)'
    combos = []
    combo_dic = {}
    for i in range(len(data)):
        if i % 4 == 0 or i % 4 == 1:
            match = re.search(button_pattern, data[i])
            combo_dic[match.group(1)] = [int(match.group(2)), int(match.group(3))]
        if i % 4 == 2:
            match = re.search(prize_pattern, data[i])
            combo_dic['Prize'] = [int(match.group(1)), int(match.group(2))]
            combos.append(combo_dic.copy())
    return combos

def solve_combination(combo):
    [ax, ay] = combo['A']
    [bx, by] = combo['B']
    [px, py] = combo['Prize']
    a = (px*by - py*bx) / (ax*by - ay*bx)
    b = (px - ax*a) / bx
    if a % 1 == 0 and b % 1 == 0:
        return int(a * 3 + b)
    return 0

def puzzle1():
    combos = clean_data()
    tokens = 0
    for combo in combos:
        tokens += solve_combination(combo)
    return tokens

def puzzle2():
    combos = clean_data()
    tokens = 0
    for combo in combos:
        combo['Prize'] = [i + 10000000000000 for i in combo['Prize']]
        tokens += solve_combination(combo)
    return tokens

print(puzzle1())
print(puzzle2())