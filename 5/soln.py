import sys
from collections import defaultdict
from pathlib import Path

def is_valid_update(update: list[int], adj_matrix: dict[int, list[int]]):
    for i, page in enumerate(update):
        if not all([next_page in adj_matrix[page] for next_page in update[i + 1:]]):
            return False, i
    return True, -1

def part1(rules: tuple[str, str], updates: list[list[int]]):
    adj_matrix = defaultdict(lambda: list())
    for last, cur in rules:
        adj_matrix[last].append(cur)

    middle_sums = 0
    for update in updates:
        if is_valid_update(update, adj_matrix)[0]:
            middle_sums += update[len(update) // 2]
    print(middle_sums)


def part2(rules: tuple[str, str], updates: list[list[int]]):
    adj_matrix = defaultdict(lambda: list())
    for last, cur in rules:
        adj_matrix[last].append(cur)

    middle_sums = 0
    for update in updates:
        valid, idx = is_valid_update(update, adj_matrix)
        if valid:
            continue
        temp = []
        while len(temp) != len(update):
            rem_update = list(set(update) - set(temp))
            for i, page in enumerate(rem_update):
                rest = rem_update[i + 1:]
                if not all([remaining_page in adj_matrix[page] for remaining_page in rest]):
                    continue
                temp.append(page)
                break
        middle_sums += temp[len(temp) // 2]

    print(middle_sums)

if __name__ == '__main__':
    input_file = Path(sys.argv[1])
    rules, updates = input_file.read_text().split('\n\n')
    rules = [tuple(map(int, rule.split('|'))) for rule in rules.splitlines()]
    updates = [[int(page) for page in update.split(',')] for update in updates.splitlines()]
    part1(rules, updates)
    part2(rules, updates)



