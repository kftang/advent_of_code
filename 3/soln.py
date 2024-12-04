from enum import Enum, auto
from itertools import combinations
import sys
from collections import defaultdict
from pathlib import Path

class State(Enum):
    INITIAL = auto()
    # for mul(<num1>,<num2>)
    M = auto()
    U = auto()
    L = auto()
    MUL_OPEN_PAREN = auto()
    NUM1 = auto()
    COMMA = auto()
    NUM2 = auto()
    # for do() and don't()
    D = auto()
    O = auto()
    DO_OPEN_PAREN = auto()
    N = auto()
    SINGLE_QUOTE = auto()
    T = auto()
    DONT_OPEN_PAREN = auto()


def part1(input_str: str):
    state = State.INITIAL
    products = []
    num1, num2 = None, None
    enabled = True
    for input_char in input_str:
        match state:
            case State.INITIAL:
                num1, num2 = None, None
                if input_char == 'm':
                    state = State.M
                if input_char == 'd':
                    state = State.D
            case State.M:
                if input_char == 'u':
                    state = State.U
                elif input_char == 'd':
                    state = State.D
                elif input_char != 'm':
                    state = State.INITIAL
            case State.U:
                if input_char == 'l':
                    state = State.L
                elif input_char == 'd':
                    state = State.D
                elif input_char == 'm':
                    state = State.M
                else:
                    state = State.INITIAL
            case State.L:
                if input_char == '(':
                    state = State.MUL_OPEN_PAREN
                elif input_char == 'd':
                    state = State.D
                elif input_char == 'm':
                    state = State.M
                else:
                    state = State.INITIAL
            case State.MUL_OPEN_PAREN:
                if input_char.isdigit():
                    state = State.NUM1
                    num1 = int(input_char)
                elif input_char == 'd':
                    state = State.D
                elif input_char == 'm':
                    state = State.M
                else:
                    state = State.INITIAL
            case State.NUM1:
                if input_char.isdigit():
                    num1 = num1 * 10 + int(input_char)
                elif input_char == ',' and num1 is not None:
                    state = State.COMMA
                elif input_char == 'd':
                    state = State.D
                elif input_char == 'm':
                    state = State.M
                else:
                    state = State.INITIAL
            case State.COMMA:
                if input_char.isdigit():
                    state = State.NUM2
                    num2 = int(input_char)
                elif input_char == 'd':
                    state = State.D
                elif input_char == 'm':
                    state = State.M
                else:
                    state = State.INITIAL
            case State.NUM2:
                if input_char.isdigit():
                    num2 = num2 * 10 + int(input_char)
                elif input_char == ')' and num2 is not None:
                    state = State.INITIAL
                    if enabled:
                        products.append(num1 * num2)
                elif input_char == 'd':
                    state = State.D
                elif input_char == 'm':
                    state = State.M
                else:
                    state = State.INITIAL
            case State.D:
                if input_char == 'o':
                    state = State.O
                elif input_char == 'm':
                    state = State.M
                elif input_char != 'd':
                    state = State.INITIAL
            case State.O:
                if input_char == '(':
                    state = State.DO_OPEN_PAREN
                elif input_char == 'n':
                    state = State.N
                elif input_char == 'd':
                    state = State.D
                elif input_char == 'm':
                    state = State.M
                else:
                    state = State.INITIAL
            case State.DO_OPEN_PAREN:
                if input_char == ')':
                    state = State.INITIAL
                    enabled = True
                elif input_char == 'd':
                    state = State.D
                elif input_char == 'm':
                    state = State.M
                else:
                    state = State.INITIAL
            case State.N:
                if input_char == '\'':
                    state = State.SINGLE_QUOTE
                elif input_char == 'd':
                    state = State.D
                elif input_char == 'm':
                    state = State.M
                else:
                    state = State.INITIAL
            case State.SINGLE_QUOTE:
                if input_char == 't':
                    state = State.T
                elif input_char == 'd':
                    state = State.D
                elif input_char == 'm':
                    state = State.M
                else:
                    state = State.INITIAL
            case State.T:
                if input_char == '(':
                    state = State.DONT_OPEN_PAREN
                elif input_char == 'd':
                    state = State.D
                elif input_char == 'm':
                    state = State.M
                else:
                    state = State.INITIAL
            case State.DONT_OPEN_PAREN:
                if input_char == ')':
                    state = State.INITIAL
                    enabled = False
                elif input_char == 'd':
                    state = State.D
                elif input_char == 'm':
                    state = State.M
                else:
                    state = State.INITIAL
    print(sum(products))


if __name__ == '__main__':
    input_file = Path(sys.argv[1])
    input_str = input_file.read_text()
    part1(input_str)


