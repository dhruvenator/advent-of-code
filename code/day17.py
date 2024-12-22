import sys
from os.path import abspath, join, dirname
sys.path.append(abspath(join(dirname(__file__), '..')))
from data.fetch import read_file_to_list

class ChronospatialComputer:
    def __init__(self):
        self.clean_data()
        self.output = []
        self.pointer = 0
        self.instruction = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv
        }

    def clean_data(self):
        data = read_file_to_list('/Users/dhruvix/Documents/Personal/aoc/data/day17.txt')
        self.A = int(data[0].split(' ')[-1])
        self.B = int(data[1].split(' ')[-1])
        self.C = int(data[2].split(' ')[-1])
        self.instructions = list(map(int, data[4].split(' ')[-1].split(',')))

    def get_operand(self, literal=False):
        val = self.instructions[self.pointer + 1]
        if literal or val <= 3:
            return val
        elif val == 4:
            return self.A
        elif val == 5:
            return self.B
        elif val == 6:
            return self.C
    
    def adv(self):
        op = self.get_operand()
        self.A = self.A >> op
        self.pointer += 2

    def bxl(self):
        op = self.get_operand(True)
        self.B = self.B ^ op
        self.pointer += 2

    def bst(self):
        op = self.get_operand()
        self.B = op % 8
        self.pointer += 2

    def jnz(self):
        if self.A == 0:
            self.pointer += 2
        else:
            self.pointer = self.get_operand(True)

    def bxc(self):
        self.B = self.B ^ self.C
        self.pointer += 2

    def out(self):
        op = self.get_operand()
        self.output.append(op % 8)
        self.pointer += 2

    def bdv(self):
        op = self.get_operand()
        self.B = self.A >> op
        self.pointer += 2

    def cdv(self):
        op = self.get_operand()
        self.C = self.A >> op
        self.pointer += 2
    
    # sorry this only works on my input.
    def rec_solve(self, program, a_val):
        if program == []: return a_val
        for b in range(8):
            a = a_val << 3 | b
            b = a % 8
            b = b ^ 3
            c = a >> b
            b = b ^ c
            b = b ^ 5
            if b % 8 == program[-1]:
                is_possible = self.rec_solve(program[:-1], a)
                if not is_possible: continue
                else:
                    return is_possible
        else:
            return False

    def puzzle1(self):
        while self.pointer < len(self.instructions):
            self.instruction[self.instructions[self.pointer]]()
        return ','.join(map(str, self.output))

    def puzzle2(self):
        return self.rec_solve(self.instructions[:], 0)


cc = ChronospatialComputer()
print(cc.puzzle1())
print(cc.puzzle2())