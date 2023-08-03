import datetime


class Bell:
    def __init__(self, time_begin: datetime.time, time_end: datetime.time, number: int = None):
        self.number: int = number
        self.begin: datetime.time = time_begin
        self.end:datetime.time = time_end

    def get_str(self) -> str:
        return self.begin.strftime('%H:%M') + '-' + self.end.strftime('%H:%M')
