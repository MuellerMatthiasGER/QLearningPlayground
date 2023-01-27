import tkinter as tk
from tkinter import ttk
from model import Model
import shapes

CANVAS_MAX_WIDTH = 800
CANVAS_MAX_HEIGHT = 500
LINE_WIDTH = 3

class App(tk.Frame):
    def __init__(self, parent, controller, model: Model, *args, **kwargs) -> None:
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.controller = controller
        self.model = model

        self.grid = Grid(self)
        self.grid.pack(side='left', fill='both')

        ControlPanel(self).pack(side='right', padx=10, pady=10)

    def update(self):
        self.grid.draw()

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

    # TODO: check what actually needs be drawn each step
    def draw(self):
        self.canvas.delete('all')

        self.draw_tiles()
        self.draw_agent()
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

    def draw_agent(self):
        agent = self.parent.model.agent
        self.draw_figure(agent.y, agent.x, dash=None)
        self.draw_figure(agent.prev_y, agent.prev_x, dash=(5, 3))

    def draw_figure(self, y, x, dash):
        center_x = (x + 0.5) * self.cell_size
        center_y = (y + 0.5) * self.cell_size 
        radius = self.cell_size * 0.3
        self.canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, width=LINE_WIDTH * 2, outline='purple', dash=dash)

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
    def __init__(self, parent: App) -> None:
        tk.Frame.__init__(self, parent)
        self.parent = parent

        # ttk.Label(self, text="Rows:").grid(row=0, column=0)
        # ttk.Entry(self).grid(row=0, column=1)
        # ttk.Label(self, text="Columns:").grid(row=0, column=2)
        # ttk.Entry(self).grid(row=0, column=3)

        next_step_button = ttk.Button(self, text="Next Step", command=self.parent.controller.next_step)
        next_iter_button = ttk.Button(self, text="Next Iteration", command=lambda: self.parent.controller.execute_n_iterations(1))
        next_thousand_button = ttk.Button(self, text="1000 Iteration", command=lambda: self.parent.controller.execute_n_iterations(1000))


        ttk.Button(self, text="Show Q", command=lambda: print(self.parent.controller.model.agent.qtable)).pack()
        ttk.Button(self, text="Show me baby", command=self.parent.controller.model.agent.reset_epsilon).pack()


        next_step_button.pack(side='top')
        next_iter_button.pack(side='top')
        next_thousand_button.pack(side='top')

