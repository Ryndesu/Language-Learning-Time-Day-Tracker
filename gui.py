import customtkinter as ctk
from calculations import get_time_per_day, get_percent_to_target

version_number = "1.0.1"
value_error = "Error: Input a number"

# SETUP --------------------------------------------
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("720x480")
app.title(f"Time Per Day Calculator | v{version_number}")

# INPUTS -------------------------------------------
input_label = ctk.CTkLabel(app, text="Inputs:")
input_label.pack(padx=10, pady=10)

total_time_hrs_entry = ctk.CTkEntry(app, corner_radius=10, placeholder_text="Hours")
total_time_hrs_entry.pack(padx=10, pady=10)

total_time_mins_entry = ctk.CTkEntry(app, corner_radius=10, placeholder_text="Minutes")
total_time_mins_entry.pack(padx=10, pady=10)

total_time_secs_entry = ctk.CTkEntry(app, corner_radius=10, placeholder_text="Seconds")
total_time_secs_entry.pack(padx=10, pady=10)

target_time_entry = ctk.CTkEntry(app, corner_radius=10, placeholder_text="Target Time")
target_time_entry.pack(padx=10, pady=10)

# LABELS -------------------------------------------
total_time_result_label = ctk.CTkLabel(app, text="Total Time: ")
total_time_result_label.pack(padx=10, pady=10)

percent_to_target_label = ctk.CTkLabel(app, text="Percent to target: ")
percent_to_target_label.pack(padx=10, pady=10)

# FUNCTIONS ----------------------------------------
target_time = target_time_entry.get()

def get_total_time():
    try:
        total_time_hrs = int(total_time_hrs_entry.get())
    except TypeError:
        print(value_error)
    try:
        total_time_mins = int(total_time_mins_entry.get())
    except TypeError:
        print(value_error)
    try:
        total_time_secs = int(total_time_secs_entry.get())
    except TypeError:
        print(value_error)

    total_time = total_time_hrs + (total_time_mins / 60) + (total_time_secs / 3600)
    return total_time

def update_total_time_result_label():
    try:
        total_time_hrs = int(total_time_hrs_entry.get())
    except ValueError:
        print(value_error)

    try:
        total_time_mins = int(total_time_mins_entry.get())
    except ValueError:
        print(value_error)

    try:
        total_time_sec = int(total_time_secs_entry.get())
    except ValueError:
        print(value_error)

    try:
        target_time = int(target_time_entry.get())
    except ValueError:
        print(value_error)

    time_per_day_hrs, time_per_day_mins = get_time_per_day(total_time_hrs, total_time_mins, total_time_sec, target_time)
    total_time_result_label.configure(text=f"Total time per day: {time_per_day_hrs}hr {time_per_day_mins}min")

def update_percent_to_target_label():
    try:
        target_time = int(target_time_entry.get())
    except ValueError:
        print(value_error)

    percent_to_target = get_percent_to_target(get_total_time(), target_time)
    percent_to_target_label.configure(text=f"Percent to target: {percent_to_target}%")

def calculate():
    update_total_time_result_label()
    update_percent_to_target_label()

button = ctk.CTkButton(app, corner_radius=10, text="Calculate", command=calculate)
button.pack(padx=10, pady=10)

app.mainloop()
