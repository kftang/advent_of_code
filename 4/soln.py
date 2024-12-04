import sys
from pathlib import Path

def part1(rows: list[str]):
    find_word = 'XMAS'
    find_word_len = len(find_word)
    matches = 0
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            # up (-rows)
            if i >= find_word_len - 1:
                if all([find_word[k] == rows[i - k][j] for k in range(find_word_len)]):
                    matches += 1
            # right (+cols)
            if j <= len(rows[i]) - find_word_len:
                if all([find_word[k] == rows[i][j + k] for k in range(find_word_len)]):
                    matches += 1
            # down (+rows)
            if i <= len(rows) - find_word_len:
                if all([find_word[k] == rows[i + k][j] for k in range(find_word_len)]):
                    matches += 1
            # left (-cols)
            if j >= find_word_len - 1:
                if all([find_word[k] == rows[i][j - k] for k in range(find_word_len)]):
                    matches += 1
            # up left (-rows, -cols)
            if i >= find_word_len - 1 and j >= find_word_len - 1:
                if all([find_word[k] == rows[i - k][j - k] for k in range(find_word_len)]):
                    matches += 1
            # down left (+rows, -cols)
            if i <= len(rows) - find_word_len and j >= find_word_len - 1:
                if all([find_word[k] == rows[i + k][j - k] for k in range(find_word_len)]):
                    matches += 1
            # down right (+rows, +cols)
            if i <= len(rows) - find_word_len and j <= len(rows[i]) - find_word_len:
                if all([find_word[k] == rows[i + k][j + k] for k in range(find_word_len)]):
                    matches += 1
            # up right (-rows, +cols)
            if i >= find_word_len - 1 and j <= len(rows[i]) - find_word_len:
                if all([find_word[k] == rows[i - k][j + k] for k in range(find_word_len)]):
                    matches += 1
    print(matches)

def part2(rows: list[str]):
    matches = 0
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if i > 0 and j > 0 and i < len(rows) - 1 and j < len(rows[i]) - 1 and rows[i][j] == 'A':
                if rows[i - 1][j - 1] == 'M' and rows[i - 1][j + 1] == 'M':
                    if rows[i + 1][j + 1] == 'S' and rows[i + 1][j - 1] == 'S':
                        matches += 1
                if rows[i - 1][j - 1] == 'M' and rows[i - 1][j + 1] == 'S':
                    if rows[i + 1][j + 1] == 'S' and rows[i + 1][j - 1] == 'M':
                        matches += 1
                if rows[i - 1][j - 1] == 'S' and rows[i - 1][j + 1] == 'S':
                    if rows[i + 1][j + 1] == 'M' and rows[i + 1][j - 1] == 'M':
                        matches += 1
                if rows[i - 1][j - 1] == 'S' and rows[i - 1][j + 1] == 'M':
                    if rows[i + 1][j + 1] == 'M' and rows[i + 1][j - 1] == 'S':
                        matches += 1
    print(matches)

if __name__ == '__main__':
    input_file = Path(sys.argv[1])
    rows = input_file.read_text().splitlines()
    part1(rows)
    part2(rows)


