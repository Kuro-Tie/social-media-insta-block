import tkinter as tk
from tkinter import ttk

class GUIApp(tk.Tk):
    def __init__(self,mytitle,size):
        super().__init__()
        self.title(mytitle)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0],size[1])
        self.maxsize(size[0],size[1])
        self.menu = Menu(self)

        self.mainloop()

class Menu(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)    
        self.place(x=0,y=0)
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.Label_text = ttk.Label(self, text="Instagram Blocker!",font=('Helvetica',18), background="orange")
        self.Block_button = ttk.Button(self, text="Block")
        self.UNBlock_button = ttk.Button(self, text="Unblock")
        self.CodedByText = ttk.Label(self, text="Coded By Kuro-Tie",font=('Helvetica',18), background="purple")
    def create_layout(self):
        self.columnconfigure((0,1,2), weight = 1, uniform = 'a')
        self.rowconfigure((0,1,2,3,4), weight = 1, uniform = 'a')
        self.Label_text.grid(row=0,column=0,sticky='nswe',columnspan=4)
        self.Block_button.grid(row=1,column=0,sticky='nswe',columnspan=2)
        self.UNBlock_button.grid(row=1,column=2,sticky='nswe',columnspan=2)
        self.CodedByText.grid(row=2,column=0,columnspan=4,sticky='nswe')
GUIApp("Instagram Blocker", (210,120))