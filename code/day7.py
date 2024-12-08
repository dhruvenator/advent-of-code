import sys
from os.path import abspath, join, dirname
sys.path.append(abspath(join(dirname(__file__), '..')))
from data.fetch import read_file_to_list

def clean_data():
    data = read_file_to_list('/Users/dhruvix/Documents/Personal/aoc/data/day7.txt')
    data = [l.split(':') for l in data]
    data = [[int(r[0]), [int(i) for i in r[1].split()]] for r in data]
    return data

def generate_calibration_results(curr_results, not_seen, puzzle):
    if not_seen == []:
        return curr_results
    next_num = not_seen.pop(0)
    if puzzle == 1:
        curr_results = [n + next_num for n in curr_results] + [n * next_num for n in curr_results]
    elif puzzle == 2:
        curr_results = [n + next_num for n in curr_results] + [n * next_num for n in curr_results] + [int(str(n) + str(next_num)) for n in curr_results]
    return generate_calibration_results(curr_results, not_seen, puzzle)

def check_calibration(test, nums, puzzle):
    results = generate_calibration_results([nums[0]], nums[1:], puzzle)
    return test in results

def puzzle1():
    equations = clean_data()
    calibration = 0
    for [test, nums] in equations:
        if check_calibration(test, nums, 1):
            calibration += test
    return calibration

def puzzle2():
    equations = clean_data()
    calibration = 0
    for [test, nums] in equations:
        if check_calibration(test, nums, 2):
            calibration += test
    return calibration

print(puzzle1())
print(puzzle2())