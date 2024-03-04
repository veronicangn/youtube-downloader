import tkinter
import customtkinter
from pytube import YouTube

# function to download the video
def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()  # gets highest resolution video
        title.configure(text=ytObject.title, text_color="black")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Download complete!")
    except:
        finishLabel.configure(text="Download Error", text_color="red")
    
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    completion_percentage = bytes_downloaded/ total_size * 100
    per = str(int(completion_percentage))
    pPercentage.configure(text=per + "%")
    pPercentage.update()

    # update progress bar
    progressBar.set(float(completion_percentage) / 100)

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

# Finished Downloading text
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)  # initalizes to 0%
progressBar.pack(padx=10, pady=10)

# Create Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Run app
app.mainloop();