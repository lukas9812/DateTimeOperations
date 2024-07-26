from datetime import datetime

# getting the current date and time
current_datetime = datetime.now()

# getting the year from the current date and time
current_year = current_datetime.strftime("%Y")
print("current year = ", current_year)

# getting the month from the current date and time
current_month = current_datetime.strftime("%m")
print("current month = ", current_month)

# getting the day/date from the current date and time
current_day = current_datetime.strftime("%d")
print("current day = ", current_day)

# getting the time from the current date and time in the given format
current_time = current_datetime.strftime("%H:%M:%S")
print("current time = ", current_time)

# getting the date and time from the current date and time in the given format
current_date_time = current_datetime.strftime("%m/%d/%Y, %H:%M:%S")
print("current date and time = ", current_date_time)

#Days until end of year.
day_of_year = current_datetime.timetuple().tm_yday
print("Today is {} th day of year".format(day_of_year))


def count_days_until_end_of_year(day_of_year):
    return 365 - day_of_year;


print("Until end of year remaining {} days.".format(count_days_until_end_of_year(day_of_year)))
