import tkinter as tk
from gui import App
from model import Model
from agents import Agent

class Controller:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.agent = Agent()
        self.model = Model(self.agent)
        self.gui = App(self.root, self, self.model)
        self.root.title("Q-Learning Playground")
        self.gui.pack(fill='both', expand=True)
    
    def run(self):
        self.root.mainloop()