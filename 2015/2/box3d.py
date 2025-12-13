from math import prod


class Box3d():

    height: int
    length: int
    width: int

    def __init__(self, height: int, length: int, width: int):

        self.height = height if height > 0 else exit(1)
        self.length = length if length > 0 else exit(1)
        self.width = width if width > 0 else exit(1)

    def get_wrapping_paper(self) -> int:
        return self._get_surface_area() + self._get_smallest_side_area()

    def get_ribbon_length(self) -> int:
        return self._get_volume() + self._get_smallest_perimeter()

    def _get_volume(self) -> int:
        return self.height * self.length * self.width

    def _get_smallest_side_area(self) -> int:
        return prod(sorted([self.height, self.length, self.width])[:2])

    def _get_smallest_perimeter(self) -> int:
        return sum(sorted([self.height, self.length, self.width])[:2]) * 2

    def _get_surface_area(self) -> int:
        return (2 * self.height * self.length) \
            + (2 * self.length * self.width) \
            + (2 * self.width * self.height)
