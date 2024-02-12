import tkinter
from tkinter import *
from tkinter import messagebox
import qrcode

def QRGenerate():
    if(URLEntry.get() == ""):
        messagebox.showwarning(message="URL is empty")
        return
    if(FilenameEntry.get() == ""):
        messagebox.showwarning(message="Filename is empty")
        return
    img = qrcode.make(URLEntry.get())
    img.save(FilenameEntry.get()+".svg")
    messagebox.showinfo(message="QR Code generated")



main = tkinter.Tk()
main.title("QR generator")

Label(main,text="URL:").grid(row=0)
Label(main,text="Filename:").grid(row=1)

URLEntry =Entry(main)
FilenameEntry =Entry(main)
URLEntry.grid(row=0,column=1)
FilenameEntry.grid(row=1,column=1)
button = tkinter.Button(main,text="Generate QR",command=QRGenerate).grid(row=2,column=0)

Message(main,text= "Example of a QR: \n URL example: \n https://www.google.com/ \n Filename example: \n googleQR").grid(column=0)

main.mainloop()


