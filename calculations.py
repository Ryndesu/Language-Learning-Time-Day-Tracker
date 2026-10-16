from datetime import date
from math import modf, ceil

# Date calculations
current_date = date.today()
end_of_year = date(current_date.year, 12, 31) # Get Dec 31 date => yyyy/mm/dd
days_left = (end_of_year - current_date).days + 1 # Subtract Dec 31 date from today's date & output as days, add 1 for correction

def get_time_per_day(total_time_hrs, total_time_mins, total_time_sec, target_time):
    total_time = total_time_hrs + (total_time_mins / 60) + (total_time_sec / 3600)
    time_per_day = (target_time - total_time) / days_left
    time_per_day_mins, time_per_day_hrs = modf(time_per_day)
    time_per_day_hrs: int = int(time_per_day_hrs) # convert to integer
    time_per_day_mins: int = ceil(time_per_day_mins * 60) # Convert to mins -> round up
    return time_per_day_hrs, time_per_day_mins

def get_percent_to_target(total_time, target_time):
    percent_to_target = (total_time / target_time) * 100
    return percent_to_target
