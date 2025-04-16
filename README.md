# Ad Agency Budget Management System

A Python-based simulation to manage advertising campaigns and enforce budget controls for multiple brands. Built with a clean, modular architecture, it supports real-time budget enforcement and time-based campaign activation.

## Features

- Track daily and monthly ad spend for each brand
- Automatically disable campaigns when budgets are exceeded
- Re-enable campaigns at the start of new days/months if budgets allow
- Support dayparting (run campaigns only during specific hours)
- Track and display campaign status in real-time
- End-to-end tested with Pytest

---

## Architecture Overview

**Project Structure:**
```
ad_system/
├── core/
│   ├── enums.py               # Enums (like TimeOfDay)
│   ├── models.py              # Brand and Campaign logic
│   ├── schedule.py            # Dayparting time logic
│   └── system.py              # Main AdSystem control flow
├── main.py                    # Entry-point with usage example
├── tests/                     # Pytest-based unit and integration tests
│   └── test_end_to_end.py
├── requirements.txt           # Dependencies
```

## How to Run and Test

1. Clone the repository:
```bash
git clone https://github.com/rpdevelops/AdBudgetManagement.git && cd AdBudgetManagement
```

2. Setup the environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Run the simulation:
```bash
python main.py
```

4. Run the tests:
```bash
PYTHONPATH=. pytest tests/ -v
```

## PseudoCode Overview
```
Data Structures:
- Brand: {id, name, daily_budget, monthly_budget, current_daily_spend, current_monthly_spend}
- Campaign: {id, brand_id, name, is_active, dayparting_schedule}
- DaypartingSchedule: {start_hour, end_hour}

Main Logic:
1. On spend update:
   - Check if the campaign can run
   - Update brand spend
   - Disable campaign if daily/monthly limit is exceeded

2. On each tick:
   - Re-evaluate all campaigns for time window and budgets

3. At day/month reset:
   - Reset daily/monthly spend
   - Re-enable campaigns if allowed
```

---

## Example Usage (main.py)

```python
from core.models import Brand, Campaign
from core.schedule import DaypartingSchedule
from core.system import AdSystem

# Setup
ad_system = AdSystem()
nike = Brand(1, "Nike", daily_budget=100.0, monthly_budget=3000.0)
ad_system.add_brand(nike)

schedule = DaypartingSchedule(8, 18)
ad_system.add_campaign(Campaign(1, nike.id, "Nike Campaign", schedule))
ad_system.update_campaign_spend(1, 120.0)
ad_system.print_status()
```

---

## Assumptions

- All campaign and brand data are in-memory (no DB layer)
- All time logic uses local system time
- Campaign status depends on budget and optional dayparting rules
- Spend updates are manual or simulated

---
