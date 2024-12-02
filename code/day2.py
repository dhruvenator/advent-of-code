import sys
from os.path import abspath, join, dirname
sys.path.append(abspath(join(dirname(__file__), '..')))
from data.fetch import read_file_to_list

def clean_data():
    data = read_file_to_list('/Users/dhruvix/Documents/Personal/aoc/data/day2.txt')
    return [[int(i) for i in report.split()] for report in data]

def safe_increase(report):
    for i in range(1, len(report)):
        if report[i] - report[i-1] not in [1, 2, 3]:
            return False
    return True

def safe_decrease(report):
    for i in range(1, len(report)):
        if report[i-1] - report[i] not in [1, 2, 3]:
            return False
    return True

def puzzle1():
    data = clean_data()
    safe_reports = 0
    for report in data:
        safe_reports += safe_decrease(report) or safe_increase(report)
    return safe_reports

def puzzle2():
    data = clean_data()
    safe_reports = 0
    for report in data:
        if safe_decrease(report) or safe_increase(report):
            safe_reports += 1
            continue
        for i in range(len(report)):
            new_report = report[:i] + report[i+1:]
            if safe_decrease(new_report) or safe_increase(new_report):
                safe_reports += 1
                break
    return safe_reports

print(puzzle1())
print(puzzle2())