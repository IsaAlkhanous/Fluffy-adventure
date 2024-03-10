import tkinter as tk
from tkinter import font

  
class window:
    def __init__(self):
        self.window = tk.Tk() 
        self.window.geometry("640x480")
        self.window.title("Fluffy Adventure")
        self.window.config(background = "black")
        
        self.init_UI()
        
    def click(self):
        print("meow")

    def init_UI(self):
        self.photo = tk.PhotoImage(file='Scene 1.png')
        self.title = tk.Label(self.window,text = "A Fluffy Adventure", 
                              font=("Poly", 48, "bold"),
                              fg="white",
                              bg="black",
                              compound="center").pack(pady=80)
        self.start = tk.Button(self.window,text = "START GAME",
                               command=self.start_game(),
                               font =("Poly",20,"underline"),
                               fg="white", bg="black",border=0,
                               compound="center").pack()
    def start_game(self):
        
    def scenes(self):
        
    def run(self):
        self.window.mainloop()
    
    
