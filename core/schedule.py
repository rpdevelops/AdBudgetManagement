import datetime

class DaypartingSchedule:
    def __init__(self, start_hour: int, end_hour: int):
        if not (0 <= start_hour <= 23) or not (0 <= end_hour <= 23):
            raise ValueError("Hours must be between 0 and 23")
        self.start_hour = start_hour
        self.end_hour = end_hour

    def is_active_now(self) -> bool:
        now_hour = datetime.datetime.now().hour
        if self.start_hour <= self.end_hour:
            return self.start_hour <= now_hour <= self.end_hour
        return now_hour >= self.start_hour or now_hour <= self.end_hour
