import tkinter as tk

CANVAS_MAX_WIDTH = 800
CANVAS_MAX_HEIGHT = 500
LINE_WIDTH = 3

class Grid(tk.Frame):
    def __init__(self, parent, n_rows, n_cols):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.n_rows = n_rows
        self.n_cols = n_cols
        self.cell_size = min(CANVAS_MAX_WIDTH / self.n_cols, CANVAS_MAX_HEIGHT / self.n_rows)
        self.width = self.cell_size * n_cols
        self.height = self.cell_size * n_rows

        self.canvas = tk.Canvas(self, width=self.width, height=self.height, borderwidth=3)

        self.canvas.pack()

        self.draw_grid()

    def draw_grid(self):
        # outline
        self.canvas.create_rectangle(6, 6, self.width, self.height, width=LINE_WIDTH)

        # draw vertical lines
        for i in range(1, self.n_rows):
            y = i * self.cell_size + LINE_WIDTH
            self.canvas.create_line(0, y, self.width, y, width=LINE_WIDTH)

        # draw horizontal lines
            for i in range(1, self.n_cols):
                x = i * self.cell_size
                self.canvas.create_line(x, 0, x, self.height, width=LINE_WIDTH)


class App(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.controller = controller

        self.grid = Grid(self, n_rows=5, n_cols=5)

        self.grid.pack(fill='both')


if __name__ == "__main__":
    root = tk.Tk()
    App(root, None).pack(side="top", fill="both", expand=True)
    root.mainloop()