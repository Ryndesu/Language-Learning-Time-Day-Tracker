import customtkinter as ctk

def printinput():
    user_input = custom_input.get()
    print(user_input)

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("720x480")
app.title("Test")

title = ctk.CTkLabel(app, text="This is a test")
title.pack(padx=10, pady=10)

custom_input = ctk.CTkEntry(app, width=350, height=40)
custom_input.pack()

button = ctk.CTkButton(app, text="Test Button", command=printinput)
button.pack(padx=10, pady=10)

temp = ctk.CTkSwitch(app, text="Test")
temp.pack(padx=10, pady=10)

app.mainloop()