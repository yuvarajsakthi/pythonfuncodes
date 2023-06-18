from tkinter import *
from translate import Translator

# Creating display window
Screen = Tk()
Screen.title("Language Translator App")
Screen.geometry("450x350")
Screen.resizable(0, 0)
Screen.config(bg="pink")

# input widget
InputLanguageChoice = StringVar()
InputLanguageChoice.set("English")
LanguageChoices = OptionMenu(
    Screen, InputLanguageChoice, 'Hindi', 'English', 'French', 'German', 'Spanish')
LanguageChoices.config(bg="green", fg="white")
LanguageChoices["menu"].config(bg="red")
LanguageChoices.grid(row=2, column=2, pady=10, ipadx=15)

# output widget
OutputLanguageChoice = StringVar()
OutputLanguageChoice.set("Choose Here")
LanguageChoices = OptionMenu(
    Screen, OutputLanguageChoice, 'Hindi', 'English', 'French', 'German', 'Spanish', 'Amharic')
LanguageChoices.config(bg="green", fg="white")
LanguageChoices["menu"].config(bg="red")
LanguageChoices.grid(row=2, column=2, pady=10, ipadx=15)

# input text widget
Label(Screen, text="Enter Text Here").grid(row=3, column=1)
TextVar = StringVar()
Textbox = Entry(Screen, textvariable=TextVar).grid(
    row=3, column=2, ipadx=15, ipady=20)

# output text widget
Label(Screen, text="Output Text").grid(row=3, column=3)
OutputVar = StringVar()
Textbox = Entry(Screen, textvariable=OutputVar).grid(
    row=3, column=4, ipadx=15, ipady=20)

# defining function


def Translate():
    translator = Translator(
        from_lang=InputLanguageChoice.get(), to_lang=OutputLanguageChoice.get())
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)


# Button for calling function
B = Button(Screen, text="Translate", command=Translate,
           relief=GROOVE).grid(row=4, column=3)

Screen.mainloop()
