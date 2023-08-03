import datetime
from typing import List

from .day import Day
from .bells import Bells


class Week:
    DAYS_NAME_RU: List[str] = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    DAYS_NAME_EN: List[str] = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

    begin: datetime.date = None
    end: datetime.date = None
    days: List[Day]
    group: str
    number: int
    timetable_bells: Bells

    def set_period(self, begin: datetime.date = None, end: datetime.date = None):
        self.begin = begin
        self.end = end
        if self.days:
            for i, day in enumerate(self.days):
                day: Day
                if self.begin:
                    day.date = self.begin + datetime.timedelta(days=i)
                day.weekday = self.DAYS_NAME_RU[i]

    def get_period(self):
        if not self.begin or not self.end:
            return
        return self.begin.strftime("%d.%m") + '-' + self.end.strftime("%d.%m")
