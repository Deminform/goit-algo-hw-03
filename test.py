
# users = [
#     {"name": "Bill Gates", "birthday": "1955.3.27"},
#     {"name": "Steve Jobs", "birthday": "1955.6.28"},
#     {"name": "Jinny Lee", "birthday": "1956.6.29"},
#     {"name": "John Doe", "birthday": "1985.07.02"},
#     {"name": "Jane Smith", "birthday": "1990.01.27"}
# ]


# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()


# def date_to_string(date):
#     return date.strftime("%Y.%m.%d")


# def prepare_user_list(user_data):
#     prepared_list = []
#     for user in user_data:
#         prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
#     return prepared_list


# def find_next_weekday(start_date, weekday):
#     days_ahead = weekday - start_date.weekday()
#     if days_ahead <= 0:
#         days_ahead += 7
#     return start_date + timedelta(days=days_ahead)


# def adjust_for_weekend(birthday):
#     if birthday.weekday() >= 5:
#         return find_next_weekday(birthday, 0)
#     return birthday


# def get_upcoming_birthdays(users, days=7):
#     upcoming_birthdays = []
#     today = date.today()

#     for user in users:
#         birthday_this_year = user["birthday"].replace(year=today.year)

#         if birthday_this_year < today:
#             birthday_this_year = user["birthday"].replace(year=today.year + 1)

#         """
#         Додайте на цьому місці перевірку, чи не буде
#         припадати день народження вже наступного року.
#         """

#         if 0 <= (birthday_this_year - today).days <= days:
#             """
#             Додайте перенесення дати привітання на наступний робочий день,
#             якщо день народження припадає на вихідний.
#             """
#             birthday_this_year = adjust_for_weekend(birthday_this_year)

#             congratulation_date_str = date_to_string(birthday_this_year)
#             upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})
#     return upcoming_birthdays


# ////////////////////////////////////////////////////////////////////////////////////////

# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()


# def date_to_string(date):
#     return date.strftime("%Y.%m.%d")


# def prepare_user_list(user_data):
#     prepared_list = []
#     for user in user_data:
#         prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
#     return prepared_list


# def get_upcoming_birthdays(users, days=7):
#     upcoming_birthdays = []
#     today = date.today()

#     for user in users:
#         birthday = user['birthday']
#         date_birthday = string_to_date(birthday)
#         birthday_this_year = datetime(today.year, date_birthday.month, date_birthday.day)
#         delta_days = birthday_this_year - today
#         if 0 <= int(delta_days.days) <= days:
#             upcoming_birthdays.append({'name': user['name'], 'congratulation_date': birthday_this_year})






#     return upcoming_birthdays

# print(get_upcoming_birthdays(users, 7))


# def get_upcoming_birthdays(users, days=7):
#     upcoming_birthdays = []
#     today = date.today()
#     for user in users:
#         birthday = string_to_date(user['birthday'])
#         birthday_this_year = date(today.year, birthday.month, birthday.day)
#         string_birthday = date_to_string(birthday_this_year)
#         print(type(string_birthday))
#         delta_days = birthday_this_year - today
#         if 0 <= int(delta_days.days) <= days:
#             upcoming_birthdays.append({'name': user['name'], 'congratulation_date': string_birthday})

#     return upcoming_birthdays

# get_upcoming_birthdays(users, 7)



# def find_next_weekday(start_date: datetime, weekday) -> datetime:
#     delta = None
#     start_date_week = start_date.weekday()
#     if 6 == weekday == 5: weekday = 0
#     if start_date_week < weekday:
#         delta = timedelta(days = weekday - start_date_week)
#     else:
#         delta = timedelta(days = 7 - start_date_week + weekday)
#     return start_date + delta


# new_date = string_to_date('2024.6.28')
# find_next_weekday(new_date, 2)

# def prepare_user_list(user_data: list):
#     list = []
#     for item in user_data:
#         dict = {}
#         birth_date = string_to_date(item['birthday'])
#         dict['name'] = item['name']
#         dict['birthday'] = birth_date
#         list.append(dict)
#     return list


# print(prepare_user_list(users))


# prepare_user_list(users)


# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()


# def date_to_string(date: datetime):
#     return date.strftime("%Y.%m.%d")


# print(string_to_date('2020.01.01'))
# print(date_to_string(string_to_date('2020.01.01')))


# chicago_timezone = timezone(timedelta(hours=-8))
# chicago_now = datetime.now(chicago_timezone)

# print(chicago_now.strftime("%H:%M / %Y-%m-%d"))





# current_time = time.time()
# readable_time = time.ctime(current_time)
# local_time = time.localtime(current_time)
# utc_time = time.gmtime(current_time)

# print(current_time)
# print(local_time)
# print(utc_time)
# print(readable_time)




