from typing import Optional
from .schedule import DaypartingSchedule

class Brand:
    def __init__(self, id: int, name: str, daily_budget: float, monthly_budget: float):
        self.id = id
        self.name = name
        self.daily_budget = daily_budget
        self.monthly_budget = monthly_budget
        self.current_daily_spend = 0.0
        self.current_monthly_spend = 0.0

    def reset_daily_spend(self):
        self.current_daily_spend = 0.0

    def reset_monthly_spend(self):
        self.current_daily_spend = 0.0
        self.current_monthly_spend = 0.0

    def update_spend(self, amount: float):
        self.current_daily_spend += amount
        self.current_monthly_spend += amount

    def is_daily_budget_exceeded(self) -> bool:
        return self.current_daily_spend >= self.daily_budget

    def is_monthly_budget_exceeded(self) -> bool:
        return self.current_monthly_spend >= self.monthly_budget

class Campaign:
    def __init__(self, id: int, brand_id: int, name: str,
                 dayparting_schedule: Optional[DaypartingSchedule] = None):
        self.id = id
        self.brand_id = brand_id
        self.name = name
        self.is_active = True
        self.dayparting_schedule = dayparting_schedule

    def should_run(self) -> bool:
        if not self.is_active:
            return False
        if not self.dayparting_schedule:
            return True
        return self.dayparting_schedule.is_active_now()
