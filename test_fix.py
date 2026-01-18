import datetime
import calendar
from app import get_monthly_target

def test_jan_2026():
    year, month, target = get_monthly_target(2026, 1)
    print(f"Year: {year}, Month: {month}")
    print(f"Days in month: {target['num_days']}")
    print(f"Working days: {target['workdays']}")
    print(f"Total hours: {target['total_hours']}")
    
    # In Jan 2026, there are 31 days.
    # Weekdays:
    # 1 (Thu) - Holiday
    # 2 (Fri) - Work
    # 5-9 (Mon-Fri) - 5 days
    # 12-16 (Mon-Fri) - 5 days
    # 19-23 (Mon-Fri) - 5 days
    # 26-30 (Mon-Fri) - 5 days
    # Total weekdays = 1 (Jan 1) + 1 (Jan 2) + 5 + 5 + 5 + 5 = 22
    # Subtract Jan 1 (Holiday) -> 21
    
    assert target['workdays'] == 21, f"Expected 21 working days, but got {target['workdays']}"
    print("Test passed!")

if __name__ == "__main__":
    try:
        test_jan_2026()
    except Exception as e:
        print(f"Test failed: {e}")
