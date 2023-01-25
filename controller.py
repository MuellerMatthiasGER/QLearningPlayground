import tkinter as tk
from gui import App

class Controller:
    def __init__(self):
        self.root = tk.Tk()
        # self.model = Model()
        self.gui = App(self.root, self)
        self.root.title("Q-Learning Playground")
        self.root.mainloop()