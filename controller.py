import tkinter as tk
from gui import App
from model import Model

class Controller:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.model = Model()
        self.gui = App(self.root, self, self.model)
        self.root.title("Q-Learning Playground")
        self.gui.pack(fill='both', expand=True)
    
    def run(self):
        self.root.mainloop()

    def next_step(self):
        self.model.next_step()
        self.gui.update()

    def execute_n_iterations(self, iterations: int):
        for _ in range(iterations):
            self.model.next_iteration()
        self.gui.update()