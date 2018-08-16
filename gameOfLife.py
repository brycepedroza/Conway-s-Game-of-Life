import random
import pyglet


class Cell:

    def __init__(self, color, data):
        self.color = color
        self.status = data
        self.age = 0


    def getStatus(self):
        return self.status

    def ageCell(self):
        self.age += 1
        if self.age >= 4:
            self.age = 4

    def updateColor(self, color):
        self.color = color

class GameOfLife:

    def __init__(self, windowH, windowW, cellSize):
        self.gridW = int(windowW/cellSize)
        self.gridH = int(windowH/cellSize)
        self.cellSize = cellSize
        self.cells = []
        self.colorCount = 0


        # My Game of Life Rules
        self.generator = 0.35

        self.reproduce = 3
        self.reproduce2 = 6
        self.stasis = 2


        self.generateCells()



        # we are making a list of lists 0's are dead 1's are alive
    def generateCells(self):
        for row in range(0, self.gridH):
            self.cells.append([])
            for col in range(0, self.gridW):
                if random.random() < self.generator:
                    # newCell = Cell(self.colorSwitcher(self.colorCount),1)
                    newCell = Cell(self.colorSwitcher(0), 1)
                    self.cells[row].append(newCell)
                else:
                    # newCell = Cell(self.colorSwitcher(self.colorCount),0)
                    newCell = Cell(self.colorSwitcher(0), 0)
                    self.cells[row].append(newCell)



    def runRules(self):
        tempGrid = []
        for row in range(0, self.gridH):
            tempGrid.append([])
            for col in range(0, self.gridW):
                cellSum = sum([ self.getCellValue(row-1, col),
                                self.getCellValue(row-1, col-1),
                                self.getCellValue(row,   col-1),
                                self.getCellValue(row+1, col-1),
                                self.getCellValue(row+1, col),
                                self.getCellValue(row+1, col+1),
                                self.getCellValue(row,   col+1),
                                self.getCellValue(row-1, col+1),
                              ])


                # Top if is Standard Game of Life (23/3) Bottom if is HighLife Game of life (23/36)

                # if self.cells[row][col].getStatus() == 0 and cellSum == self.reproduce:
                if self.cells[row][col].status == 0 and (cellSum == self.reproduce or cellSum == self.reproduce2):
                        # newCell = Cell(self.colorSwitcher(self.colorCount),1)
                        newCell = Cell(self.colorSwitcher(0), 1)
                        tempGrid[row].append(newCell)
                elif self.cells[row][col].getStatus() == 1 and (cellSum == self.reproduce or cellSum == self.stasis):
                    self.cells[row][col].ageCell()
                    self.cells[row][col].updateColor(self.colorSwitcher(self.cells[row][col].age))
                    tempGrid[row].append(self.cells[row][col])
                else:
                    # newCell = Cell(self.colorSwitcher(self.colorCount),0)
                    newCell = Cell(self.colorSwitcher(0), 0)
                    tempGrid[row].append(newCell)
        self.cells = tempGrid


    def getCellValue(self, row, col):
        if row >= 0 and row < self.gridH and col >= 0 and col < self.gridW:
            return self.cells[row][col].getStatus()
        return 0



    def draw(self):
        for row in range(0, self.gridH):
            for col in range(0, self.gridW):
                myCell = self.cells[row][col]
                if myCell.getStatus() == 1:
                    sqaureCoordinates = (row * self.cellSize,                 col * self.cellSize,
                                         row * self.cellSize,                 col * self.cellSize + self.cellSize,
                                         row * self.cellSize + self.cellSize, col * self.cellSize,
                                         row * self.cellSize + self.cellSize, col * self.cellSize + self.cellSize)

                    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                                 [0, 1, 2, 1, 2, 3],
                                                 ('v2i', sqaureCoordinates),
                                                 ('c3B', self.cells[row][col].color)
                                                )
        if self.colorCount >= 5:
            self.colorCount = 0
        else:
            self.colorCount += 1


    def colorSwitcher(self, ticker):
        return {
            # Red
            0:(96, 103, 65,
               96, 103, 65,
               96, 103, 65,
               96, 103, 65),
            # Green
            1:(199, 186, 55,
               199, 186, 55,
               199, 186, 55,
               199, 186, 55),
            # Blue
            2:(190, 83, 18,
               190, 83, 18,
               190, 83, 18,
               190, 83, 18),
            # Magenta
            3: (190, 30, 34,
                190, 30, 34,
                190, 30, 34,
                190, 30, 34,),
            # Yellow
            4: (90, 0, 6,
                90, 0, 6,
                90, 0, 6,
                90, 0, 6),
        }[ticker]


