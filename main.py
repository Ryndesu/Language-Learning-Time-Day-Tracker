from datetime import datetime # Import datetime module for date calculations
import math # Import math module

# INPUTS -------------------------------------------
print('Inputs ------------------------')
# Get total time in hrs, mins, secs
totalTimeHrs: int = int(input('Total Time Hrs: '))
totalTimeMins: int = int(input('Total Time Mins: '))
totalTimeSecs: int = int(input('Total Time Secs: '))
# Get target hours
targetTime: int = int(input('Target Goal (Hrs): '))
print('-------------------------------\n')

# CALCULATIONS -------------------------------------
# Get days remaining until end of year
endOfYear = datetime(datetime.today().year, 12, 31) # Get Dec 31 date => yyyy/mm/dd
daysLeft = (endOfYear - datetime.today()).days # Subtract Dec 31 date from today's date => output as days
# Convert input time -> hrs
totalTime: float = totalTimeHrs + (totalTimeMins / 60) + (totalTimeSecs / 3600)
# Calculate time per day to reach target goal
timePerDay: float = (targetTime - totalTime) / (daysLeft + 2) # Add 2 to get time including today
# Convert time per day -> hrs & mins
timePerDayMins, timePerDayHrs = math.modf(timePerDay)
timePerDayHrs: int = int(timePerDayHrs) # convert to integer
timePerDayMins: int = math.ceil(timePerDayMins * 60) # Convert -> mins & round up
# Calculate percent until target hours
percentToTarget: float = (totalTime / targetTime) * 100

# OUTPUTS ------------------------------------------
print('Outputs -----------------------')
print(f'Percent to Goal: {percentToTarget:.2f}%') # :2f returns with 2 decimal places
print(f'Time Per Day: {timePerDayHrs}h {timePerDayMins}m')
print('-------------------------------\n')
# Pause until keypress
input("Enter to exit...")
