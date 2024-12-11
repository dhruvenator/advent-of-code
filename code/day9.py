import sys
from os.path import abspath, join, dirname
sys.path.append(abspath(join(dirname(__file__), '..')))
from data.fetch import read_file_to_list

def clean_data():
    data = read_file_to_list('/Users/dhruvix/Documents/Personal/aoc/data/day9.txt')
    counter = 0
    disk = []
    space = False
    for i in range(len(data[0])):
        num = int(data[0][i])
        if space:
            for i in range(num): disk.append('.')
        else:
            for i in range(num): disk.append(str(counter))
            counter += 1
        space = not space
    return disk

def puzzle1():
    disk = clean_data()
    start = 0
    end = len(disk) - 1
    while start <= end:
        if disk[end] == '.':
            end -= 1
        elif disk[start] == '.':
            disk[start], disk[end] = disk[end], disk[start]
            start += 1
            end -= 1
        elif disk[start] != '.':
            start += 1
    checksum = 0
    for i in range(len(disk)):
        if disk[i] == '.':
            break
        checksum += i*int(disk[i])
    return checksum

def puzzle2():
    disk = clean_data()
    files = {}
    spaces = []
    start = 0
    i = 0
    ch = disk[0]
    element_len = 0
    while i < len(disk):
        if disk[i] != ch:
            if ch == '.':
                spaces.append({
                    'start': start,
                    'length': element_len
                })
            else:
                files[ch] = {
                    'start': start,
                    'length': element_len
                }
            ch = disk[i]
            element_len = 1
            start = i
            i += 1
        else:
            i += 1
            element_len += 1
    files[ch] = {
        'start': start,
        'length': element_len
    }
    for i in range(int(disk[-1]), -1, -1):
        file = files[str(i)]
        for space_id in range(len(spaces)):
            if spaces[space_id]['length'] < file['length'] or spaces[space_id]['start'] > file['start']:
                continue
            for j in range(file['length']):
                disk[spaces[space_id]['start'] + j] = str(i)
                disk[file['start'] + j] = '.'
            spaces[space_id]['length'] -= file['length']
            spaces[space_id]['start'] += file['length']
            break
    checksum = 0
    for i in range(len(disk)):
        if disk[i] != '.':
            checksum += i*int(disk[i])
    return checksum

print(puzzle1())
print(puzzle2())