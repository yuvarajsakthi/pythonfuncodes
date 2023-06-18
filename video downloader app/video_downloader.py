# Import Libraries needed in the project
from tkinter import *
from pytube import YouTube

# Create the API windows or frame
root = Tk()
root.geometry("600x350")
root.resizable(0, 0)
root.config(bg="pink")
root.title("Youtube Video Downloader App")

# Create the text and link entry widgets
Label(root, text="Download any Youtube videos for free",
      font='Arial 14 bold').place(x=100, y=20)
Label(root, text="Paste your Favorite link here",
      font='Arial 14', bg='pink', fg='green').place(x=120, y=50)

# entery widget
videoLink = StringVar()
Entry(root, width=80, textvariable=videoLink).place(x=35, y=85)

# Creating the download function


def downloadVideo():
    url = YouTube(str(videoLink.get()))
    videoStream = url.streams.first()
    videoStream.download()  # Download Location goes here
    Label(root, text="Download Completed Successfully",
          font='Arial 14 bold', bg='green', fg='white').place(x=120, y=180)


# Create the download button
Button(root, text="Download Now", font='Arial 16 bold', bg='red',
       padx=2, command=downloadVideo).place(x=180, y=120)


root.mainloop()
