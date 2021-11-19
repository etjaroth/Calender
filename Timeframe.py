import StaticType
import datetime

class Timeframe():
    # __init__(self, datetime.datetime, datetime.datetime) -> void
    def __init__(self, start, end):
        self.start = StaticType.forceType(start, datetime.datetime)
        self.end = StaticType.forceType(end, datetime.datetime)

    def inRange(self, time):
        StaticType.forceType(time, datetime.datetime)
        b = (self.start <= time <= self.end)
        return StaticType.forceType(b, bool)

    def getStart(self):
        return StaticType.forceType(self.start, datetime.datetime)

    # getEnd(self, datetime.datetime) -> bool
    def getEnd(self):
        return StaticType.forceType(self.end, datetime.datetime)
