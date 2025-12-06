import pathlib


def is_invalid(number: int) -> bool:
    number: str = str(number)
    return number[:len(number) // 2] == number[len(number) // 2:]


def part_one(input_path: str) -> int:

    with open(input_path, "r", encoding="utf-8") as f:
        input: str = f.read()

    total: int = 0
    num_ranges: list[tuple[int, int]] = [
        (int(start), int(end))
        for r in input.split(',')
        for start, end in [r.split('-')]
    ]

    for num_range in num_ranges:
        for number in range(*num_range):
            if is_invalid(number):
                total += number

    return total


def test_part_one():
    input_path: str = pathlib.Path(__file__).parent.resolve()
    assert part_one(input_path.joinpath("input.txt")) == 24747430309
