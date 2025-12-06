import pathlib


def part_two(input_path: str) -> int:

    with open(input_path, "r", encoding="utf-8") as f:
        instructions: str = f.read()

    level: int = 0

    for idx, instruction in enumerate(list(instructions)):
        match instruction:
            case '(': level += 1
            case ')': level -= 1
            case _: pass
        if level == -1:
            return idx + 1

    return idx


def test_part_two():
    input_path: str = pathlib.Path(__file__).parent.resolve()
    assert part_two(input_path.joinpath("input.txt")) == 1771
