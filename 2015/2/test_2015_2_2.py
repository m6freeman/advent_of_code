import pathlib
from box3d import Box3d


def part_two(input_path: str) -> int:

    with open(input_path, "r", encoding="utf-8") as f:
        input: str = f.read()
    boxes: list[Box3d] = []
    for dim in input.splitlines():
        boxes.append(Box3d(*map(int, dim.split('x'))))
    return sum(
        box.get_ribbon_length() for box in boxes)


def test_part_two():
    input_path: str = pathlib.Path(__file__).parent.resolve()
    assert part_two(input_path.joinpath("input.txt")) == 3812909
