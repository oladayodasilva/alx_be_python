from datetime import datetime, timedelta

# Part 1: Current date and time
now = datetime.now()
print("Current date and time:", now)

# Part 2: Formatting date
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date:", formatted)

# Part 3: Adding user-specified days
days_to_add = int(input("Enter the number of days to add: "))
future_date = now + timedelta(days=days_to_add)
print(f"Date after {days_to_add} days:", future_date.strftime("%Y-%m-%d"))

# Part 4: Difference between two dates (example)
date1 = datetime(2025, 9, 22)
date2 = datetime(2025, 9, 29)
difference = date2 - date1
print("Days between dates:", difference.days)
