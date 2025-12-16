import pathlib
import re


def is_nice(input: str) -> bool:
    x_any_x: str = r'.*([a-z])([a-z])\1.*'
    if re.search(x_any_x, input):
        x_x_any_x_x: str = r'.*([a-z][a-z]).*\1.*'
        if re.search(x_x_any_x_x, input):
            return True
    return False


def part_two(input_path: str) -> int:

    with open(input_path, "r", encoding="utf-8") as f:
        input: str = f.read()

    answer: int = 0
    for line in input.splitlines():
        if is_nice(line.lower()):
            answer += 1

    return answer


def test_part_two():
    input_path: str = pathlib.Path(__file__).parent.resolve()
    assert part_two(input_path.joinpath("input.txt")) == 51
