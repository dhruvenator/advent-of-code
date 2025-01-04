import sys
from os.path import abspath, join, dirname
sys.path.append(abspath(join(dirname(__file__), '..')))
from data.fetch import read_file_to_list

def clean_data():
    data = read_file_to_list('/Users/dhruvix/Documents/Personal/aoc/data/day22.txt')
    return list(map(int, data))

def next_secret_number(curr):
    a = curr * 64
    b = curr ^ a
    c = b % 16777216
    a = c // 32
    b = c ^ a
    c = b % 16777216
    a = c * 2048
    b = c ^ a
    return b % 16777216

def puzzle1(n):
    secret_sum = 0
    for buyer in clean_data():
        sn = buyer
        for _ in range(n):
            sn = next_secret_number(sn)
        secret_sum += sn
    return secret_sum

def puzzle2(n, seq_len):
    sequence_totals = {}
    for buyer in clean_data():
        sn = buyer
        buyer_prices = [sn % 10]
        for _ in range(n):
            sn = next_secret_number(sn)
            buyer_prices.append(sn % 10)
        visited_seq = set()
        for i in range(len(buyer_prices) - seq_len):
            seq = buyer_prices[i:i+seq_len+1]
            seq = tuple([seq[s+1] - seq[s] for s in range(len(seq) - 1)])
            if seq in visited_seq: continue
            visited_seq.add(seq)
            sequence_totals[seq] = sequence_totals.get(seq, 0) + buyer_prices[i + seq_len]
    return max(sequence_totals.values())

print(puzzle1(2000))
print(puzzle2(2000, 4))