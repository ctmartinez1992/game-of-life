import pyxel


neighbours_indexes = [-1, 0, 1]


class GameOfLife:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        self.n_cols = width // cell_size
        self.n_rows = height // cell_size

        self.grid = [[False for _ in range(self.n_cols)] for _ in range(self.n_rows)]
        self.initialize_grid()

    def initialize_grid(self):
        self.grid[60][60] = True
        self.grid[60][61] = True
        
        self.grid[61][59] = True
        self.grid[61][60] = True
        self.grid[61][61] = True
        self.grid[61][62] = True
        
        self.grid[63][58] = True
        self.grid[63][59] = True
        self.grid[63][60] = True
        self.grid[63][61] = True
        self.grid[63][62] = True
        self.grid[63][63] = True
        
        self.grid[64][59] = True
        self.grid[64][60] = True
        self.grid[64][61] = True
        self.grid[64][62] = True

        self.grid[66][58] = True
        self.grid[66][59] = True
        self.grid[66][62] = True
        self.grid[66][63] = True

        self.grid[67][56] = True
        self.grid[67][57] = True
        self.grid[67][59] = True
        self.grid[67][62] = True
        self.grid[67][64] = True
        self.grid[67][65] = True

        self.grid[68][59] = True
        self.grid[68][62] = True

        self.grid[70][60] = True
        self.grid[70][61] = True

        self.grid[71][60] = True
        self.grid[71][61] = True

    def update(self):
        new_grid = [[False for _ in range(self.n_cols)] for _ in range(self.n_rows)]
        for row in range(self.n_rows):
            for col in range(self.n_cols):
                live_neighbors = self.count_live_neighbors(row, col)
                if self.grid[row][col]:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[row][col] = False
                    else:
                        new_grid[row][col] = True
                else:
                    if live_neighbors == 3:
                        new_grid[row][col] = True
        self.grid = new_grid

    def count_live_neighbors(self, row, col):
        count = 0
        for i in neighbours_indexes:
            for j in neighbours_indexes:
                if i == 0 and j == 0:
                    continue
                neighbor_row = (row + i + self.n_rows) % self.n_rows
                neighbor_col = (col + j + self.n_cols) % self.n_cols
                if self.grid[neighbor_row][neighbor_col]:
                    count += 1
        return count

    def draw(self):
        for row in range(self.n_rows):
            for col in range(self.n_cols):
                if self.grid[row][col]:
                    pyxel.rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size, 9)

class App:
    def __init__(self):
        self.game = GameOfLife(128, 128, 1)
        pyxel.init(self.game.width, self.game.height, fps=10)

    def update(self):
        self.game.update()

    def draw(self):
        pyxel.cls(0)
        self.game.draw()

    def run(self):
        pyxel.run(self.update, self.draw)

app = App()
app.run()