import sys
from collections import defaultdict
from pathlib import Path

def part1(left_ids: list[int], right_ids: list[int]):
    distance = 0
    for left_id, right_id in zip(sorted(left_ids), sorted(right_ids)):
        distance += abs(left_id - right_id)

    print(distance)

def part2(left_ids: list[int], right_ids: list[int]):
    similarity = 0
    counts: dict[int, int] = defaultdict(lambda: 0)
    for right_id in right_ids:
        counts[right_id] += 1
    for left_id in left_ids:
        similarity += left_id * counts[left_id]
    print(similarity)

if __name__ == '__main__':
    left_ids: list[int] = []
    right_ids: list[int] = []
    input_file = Path(sys.argv[1])
    for line in input_file.read_text().splitlines():
        left, right = line.split()
        left_ids.append(int(left))
        right_ids.append(int(right))

    part1(left_ids, right_ids)
    part2(left_ids, right_ids)

