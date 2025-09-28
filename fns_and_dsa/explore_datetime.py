from datetime import datetime, timedelta


def display_current_datetime():
    """Display and return the current date and time in YYYY-MM-DD HH:MM:SS format"""
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", current_date)
    return current_date


def calculate_future_date(days):
    """Calculate and return the date after a given number of days"""
    now = datetime.now()
    future_date = now + timedelta(days=days)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future)
    return formatted_future


if __name__ == "__main__":
    # Part 1
    display_current_datetime()

    # Part 2
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Invalid input. Please enter an integer.")
