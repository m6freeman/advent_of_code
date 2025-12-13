import pathlib
from box3d import Box3d


def part_one(input_path: str) -> int:

    with open(input_path, "r", encoding="utf-8") as f:
        input: str = f.read()
    boxes: list[Box3d] = []
    for dim in input.splitlines():
        boxes.append(Box3d(*map(int, dim.split('x'))))
    return sum(
        box.get_wrapping_paper() for box in boxes)


def test_part_one():
    input_path: str = pathlib.Path(__file__).parent.resolve()
    assert part_one(input_path.joinpath("input.txt")) == 1598415
