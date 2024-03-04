import tkinter
import customtkinter
from pytube import YouTube

# function to download the video
def startDownload(event=None):
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()  # gets highest resolution video
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Download completed!", text_color="green", font=("Calibri", 15, "bold"))
    except:
        finishLabel.configure(text="Download Error", text_color="red", font=("Calibri", 15, "bold"))
    
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
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()  # initializes

app.geometry("720x480")  # screen size
app.title("Youtube Downloader")


# Add UI Elements
# first argument specifies where to put item
app_title = customtkinter.CTkLabel(app, text="Youtube Video Downloader", font=("Calibri", 30, "bold"))
app_title.pack(padx=10, pady=10)

title = customtkinter.CTkLabel(app, text="Insert a Youtube Link:", font=("Calibri", 20))  
title.pack(padx=10, pady=10)

# Create input box to put in Youtube link
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var, font=("Calibri", 15))
link.pack()

# Create Download button
download = customtkinter.CTkButton(app, text="Download!", command=startDownload, font=("Calibri", 15),
                                   fg_color="lightcoral", hover_color="lightpink", width=45, height=45,
                                   text_color="black")
download.pack(padx=10, pady=20)

app.bind("<Return>", startDownload)  # allows user to press "Enter" on keyboard to download

# Create progress bar
progressBar = customtkinter.CTkProgressBar(app, width=400, progress_color="lightcoral")
progressBar.set(0)  # initalizes to 0%
progressBar.pack(padx=10, pady=10)

# Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%", font=("Calibri", 15))
pPercentage.pack()

# Finished Downloading text
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Runs the app
app.mainloop();