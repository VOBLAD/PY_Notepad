from tkinter import *
from tkinter import filedialog

def save():
    open_file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if open_file is None:
        return
    text = str(txt.get(1.0, END))
    open_file.write(text)
    open_file.close()


def upload():
    file = filedialog.askopenfile(mode='r', filetype=[('text files', '*.txt')])
    if file is not None:
        content = file.read()
    txt.insert(INSERT, content)



root = Tk()
root.geometry("800x600")
root.config(bg="navy blue")
root.title("Блокнот")
root.resizable(False, False)

icon = PhotoImage(file="2.png")
icon1 = PhotoImage(file="1.png")


btns = Button(root, command=save, image=icon, bg="navy blue", relief=FLAT).place(y=180)



btnu = Button(root, command=upload, image=icon1, bg="navy blue", relief=FLAT)
btnu.pack(side=LEFT)

txt = Text(root, fg="black", font="Arial 20 bold", wrap=WORD)
txt.pack()



root.mainloop()