#pip install holidays
import datetime
import holidays

def next_holiday():
    today = datetime.date.today()
    year = today.year

    # Use your country's holidays (example: US, but you can change to holidays.Morocco() etc.)
    country_holidays = holidays.US(years=[year, year+1])

    # Find the next holiday
    for date, name in sorted(country_holidays.items()):
        if date >= today:
            delta = date - today
            print("Today's date:", today)
            print(f"The next holiday is {name} in {delta.days} days.")
            return

next_holiday()
