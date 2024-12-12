from tkinter import*
from gtts import gTTS
from playsound import playsound
def play_text():
    text = text_entry.get()
    if text:
        myjob=gTTS(text=text,lang="en")
        myjob.save('welcome.mp3')
        playsound('welcome.mp3')

def clear_text():
    text_entry.delete(0, 'end')

root=Tk()
root.title("Text to Speech")
root.geometry("300x500")


Label(root, text="Text to Speech" ,font=("Times", 20)).pack(pady=10)
label1=Label(root,text="Enter Your Text :", font="Arial 12",fg="red").pack(pady=10)

text_entry = Entry(root, width=40, font=("New Roman", 14))
text_entry.pack(pady=10)
play_button = Button(root, text="Play", command=play_text, bg="gray", fg="white", font=("Helvetica", 14))
play_button.pack(side="left", padx=14, pady=20)

exit_button = Button(root, text="Exit", command=root.quit, bg="red", fg="white", font=("New Roman", 14))
exit_button.pack(side="right", padx=14, pady=20)

set_button = Button(root, text="Set", command=clear_text, bg="blue", fg="white", font=("New Roman", 14))
set_button.pack(side="top",padx=14, pady=20)


root.mainloop()








