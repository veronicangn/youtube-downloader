import tkinter
import customtkinter
from pytube import YouTube

# function to download the video
def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()  # gets highest resolution video
        video.download()
    except:
        print("Youtube link is invalid")
    print("Download complete!")


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
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Create Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)

# Run app
app.mainloop();