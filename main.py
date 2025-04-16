from core.models import Brand, Campaign
from core.schedule import DaypartingSchedule
from core.system import AdSystem
import datetime


def main():
    ad_system = AdSystem()

    # Create brands
    nike = Brand(1, "Nike", 100.0, 3000.0)
    adidas = Brand(2, "Adidas", 80.0, 2400.0)

    ad_system.add_brand(nike)
    ad_system.add_brand(adidas)

    # Create dayparting schedules
    morning = DaypartingSchedule(8, 12)
    evening = DaypartingSchedule(18, 22)

    # Add campaigns
    ad_system.add_campaign(Campaign(1, nike.id, "Nike Running", morning))
    ad_system.add_campaign(Campaign(2, nike.id, "Nike Basketball"))
    ad_system.add_campaign(Campaign(3, adidas.id, "Adidas Soccer", evening))

    # Simulate spend
    ad_system.update_campaign_spend(1, 30.0)
    ad_system.update_campaign_spend(2, 50.0)
    ad_system.update_campaign_spend(3, 40.0)

    ad_system.check_all_campaigns()
    ad_system.print_status()

    # Exceed Nike's budget
    print("\nSimulating exceeding daily budget for Nike...")
    ad_system.update_campaign_spend(1, 30.0)
    ad_system.update_campaign_spend(2, 50.0)
    ad_system.check_all_campaigns()
    ad_system.print_status()

    ad_system.update_campaign_spend(2, 10.0)
    ad_system.check_all_campaigns()
    ad_system.print_status()

    print("\nSimulating a new day...")
    ad_system.last_update_day = (datetime.datetime.now().day - 1) % 28
    ad_system.check_and_reset_budgets()
    ad_system.check_all_campaigns()
    ad_system.print_status()


if __name__ == "__main__":
    main()
