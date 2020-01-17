class Sudoku:

    def __init__(self, size=4):
        self.size = size
        self.count = 0
        if size == 4:
            self.file = open("solutions.txt", "w")
        if size != 4 and size != 6:
            raise ValueError("Not supported size - 4 and 6 are allowed")

    def check_grid(self, grid):
        for row in range(0, self.size):
            for col in range(0, self.size):
                if grid[row][col] == 0:
                    return False
        return True

    def print_grid(self, grid):
        for row in range(0, 4):
            for col in range(0, 4):
                if col == 1:
                    self.file.write("{} | ".format(grid[row][col]))
                else:
                    self.file.write("{} ".format(grid[row][col]))
            if row == 1:
                self.file.write(" \n- - - - - ")
            self.file.write("\n")
        self.file.write("\n")


    def solve_grid(self, grid):

        if self.size == 4:
            self.solve_grid_2(grid)
        elif self.size == 6:
            self.solve_grid_3(grid)

    def solve_grid_2(self, grid):
        for i in range(0, 16):
            row = i // 4
            col = i % 4
            if grid[row][col] == 0:
                for value in range(1, 5):
                    if not (value in grid[row]):
                        if value not in (
                                grid[0][col], grid[1][col], grid[2][col], grid[3][col]):
                            if row < 2:
                                if col < 2:
                                    square = [grid[i][0:2] for i in range(0, 2)]
                                else:
                                    square = [grid[i][2:4] for i in range(0, 2)]
                            else:
                                if col < 2:
                                    square = [grid[i][0:2] for i in range(2, 4)]
                                else:
                                    square = [grid[i][2:4] for i in range(2, 4)]
                            if value not in (square[0] + square[1]):
                                grid[row][col] = value
                                if self.check_grid(grid):
                                    self.print_grid(grid)
                                    self.count = self.count + 1
                                else:
                                    if self.solve_grid(grid):
                                        self.file.close()
                                        return True
                break
        grid[row][col] = 0

    def solve_grid_3(self, grid):
        for i in range(0, 36):
            row = i // 6
            col = i % 6
            if grid[row][col] == 0:
                for value in range(1, 7):
                    if not (value in grid[row]):
                        if value not in (
                                grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col], grid[5][col]):
                            if row < 3:
                                if col < 2:
                                    square = [grid[i][0:2] for i in range(0, 3)]
                                elif col < 4:
                                    square = [grid[i][2:4] for i in range(0, 3)]
                                else:
                                    square = [grid[i][4:6] for i in range(0, 3)]
                            else:
                                if col < 2:
                                    square = [grid[i][0:2] for i in range(3, 6)]
                                elif col < 4:
                                    square = [grid[i][2:4] for i in range(3, 6)]
                                else:
                                    square = [grid[i][4:6] for i in range(3, 6)]
                            if value not in (square[0] + square[1] + square[2]):
                                grid[row][col] = value
                                if self.check_grid(grid):
                                    self.count = self.count + 1
                                else:
                                    if self.solve_grid(grid):
                                        return True
                break
        grid[row][col] = 0


if __name__ == "__main__":
    print("\n13.4")
    grid4 = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    sudoku4 = Sudoku(4)
    sudoku4.solve_grid(grid4)
    print("Number of 4x4 solutions: {}".format(sudoku4.count))
    print("Solutions saved to file solutions.txt")

    print("\n13.5")
    print("Solving sudoku 6x6 can take a while. Please wait. Output will be 28200960")
    grid6 = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]]
    sudoku6 = Sudoku(6)
    sudoku6.solve_grid(grid6)
    print("Number of 6x6 solutions 6: {}".format(sudoku6.count))
