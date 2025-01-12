import sys
from os.path import abspath, join, dirname
from itertools import combinations
sys.path.append(abspath(join(dirname(__file__), '..')))
from data.fetch import read_file_to_list

def clean_data():
    data = read_file_to_list('/Users/dhruvix/Documents/Personal/aoc/data/day23.txt')
    return [d.split('-') for d in data]

def puzzle1():
    edges = clean_data()
    adj_mat = {}
    all_trios = set()
    for [e1, e2] in edges:
        adj_mat[e1] = adj_mat.get(e1, [e1]) + [e2]
        adj_mat[e2] = adj_mat.get(e2, [e2]) + [e1]
    for e1 in adj_mat.keys():
        for e2 in adj_mat.keys():
            if e1 == e2: continue
            common = set(adj_mat[e1]).intersection(set(adj_mat[e2]))
            if e1 not in common or e2 not in common:
                continue
            common = common - {e1, e2}
            for c in common:
                trio = set([e1, e2, c])
                if [t for t in trio if t.startswith('t')]:
                    all_trios.add(tuple(sorted(list(trio))))
    return len(all_trios)

def puzzle2():
    edges = clean_data()
    adj_mat = {}
    for [e1, e2] in edges:
        adj_mat[e1] = adj_mat.get(e1, []) + [e2]
        adj_mat[e2] = adj_mat.get(e2, []) + [e1]
    fc_components = set()
    def fully_connected(node, matched):
        so_far = tuple(sorted(list(matched)))
        if so_far in fc_components: return
        else: fc_components.add(so_far)
        neighbours = set(adj_mat[node])
        for neighbour in neighbours:
            if neighbour in matched: continue
            if not (matched <= set(adj_mat[neighbour])): continue
            fully_connected(neighbour, {*matched, neighbour})
    for node in adj_mat.keys():
        fully_connected(node, {node})
    return ','.join(sorted(fc_components, key=len, reverse=True)[0])

print(puzzle1())
print(puzzle2())