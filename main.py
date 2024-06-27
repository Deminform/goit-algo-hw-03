import random
import re
from datetime import datetime


# Module 3 / task 1 - Get date difference in days
def get_days_from_today(string_date: str) -> int:
    try:
        input_date = datetime.strptime(string_date, "%Y-%m-%d").date()
        current_date = datetime.today().date()
        return (current_date - input_date).days
    except ValueError:
        raise ValueError("Please enter a valid date in the format 'YYYY-MM-DD'")


# Module 3 / task 2 - Get a new list of numbers in a custom range
def get_numbers_ticket(min_number, max_number, quantity):
    if min_number >= 1 and max_number <= 1000:
        random_number_set = set()
        while len(random_number_set) < quantity:
            random_number_set.add(random.randint(min_number, max_number))
        return sorted(list(random_number_set))
    else:
        return []


# Module 3 / task 3 - Customize a uniform format for phone numbers
def normalize_phone(phone_number):
    formatted_numbers = []
    for number in phone_number:
        formatted_numbers.append('+38' + re.sub(r'\D*', '', number).removeprefix('38'))
    return formatted_numbers
