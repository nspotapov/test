import datetime
from typing import List

from .pair import Pair


class Day:
    number: int
    date: datetime.date = None
    weekday: str
    pairs: List[Pair]

    def get_date(self):
        if self.date is None:
            return
        return self.date.strftime('%d.%m')
