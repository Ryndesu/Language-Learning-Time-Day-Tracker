from datetime import date
import math

version: str = "1.1.4"

def get_integer_input(user_input: str) -> int:
    while True:
        try:
            return int(input(user_input))
        except ValueError:
            print("Please input an integer")

# INPUTS -------------------------------------------
print(f"{' [INPUT] ':-^40}")
# Get total time in hrs, mins, secs & target time
total_time_hrs = get_integer_input("Total Time Hrs: ")
total_time_mins = get_integer_input("Total Time Mins: ")
total_time_secs = get_integer_input("Total Time Sec: ")
target_time = get_integer_input("Target Goal (Hrs): ")
print(f"{'':-^40}\n") # Print spacer

# CALCULATIONS -------------------------------------
# Get days remaining until end of year
current_date = date.today()
end_of_year = date(current_date.year, 12, 31) # Get Dec 31 date => yyyy/mm/dd
days_left = (end_of_year - current_date).days + 1 # Subtract Dec 31 date from today's date & output as days, add 1 for correction
# Convert input time -> hrs
total_time: float = total_time_hrs + (total_time_mins / 60) + (total_time_secs / 3600)
# Calculate time per day to reach target goal
time_per_day: float = (target_time - total_time) / (days_left) # Calculate time per day
# Convert time per day -> hrs & mins
time_per_day_mins, time_per_day_hrs = math.modf(time_per_day)
time_per_day_hrs: int = int(time_per_day_hrs) # convert to integer
time_per_day_mins: int = math.ceil(time_per_day_mins * 60) # Convert -> mins & round up
# Calculate percent until target hours
percent_to_target: float = (total_time / target_time) * 100

# OUTPUTS ------------------------------------------
print(f"{' [OUTPUT] ':-^40}")
print(f"{date.today().strftime('%B %d, %Y')} -> {end_of_year.strftime('%B %d, %Y')}") # Today's date -> 12/31
print(f"Days left: {days_left}")
print(f"Percent to Goal: {percent_to_target:.1f}%") # Display percent to goal rounded to 1 decimal
print(f"Time Per Day to Goal: {time_per_day_hrs}h {time_per_day_mins}m")
print(f"{'':-^40}\n") # Print spacer

# DEBUG --------------------------------------------
print(f"{f' [DEBUG | VERSION: {version}] ':-^40}") # REDO THIS *****

def debug(**kwargs) -> None:
    for var_name, var_value in kwargs.items():
        print(f"{var_name} = {var_value}")

debug(
    days_left=days_left,
    total_time=total_time,
    time_per_day=time_per_day,
    time_per_day_hrs=time_per_day_hrs,
    time_per_day_mins=time_per_day_mins,
    percent_to_target=percent_to_target
)

print(f"{'':-^40}\n") # Print spacer

# EXIT ---------------------------------------------
input("Enter to exit...") # Pause until keypress
 
