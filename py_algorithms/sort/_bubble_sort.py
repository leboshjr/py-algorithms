from typing import List

from ..utils import compare_ints
from .sort import Sort


class BubbleSort(Sort):
    """
        Simple sorting algorithm

        Stability: yes
        N: len(XS)
        Time: O(N^2)
        Space: O(N)
    """

    def sort(self, xs: List[int]) -> List[int]:
        if not isinstance(xs, (list, tuple)):
            raise RuntimeError('Can sort only iterable entity.')

        done = False
        while not done:
            swapped = False
            for i in range(0, len(xs) - 1):
                # compare current item with next one,
                # if current bigger than next one - swap it, mark state flag
                if 1 == compare_ints(xs[i], xs[i + 1]):
                    xs[i], xs[i + 1] = xs[i + 1], xs[i]
                    swapped = True
            # all items are in order now
            if not swapped:
                done = True
        return xs
