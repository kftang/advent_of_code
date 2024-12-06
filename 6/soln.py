import sys
import json
from collections import defaultdict
from pathlib import Path

def is_valid_update(update: list[int], adj_matrix: dict[int, list[int]]):
    for i, page in enumerate(update):
        if not all([next_page in adj_matrix[page] for next_page in update[i + 1:]]):
            return False, i
    return True, -1

def transform(pos1, pos2) -> tuple[int, int]:
    return (pos1[0] + pos2[0], pos1[1] + pos2[1])

def next_dir(direction) -> tuple[int, int]:
    if direction == (-1, 0):
        return (0, 1)
    elif direction == (0, 1):
        return (1, 0)
    elif direction == (1, 0):
        return (0, -1)
    elif direction == (0, -1):
        return (-1, 0)

    raise RuntimeError()

def part1(map: list[list[str]], start: tuple[int, int]):
    visited = set()
    pos = start
    dir = (-1, 0)
    while True:
        visited.add(pos)
        row, col = transform(pos, dir)
        if row >= len(map) - 1 or row < 0 or col >= len(map[row]) - 1 or col < 0:
            print(len(visited))
            return
        elif map[row][col] != '#':
            pos = (row, col)
            continue
        else:
            dir = next_dir(dir)

def has_block(map, start):
    visited_and_dir = set()
    pos = start
    dir = (-1, 0)
    while True:
        if (pos, dir) in visited_and_dir:
            return True
        visited_and_dir.add((pos, dir))
        row, col = transform(pos, dir)
        if row >= len(map) or row < 0 or col >= len(map[row]) or col < 0:
            return False
        elif map[row][col] != '#':
            pos = (row, col)
            continue
        else:
            dir = next_dir(dir)

def part2(map: list[list[str]], start: tuple[int, int]):
    blocks = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] != '#' and map[i][j] != '^':
                temp_map = json.loads(json.dumps(map))
                temp_map[i][j] = '#'
                if has_block(temp_map, start):
                    print((i, j))
                    blocks += 1
    print(blocks)

if __name__ == '__main__':
    input_file = Path(sys.argv[1])
    map = [list(row) for row in input_file.read_text().splitlines()]
    start = (0, 0)
    for i, row in enumerate(map):
        for j, space in enumerate(row):
            if space == '^':
                start = (i, j)
    part1(map, start)
    part2(map, start)



