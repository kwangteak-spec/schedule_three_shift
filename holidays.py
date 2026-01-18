import datetime

def get_korean_holidays(year):
    """
    Returns a set of datetime.date objects for Korean public holidays in the given year.
    For 2026, it returns the hardcoded list.
    """
    holidays = set()
    
    if year == 2026:
        # New Year's Day
        holidays.add(datetime.date(2026, 1, 1))
        
        # Seollal (Lunar New Year)
        holidays.add(datetime.date(2026, 2, 16))
        holidays.add(datetime.date(2026, 2, 17))
        holidays.add(datetime.date(2026, 2, 18))
        
        # Independence Movement Day
        holidays.add(datetime.date(2026, 3, 1))
        # Substitute holiday for Mar 1
        holidays.add(datetime.date(2026, 3, 2))
        
        # Children's Day
        holidays.add(datetime.date(2026, 5, 5))
        
        # Buddha's Birthday
        holidays.add(datetime.date(2026, 5, 24))
        # Substitute holiday for Buddha's Birthday
        holidays.add(datetime.date(2026, 5, 25))
        
        # Memorial Day
        holidays.add(datetime.date(2026, 6, 6))
        
        # Liberation Day
        holidays.add(datetime.date(2026, 8, 15))
        
        # Chuseok
        holidays.add(datetime.date(2026, 9, 24))
        holidays.add(datetime.date(2026, 9, 25))
        holidays.add(datetime.date(2026, 9, 26))
        
        # National Foundation Day
        holidays.add(datetime.date(2026, 10, 3))
        # Substitute holiday for National Foundation Day
        holidays.add(datetime.date(2026, 10, 5))
        
        # Hangeul Day
        holidays.add(datetime.date(2026, 10, 9))
        
        # Christmas
        holidays.add(datetime.date(2026, 12, 25))
        
    else:
        # For other years, basic fixed holidays (as a placeholder)
        holidays.add(datetime.date(year, 1, 1))
        holidays.add(datetime.date(year, 3, 1))
        holidays.add(datetime.date(year, 5, 5))
        holidays.add(datetime.date(year, 6, 6))
        holidays.add(datetime.date(year, 8, 15))
        holidays.add(datetime.date(year, 10, 3))
        holidays.add(datetime.date(year, 10, 9))
        holidays.add(datetime.date(year, 12, 25))
        
    return holidays

def is_holiday(date):
    """
    Checks if a given date is a holiday.
    """
    holidays = get_korean_holidays(date.year)
    return date in holidays
