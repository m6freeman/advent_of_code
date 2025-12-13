from hashlib import md5
import pathlib


def part_one(input_path: str) -> int:

    with open(input_path, "r", encoding="utf-8") as f:
        input: str = f.read().strip('\n')

    i: int = 0
    while True:
        x = md5((input + str(i)).encode()).hexdigest()
        if str(x).startswith("00000"):
            return i
        i += 1


def test_part_one():
    input_path: str = pathlib.Path(__file__).parent.resolve()
    assert part_one(input_path.joinpath("input.txt")) == 346386
