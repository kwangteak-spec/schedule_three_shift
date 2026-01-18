import datetime
import calendar
from holidays import is_holiday

def calculate_workdays(year, month):
    num_days = calendar.monthrange(year, month)[1]
    workdays = 0
    for day in range(1, num_days + 1):
        d = datetime.date(year, month, day)
        weekday = d.weekday()
        if weekday < 5 and not is_holiday(d):
            workdays += 1
    return workdays

def test_jan_2026():
    workdays = calculate_workdays(2026, 1)
    print(f"Jan 2026 Working Days: {workdays}")
    assert workdays == 21, f"Expected 21, got {workdays}"
    print("Test passed!")

if __name__ == "__main__":
    test_jan_2026()
