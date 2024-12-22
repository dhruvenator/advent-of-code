import sys
from os.path import abspath, join, dirname
from functools import cache
sys.path.append(abspath(join(dirname(__file__), '..')))
from data.fetch import read_file_to_list

class LinenLayout:
    def __init__(self):
        self.clean_data()

    def clean_data(self):
        data = read_file_to_list('/Users/dhruvix/Documents/Personal/aoc/data/day19.txt')
        self.patterns = data[0].split(', ')
        self.designs = data[2:]
    
    @cache
    def is_possible(self, design):
        if design == "":
            return True
        for pattern in self.patterns:
            if design.startswith(pattern) and self.is_possible(design[len(pattern):]):
                return True
        return False
    
    @cache
    def arrangements(self, design):
        if design == "":
            return 1
        num_ways = 0
        for pattern in self.patterns:
            if design.startswith(pattern):
                num_ways += self.arrangements(design[len(pattern):])
        return num_ways

    def puzzle1(self):
        possible_designs = 0
        for design in self.designs:
            possible_designs += self.is_possible(design)
        return possible_designs

    def puzzle2(self):
        pattern_arrangements = 0
        for design in self.designs:
            pattern_arrangements += self.arrangements(design)
        return pattern_arrangements

ll = LinenLayout()
print(ll.puzzle1())
print(ll.puzzle2())