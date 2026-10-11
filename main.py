from datetime import datetime # Import datetime module for date calculations
import math # Import math module

# INPUTS -------------------------------------------
print('Inputs ------------------------')
# Get total time in hrs, mins, secs
total_time_hrs: int = int(input('Total Time Hrs: '))
total_time_mins: int = int(input('Total Time Mins: '))
total_time_secs: int = int(input('Total Time Secs: '))
# Get target hours
target_time: int = int(input('Target Goal (Hrs): '))
print('-------------------------------\n')

# CALCULATIONS -------------------------------------
# Get days remaining until end of year
end_of_year = datetime(datetime.today().year, 12, 31) # Get Dec 31 date => yyyy/mm/dd
days_left = (end_of_year - datetime.today()).days # Subtract Dec 31 date from today's date => output as days
# Convert input time -> hrs
total_time: float = total_time_hrs + (total_time_mins / 60) + (total_time_secs / 3600)
# Calculate time per day to reach target goal
time_per_day: float = (target_time - total_time) / (days_left + 2) # Add 2 to get time including today
# Convert time per day -> hrs & mins
time_per_day_mins, time_per_day_hrs = math.modf(time_per_day)
time_per_day_hrs: int = int(time_per_day_hrs) # convert to integer
time_per_day_mins: int = math.ceil(time_per_day_mins * 60) # Convert -> mins & round up
# Calculate percent until target hours
percent_to_target: float = (total_time / target_time) * 100

# OUTPUTS ------------------------------------------
print('Outputs -----------------------')
print(f'Percent to Goal: {percent_to_target:.2f}%') # :2f returns with 2 decimal places
print(f'Time Per Day: {time_per_day_hrs}h {time_per_day_mins}m')
print('-------------------------------\n')
# Pause until keypress
input("Enter to exit...")
