from datetime import datetime
today = datetime.now().date()
target_date = datetime(2025, 1, 1).date()
days_remaining = (target_date - today).days
print(f"There are {days_remaining} days left until 2025.")