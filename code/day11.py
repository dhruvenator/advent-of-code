import sys
from os.path import abspath, join, dirname
from functools import cache
sys.path.append(abspath(join(dirname(__file__), '..')))
from data.fetch import read_file_to_list

class PlutonianPebbles:
    def __init__(self):
        self.clean_data()

    def clean_data(self):
        data = read_file_to_list('/Users/dhruvix/Documents/Personal/aoc/data/day11.txt')
        data = data[0].split(' ')
        self.stones = list(map(int, data))
    
    def transform_stone(self, stone):
        if stone == 0:
            return [1]
        elif len(str(stone)) %2 == 0:
            stone = str(stone)
            return [int(stone[:len(stone)//2]), int(stone[len(stone)//2:])]
        else:
            return [stone * 2024]
    
    def blink(self):
        new_stones = []
        for s in self.stones:
            new_stones += self.transform_stone(s)
        self.stones = new_stones

    @cache
    def recursive_blink(self, stone, steps_left):
        if steps_left == 0:
            return 1
        if stone == 0:
            return self.recursive_blink(1, steps_left - 1)
        if len(str(stone)) %2 == 0:
            n1 = int(str(stone)[:len(str(stone))//2])
            n2 = int(str(stone)[len(str(stone))//2:])
            return self.recursive_blink(n1, steps_left - 1) + self.recursive_blink(n2, steps_left - 1)
        return self.recursive_blink(stone * 2024, steps_left - 1)

    def puzzle1(self):
        for _ in range(25):
            self.blink()
        return len(self.stones)

    def puzzle2(self):
        self.clean_data()
        return sum([self.recursive_blink(s, 75) for s in self.stones])

pp = PlutonianPebbles()
print(pp.puzzle1())
print(pp.puzzle2())