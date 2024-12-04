from itertools import combinations
import sys
from collections import defaultdict
from pathlib import Path

def is_safe(report: list[int]) -> bool:
    min_diff = 1
    max_diff = 3
    if report[0] > report[1]:
        # decreasing
        if not all([report[i] > report[i + 1] for i in range(len(report) - 1)]):
           return False 
    else:
        # increasing
        if not all([report[i] < report[i + 1] for i in range(len(report) - 1)]):
            return False

    # check min/max difference
    if not all([abs(report[i] - report[i + 1]) >= min_diff and abs(report[i] - report[i + 1]) <= max_diff for i in range(len(report) - 1)]):
        return False
    return True

def part1(reports: list[list[int]]):
    num_safe = sum([1 for report in reports if is_safe(report)])
    print(num_safe)

def part2(reports: list[list[int]]):
    num_safe = 0
    for report in reports:
        if is_safe(report):
            num_safe += 1
            continue
        for report_minus_one in combinations(report, len(report) - 1):
            if is_safe(list(report_minus_one)):
                num_safe += 1
                break
    print(num_safe)

if __name__ == '__main__':
    input_file = Path(sys.argv[1])
    reports = [[int(level) for level in levels] for levels in [report.split() for report in input_file.read_text().splitlines()]]
    part1(reports)
    part2(reports)


