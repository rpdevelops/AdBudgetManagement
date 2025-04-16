import datetime
from core.models import Brand, Campaign
from core.schedule import DaypartingSchedule
from core.system import AdSystem


def test_end_to_end_campaign_lifecycle():
    ad_system = AdSystem()

    brand = Brand(1, "TestBrand", daily_budget=100.0, monthly_budget=500.0)
    ad_system.add_brand(brand)

    schedule_all_day = DaypartingSchedule(0, 23)

    campaign1 = Campaign(1, brand_id=1, name="Campaign A", dayparting_schedule=schedule_all_day)
    campaign2 = Campaign(2, brand_id=1, name="Campaign B", dayparting_schedule=schedule_all_day)
    campaign3 = Campaign(3, brand_id=1, name="Campaign C")

    ad_system.add_campaign(campaign1)
    ad_system.add_campaign(campaign2)
    ad_system.add_campaign(campaign3)

    # Initial spend below budget
    ad_system.update_campaign_spend(3, 50.0)
    ad_system.check_all_campaigns()
    assert brand.current_daily_spend == 50.0
    assert campaign3.is_active
    assert campaign1.is_active
    assert campaign2.is_active

    # Spend enough to exceed daily budget
    ad_system.update_campaign_spend(3, 60.0)
    ad_system.check_all_campaigns()
    assert brand.current_daily_spend == 110.0
    assert not campaign1.is_active
    assert not campaign2.is_active
    assert not campaign3.is_active

    # Simulate a new day
    ad_system.last_update_day = (datetime.datetime.now().day - 1) % 28 or 1
    ad_system.check_and_reset_budgets()
    ad_system.check_all_campaigns()
    assert campaign1.is_active
    assert campaign2.is_active
    assert campaign3.is_active

    # Exceed monthly budget
    ad_system.update_campaign_spend(3, 500.0)
    ad_system.check_all_campaigns()
    assert brand.is_monthly_budget_exceeded()
    assert not campaign1.is_active
    assert not campaign2.is_active
    assert not campaign3.is_active
