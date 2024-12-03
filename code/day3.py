import sys
from os.path import abspath, join, dirname
import re
sys.path.append(abspath(join(dirname(__file__), '..')))
from data.fetch import read_file_to_list

def clean_data():
    data = read_file_to_list('/Users/dhruvix/Documents/Personal/aoc/data/day3.txt')
    return ''.join(data)

def puzzle1(data=None):
    program = clean_data() if not data else data
    value = 0
    pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(pattern, program)
    for match in matches:
        match = match[4:-1]
        nums = match.split(',')
        value += int(nums[0]) * int(nums[1])
    return value


def puzzle2():
    program = clean_data()
    if not program.startswith("do()"): program = "do()" + program
    if not program.endswith("don't()"): program = program + "don't()"
    value = 0
    active_region = r"do\(\)(.*?)don't\(\)"
    active_zones = re.findall(active_region, program)
    for sub_program in active_zones:
        value += puzzle1(sub_program)
    return value

print(puzzle1())
print(puzzle2())