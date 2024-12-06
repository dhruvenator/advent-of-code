import sys
from os.path import abspath, join, dirname
from functools import cmp_to_key
sys.path.append(abspath(join(dirname(__file__), '..')))
from data.fetch import read_file_to_list

class PrintQueue:
    def __init__(self):
        self.clean_data()
        self.incorrect_updates = []
        self.rule_dic = {}
        for x, y in self.rules:
            self.rule_dic[y] = [x] if y not in self.rule_dic else self.rule_dic[y] + [x]
    
    def clean_data(self):
        data = read_file_to_list('/Users/dhruvix/Documents/Personal/aoc/data/day5.txt')
        sep = data.index('')
        rules = data[:sep]
        updates = data[sep+1:]
        self.rules = [r.split('|') for r in rules]
        self.updates = [u.split(',') for u in updates]
    
    def rule_comparison(self, a, b):
        if b in self.rule_dic.get(a, []): 
            return 1
        elif a in self.rule_dic.get(b, []): 
            return -1
        else: 
            return 0

    def puzzle1(self):
        mid_sum = 0
        for update in self.updates:
            visited = set()
            for u in update:
                if u not in self.rule_dic or u in self.rule_dic and set(self.rule_dic[u]).intersection(set(update)).issubset(visited):
                    visited.add(u)
                else:
                    break
            if len(visited) == len(update):
                mid_sum += int(update[len(update)//2])
            else:
                self.incorrect_updates.append(update)
        return mid_sum

    def puzzle2(self):
        mid_sum = 0
        for update in self.incorrect_updates:
            sorted_update = sorted(update, key=cmp_to_key(self.rule_comparison))
            mid_sum += int(sorted_update[len(update)//2])
        return mid_sum

pq = PrintQueue()
print(pq.puzzle1())
print(pq.puzzle2())