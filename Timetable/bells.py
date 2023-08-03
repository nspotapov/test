import datetime
from typing import List

from .bell import Bell


class Bells:
    bells: List[Bell]

    def __iter__(self):
        for bell in self.bells:
            yield bell
