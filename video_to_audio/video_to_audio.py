import moviepy.editor as mp
from tkinter import *
from tkinter import filedialog

# Now we are going to create a function Uploading the Video File


def upload():
    # uploading file
    filename = filedialog.askopenfilename(
        filetypes=[('Mp4 Files', '*.mp4'), ('WMV Files', '*.wmv'), ('ogg files', '*.ogg')])
    # The message showing when the file is uploaded
    messageForUpload.set("File Uploaded:"+filename)
    # declaring global variable
    global fname
    # passing uploaded filename into fname
    fname = filename

# Now we are going to create a function converting video file to audio file


def convert():
    videoClip = mp.VideoFileClip(fname)
    # The generated audio filename is hello
    videoClip.audio.write_audiofile("hello.mp3")
    messageToGenerate.set(
        "Congradulation,Audio file is generated successfully")


# project canva
root = Tk()

# setting window height and width
root.geometry("700x250")

# setting project/window bacground color
root["bg"] = "pink"

# setting project title
root.title("Video to audio converting app done by Yuvaraj")

# create variables for messages
global messageForUpload
global messageToGenerate
messageForUpload = StringVar()
messageToGenerate = StringVar()

# Label for uploading message
Label(root, text="hello", textvar=messageForUpload,
      font="Arial 12", fg="#fff", bg="green").place(x=100, y=40)

# button for uploading file
Button(root, text="Upload Video", command=upload,
       font="Arial 12 bold", fg="#fff", bg="green").place(x=100, y=70)

# Label for converting message
Label(root, text="hello", textvar=messageToGenerate,
      font="Arial 12", fg="#fff", bg="green").place(x=100, y=120)

# button for converting video to audio
Button(root, text="Convert Video", command=convert,
       font="Arial 12 bold", fg="#fff", bg="green").place(x=350, y=70)


root.mainloop()
