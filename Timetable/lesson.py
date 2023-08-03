import textwrap


class Lesson:
    group: str
    name: str
    room: str
    teacher: str

    def __str__(self):
        data = [x for x in [self.name, self.teacher, self.room] if x != ""]
        return ', '.join(data)
