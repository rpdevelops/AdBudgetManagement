import datetime
from typing import Dict
from .models import Brand, Campaign

class AdSystem:
    def __init__(self):
        self.brands: Dict[int, Brand] = {}
        self.campaigns: Dict[int, Campaign] = {}
        now = datetime.datetime.now()
        self.last_update_day = now.day
        self.last_update_month = now.month

    def add_brand(self, brand: Brand):
        self.brands[brand.id] = brand

    def add_campaign(self, campaign: Campaign):
        if campaign.brand_id not in self.brands:
            raise ValueError(f"Brand ID {campaign.brand_id} not found")
        self.campaigns[campaign.id] = campaign

    def update_campaign_spend(self, campaign_id: int, amount: float):
        if campaign_id not in self.campaigns:
            raise ValueError("Campaign ID not found")
        campaign = self.campaigns[campaign_id]
        brand = self.brands[campaign.brand_id]

        if campaign.should_run():
            brand.update_spend(amount)
            self._check_campaign_status(campaign)

    def _check_campaign_status(self, campaign: Campaign):
        brand = self.brands[campaign.brand_id]
        if brand.is_monthly_budget_exceeded() or brand.is_daily_budget_exceeded():
            campaign.is_active = False

    def check_all_campaigns(self):
        for campaign in self.campaigns.values():
            brand = self.brands[campaign.brand_id]
            if brand.is_monthly_budget_exceeded() or brand.is_daily_budget_exceeded():
                campaign.is_active = False
            else:
                campaign.is_active = campaign.should_run()

    def check_and_reset_budgets(self):
        now = datetime.datetime.now()

        if now.month != self.last_update_month:
            for brand in self.brands.values():
                brand.reset_monthly_spend()
            self.last_update_month = now.month
            for campaign in self.campaigns.values():
                campaign.is_active = True

        if now.day != self.last_update_day:
            for brand in self.brands.values():
                brand.reset_daily_spend()
            self.last_update_day = now.day
            for campaign in self.campaigns.values():
                if not self.brands[campaign.brand_id].is_monthly_budget_exceeded():
                    campaign.is_active = True

    def print_status(self):
        print("\n--- Status ---")
        for brand in self.brands.values():
            print(f"{brand.name} - Daily: ${brand.current_daily_spend:.2f}/${brand.daily_budget:.2f}, Monthly: ${brand.current_monthly_spend:.2f}/${brand.monthly_budget:.2f}")
        for campaign in self.campaigns.values():
            brand = self.brands[campaign.brand_id]
            status = "ACTIVE" if campaign.should_run() else "INACTIVE"
            print(f"Campaign {campaign.name} ({brand.name}): {status}")
