import sys
from os.path import abspath, join, dirname
sys.path.append(abspath(join(dirname(__file__), '..')))
from data.fetch import read_file_to_list

def clean_data():
    data = read_file_to_list('/Users/dhruvix/Documents/Personal/aoc/data/day25.txt')
    locks = []
    keys = []
    height = data.index('') - 2
    width = len(data[0])
    data = ''.join([d if d else '|' for d in data]).split('|')
    for ele in data:
        lens = {}
        for i, e in enumerate(ele):
            lens[i % width] = lens.get(i % width, 0) + (e == '#')
        if ele[0] == '#':
            locks.append([lens[i] - 1 for i in range(width)])
        else:
            keys.append([lens[i] - 1 for i in range(width)])
    return locks, keys, height

def puzzle1():
    locks, keys, height = clean_data()
    fits = 0
    for lock in locks:
        for key in keys:
            for i in range(len(key)):
                if key[i] + lock[i] > height:
                    break
            else:
                fits += 1
    return fits

print(puzzle1())