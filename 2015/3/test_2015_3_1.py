import pathlib


def part_one(input_path: str) -> int:

    with open(input_path, "r", encoding="utf-8") as f:
        input: str = f.read()

    unique_houses: set = set()
    x: int = 0
    y: int = 0

    for direction in input.strip('\n'):
        unique_houses.add((x, y))
        match direction:
            case '^':
                x += 1
            case '>':
                y += 1
            case 'v':
                x -= 1
            case '<':
                y -= 1
            case _:
                print(direction)
                exit(1)

    return len(unique_houses)


def test_part_one():
    input_path: str = pathlib.Path(__file__).parent.resolve()
    assert part_one(input_path.joinpath("input.txt")) == 2565
