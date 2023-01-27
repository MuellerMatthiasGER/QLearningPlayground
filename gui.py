import tkinter as tk
from tkinter import ttk
from model import Model
import shapes

CANVAS_MAX_WIDTH = 800
CANVAS_MAX_HEIGHT = 500
LINE_WIDTH = 3

class Grid(tk.Frame):
    def __init__(self, parent) -> None:
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.n_rows = self.parent.model.env.n_rows
        self.n_cols = self.parent.model.env.n_cols
        self.cell_size = min(CANVAS_MAX_WIDTH / self.n_cols, CANVAS_MAX_HEIGHT / self.n_rows)
        self.width = self.cell_size * self.n_cols
        self.height = self.cell_size * self.n_rows

        self.canvas = tk.Canvas(self, width=self.width, height=self.height, borderwidth=3)

        self.canvas.pack()

        self.draw()

    def draw(self):
        self.draw_qtable()
        self.draw_tiles()
        self.draw_grid()

    def draw_tiles(self):
        tiles = self.parent.model.env.tiles
        for row in range(tiles.shape[0]):
            for col in range(tiles.shape[1]):
                tile = tiles[row, col]
                x = col * self.cell_size
                y = row * self.cell_size
                if tile == '#':
                    self.canvas.create_rectangle(x, y, x + self.cell_size, y + self.cell_size, fill='#333')
                elif tile == 'G':
                    points = shapes.get_star_shape(x + self.cell_size / 2, y + self.cell_size / 2, self.cell_size * 0.4)
                    self.canvas.create_polygon(points, fill='#FD0')
                elif tile == 'A':
                    self.canvas.create_rectangle(x, y, x + self.cell_size, y + self.cell_size, fill='#F00')

    def draw_qtable(self):
        pass

    def draw_grid(self) -> None:
        # outline
        self.canvas.create_rectangle(6, 6, self.width, self.height, width=LINE_WIDTH)

        # draw vertical lines
        for i in range(1, self.n_rows):
            y = i * self.cell_size
            self.canvas.create_line(0, y, self.width, y, width=LINE_WIDTH)

        # draw horizontal lines
            for i in range(1, self.n_cols):
                x = i * self.cell_size
                self.canvas.create_line(x, 0, x, self.height, width=LINE_WIDTH)

class ControlPanel(tk.Frame):
    def __init__(self, parent) -> None:
        tk.Frame.__init__(self, parent)
        self.parent = parent

        # ttk.Label(self, text="Rows:").grid(row=0, column=0)
        # ttk.Entry(self).grid(row=0, column=1)
        # ttk.Label(self, text="Columns:").grid(row=0, column=2)
        # ttk.Entry(self).grid(row=0, column=3)

        



class App(tk.Frame):
    def __init__(self, parent, controller, model: Model, *args, **kwargs) -> None:
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.controller = controller
        self.model = model

        Grid(self).pack(side='left', fill='both')
        ControlPanel(self).pack(side='right', padx=10, pady=10)

