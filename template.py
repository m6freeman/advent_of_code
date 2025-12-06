import pathlib


def part_one(input_path: str) -> int:

    with open(input_path, "r", encoding="utf-8") as f:
        input: str = f.read()

    print(input)
    return 0


def test_part_one():
    input_path: str = pathlib.Path(__file__).parent.resolve()
    assert part_one(input_path.joinpath("input.txt")) == 1


def part_two(input_path: str) -> int:

    with open(input_path, "r", encoding="utf-8") as f:
        input: str = f.read()

    print(input)
    return 0


def test_part_two():
    input_path: str = pathlib.Path(__file__).parent.resolve()
    assert part_two(input_path.joinpath("input.txt")) == 1
