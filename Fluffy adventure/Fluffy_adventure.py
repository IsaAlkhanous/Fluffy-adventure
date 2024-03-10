from tkinter import * 

def click():
    print("meow")

window =Tk() #initiate window
window.geometry("420x420")
window.title("Fluffy Adventure")
window.config(background = "black")

photo = PhotoImage(file='Scene 1.png')
title = Button(window,text = "Fluffy Adventure", font=("Calibri", 40, "bold"),command=click,
                                                fg="white",bg="black",
                                                image = photo,
                                                compound="center")
title.pack()
window.mainloop()   
