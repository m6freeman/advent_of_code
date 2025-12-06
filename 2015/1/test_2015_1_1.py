import pathlib


def part_one(input_path: str) -> int:

    with open(input_path, "r", encoding="utf-8") as f:
        instructions: str = f.read()

    level: int = 0

    for instruction in list(instructions):
        match instruction:
            case '(': level += 1
            case ')': level -= 1
            case _: pass

    return level


def test_part_one():
    input_path: str = pathlib.Path(__file__).parent.resolve()
    assert part_one(input_path.joinpath("input.txt")) == 138
