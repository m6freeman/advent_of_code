import pathlib


def part_one(input_path: str) -> int:

    with open(input_path, "r", encoding="utf-8") as f:
        instructions: list[str] = f.read().split("\n")

    zero_counter = 0
    current_pos: int = 50
    for instruction in instructions:
        if instruction == "":
            break
        direction: str = instruction[0]
        amount = int(instruction[1:])
        match direction:
            case 'R':
                current_pos = (current_pos + amount) % 100
            case 'L':
                current_pos = (current_pos - amount) % 100
            case _:
                pass
        if current_pos == 0:
            zero_counter += 1

    return zero_counter


def test_part_one():
    input_path: str = pathlib.Path(__file__).parent.resolve()
    assert part_one(input_path.joinpath("input.txt")) == 1040
