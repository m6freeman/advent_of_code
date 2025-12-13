import pathlib


def part_two(input_path: str) -> int:

    with open(input_path, "r", encoding="utf-8") as f:
        input: str = f.read()

    houses_hit: set = set()
    positions: dict[str, tuple[int, int]] = {
        'santa': (0, 0),
        'robot': (0, 0)
    }
    direction_map: dict[str, tuple[int, int]] = {
        '^': (1, 0),
        '>': (0, 1),
        'v': (-1, 0),
        '<': (0, -1)
    }

    for i, direction in enumerate(input.strip('\n')):
        for position in positions.items():
            houses_hit.add(position[1])

        current = 'santa' if i % 2 == 0 else 'robot'

        if direction in direction_map:
            move = direction_map[direction]
            positions[current] = (
                positions[current][0] + move[0],
                positions[current][1] + move[1],
            )
        else:
            print(direction)
            exit(1)

    return len(houses_hit)


def test_part_two():
    input_path: str = pathlib.Path(__file__).parent.resolve()
    assert part_two(input_path.joinpath("input.txt")) == 2639
