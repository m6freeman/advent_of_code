import pathlib


def part_two(input_path: str) -> int:

    with open(input_path, "r", encoding="utf-8") as f:
        instructions: list[str] = f.read().split("\n")

    zero_counter = 0
    current_pos: int = 50
    for instruction in instructions:
        if instruction == "":
            break
        direction: str = instruction[0]
        amount = int(instruction[1:])
        zero_counter += amount // 100
        amount %= 100
        match direction:
            case 'R':
                zero_counter += 1 if (amount > (100 - current_pos)) else 0
                current_pos = (current_pos + amount) % 100
            case 'L':
                zero_counter += 1 if (current_pos !=
                                      0 and amount > current_pos) else 0
                current_pos = (current_pos - amount) % 100
            case _:
                pass
        if current_pos == 0:
            zero_counter += 1
        print(amount, current_pos, zero_counter)

    return zero_counter


def test_part_two():
    input_path: str = pathlib.Path(__file__).parent.resolve()
    assert part_two(input_path.joinpath("input.txt")) == 6027
