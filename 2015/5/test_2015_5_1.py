import pathlib
import string


def is_nice(input: str) -> bool:

    bad_pairs: list[str] = ["ab", "cd", "pq", "xy"]
    if not any(bad_pair in input for bad_pair in bad_pairs):
        good_pairs: list[str] = [f"{x}{x}" for x in string.ascii_lowercase]
        if any(good_pair in input for good_pair in good_pairs):
            if sum(input.count(vowel) for vowel in 'aeiou') > 2:
                return True
    return False


def part_one(input_path: str) -> int:

    with open(input_path, "r", encoding="utf-8") as f:
        input: str = f.read()

    answer: int = 0
    for line in input.splitlines():
        if is_nice(line.lower()):
            answer += 1

    return answer


def test_part_one():
    input_path: str = pathlib.Path(__file__).parent.resolve()
    assert part_one(input_path.joinpath("input.txt")) == 236
