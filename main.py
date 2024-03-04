import tkinter
import customtkinter
from pytube import YouTube

# default system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()  # initializes
app.geometry("720x480")  # screen size
app.title("Youtube Downloader")

# Add UI Elements
title = customtkinter.CTkLabel(app, text="Insert a Youtube link")  # first argument specifies where to put item
title.pack(padx=10, pady=10)

# Create input box to put in Youtube link
link = customtkinter.CTkEntry(app, width=350, height=40)
link.pack()

# Run app
app.mainloop();