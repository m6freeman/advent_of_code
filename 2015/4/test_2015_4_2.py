from hashlib import md5
from multiprocessing import Pool
import pathlib
import sys


def find_hash(seed: str) -> int | None:
    hash = md5(seed.encode()).hexdigest()
    if str(hash).startswith("000000"):
        return int(''.join(i for i in seed if i.isdigit()))
    return None


def part_two(input_path: str) -> int:

    with open(input_path, "r", encoding="utf-8") as f:
        input: str = f.read().strip('\n')

    with Pool() as pool:
        seeds: list[str] = [input + str(i) for i in range(10000000)]
        results = pool.map(find_hash, seeds)

    lowest: int = sys.maxsize
    for result in results:
        if result:
            lowest = min(lowest, result)

    return lowest


def test_part_two():
    input_path: str = pathlib.Path(__file__).parent.resolve()
    assert part_two(input_path.joinpath("input.txt")) == 9958218
