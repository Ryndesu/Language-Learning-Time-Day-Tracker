from datetime import date # Import datetime module for date calculations
import math # Import math module

# INPUTS -------------------------------------------
print(f"{"Inputs ":-<30}") # Inputs & spacer
# Get total time in hrs, mins, secs
total_time_hrs: int = int(input("Total Time Hrs: "))
total_time_mins: int = int(input("Total Time Mins: "))
total_time_secs: int = int(input("Total Time Secs: "))
# Get target hours
target_time: int = int(input("Target Goal (Hrs): "))
print(f"{"":-<30}\n") # Spacer & line break

# CALCULATIONS -------------------------------------
# Get days remaining until end of year
end_of_year = date(date.today().year, 12, 31) # Get Dec 31 date => yyyy/mm/dd
days_left = (end_of_year - date.today()).days + 1 # Subtract Dec 31 date from today's date => output as days, add 1 for correction
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
print(f"{"Outputs ":-<30}") # Outputs & spacer
print(f"{date.today().strftime("%B %d, %Y")} --> {date(date.today().year, 12, 31).strftime("%B %d, %Y")}") # Today's date --> 12/31
print(f"Days left: {days_left}") # Display days left until 12/31
print(f"Percent to Goal: {percent_to_target:.1f}%") # Display percent to goal rounded to 1 decimal
print(f"Time Per Day: {time_per_day_hrs}h {time_per_day_mins}m") # Display time per day
print(f"{"":-<30}\n") # Spacer & line break
# Pause until keypress
input("Enter to exit...")
