import sys
from os.path import abspath, join, dirname
sys.path.append(abspath(join(dirname(__file__), '..')))
from data.fetch import read_file_to_list

def clean_data():
    data = read_file_to_list('/Users/dhruvix/Documents/Personal/aoc/data/day1.txt')
    list1 = [int(i.split()[0]) for i in data]
    list2 = [int(i.split()[1]) for i in data]
    return list1, list2

def puzzle1():
    list1, list2 = clean_data()
    list1 = sorted(list1)
    list2 = sorted(list2)
    dist = 0
    for i, j in zip(list1, list2):
        dist += abs(i - j)
    return dist

def puzzle2():
    list1, list2 = clean_data()
    counter = {}
    for n in list2:
        counter[n] = counter.get(n, 0) + 1
    similarity = 0
    for n in list1:
        similarity += n*counter.get(n, 0)
    return similarity

print(puzzle1())
print(puzzle2())