def update_result_label():
    try:
        # Use 'or "0"' so blank entries default to 0 instead of crashing
        str_hrs = total_time_hrs_entry.get() or "0"
        str_mins = total_time_mins_entry.get() or "0"
        str_secs = total_time_secs_entry.get() or "0"
        
        # Target time must be filled out
        str_target = target_time_entry.get()

        # Convert to integers/floats
        total_time_hrs = int(str_hrs)
        total_time_mins = int(str_mins)
        total_time_sec = int(str_secs)
        target_time = float(str_target)

        # Do the calculation
        time_per_day_hrs, time_per_day_mins = get_time_per_day(total_time_hrs, total_time_mins, total_time_sec, target_time)
        
        # Update the UI
        total_time_result_label.configure(text=f"Total time per day: {time_per_day_hrs}hr {time_per_day_mins}min")
        
    except ValueError:
        # If ANY conversion fails, it jumps here and updates the UI with the error
        total_time_result_label.configure(text=value_error)

def get_total_time():
    try:
        # 1. Extract strings, defaulting to "0" if the box is completely empty
        str_hrs = total_time_hrs_entry.get() or "0"
        str_mins = total_time_mins_entry.get() or "0"
        str_secs = total_time_secs_entry.get() or "0"

        # 2. Convert to integers
        total_time_hrs = int(str_hrs)
        total_time_mins = int(str_mins)
        total_time_secs = int(str_secs)

        # 3. Perform the math
        total_time = total_time_hrs + (total_time_mins / 60) + (total_time_secs / 3600)
        
        return total_time

    except ValueError:
        # If the user typed letters, catch it and return 0 (or handle the error visually)
        print("Error: Please enter valid numbers")
        return 0.0
    