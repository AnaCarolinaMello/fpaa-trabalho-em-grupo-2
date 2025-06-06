import numpy, random

class Terrain:

    symbols = {
        0: "\033[0m", #Empty terrain
        1: "\033[0m", #Obstacle
        2: "\033[94m", #Blue
        3: "\033[96m", #Cyan
        4: "\033[92m", #Green
        5: "\033[1m", #Bold
        9: "\033[91m" #Error
    }


    def __init__(self, size = 5, initalCoords = (0,0)):
        self.size = size
        self.initialCoords = initalCoords
        self.grid = numpy.zeros((size, size))

        pass

    def buildGridManual(self):
        inputGrid = input("Digite o terreno de entrada:")
        iter = 0
        for i in range(0, self.size):
            for k in range(0, self.size):
                if(iter<inputGrid.__len__()):
                    if(int(inputGrid[iter]) in self.symbols):
                        self.grid[i][k] = inputGrid[iter]
                        iter += 1 
                    else: 
                        self.grid[i][k] = 9
                        iter += 1
                    
                else:
                    self.grid[i][k] = 9


    def printGrid(self):

        for i in range(0, self.size):
            for k in range(0, self.size):
                print(self.symbols[self.grid[i][k]] + str(int(self.grid[i][k])), end='')
                print('\t', end='')
            print('\n', end='')

    def paint(self):
        firstColor = random.randrange(2,4)
        usedColors = {firstColor}
        self.grid[self.initialCoords] = firstColor
        step = 1

        self.paintGridRec(self.initialCoords, firstColor, step)

    def paintGridRec(self, curentCoords, color, step):

        print(f'-----------Step {step}-----------')
        self.printGrid()
        print()

        neighbours = [
            (curentCoords[0]+1, curentCoords[1]),
            (curentCoords[0]-1, curentCoords[1]),
            (curentCoords[0], curentCoords[1]+1),
            (curentCoords[0], curentCoords[1]-1)
        ]

        validNeighbours = []

        for neighbour in neighbours:
            if(neighbour[0] < self.size and neighbour[1]< self.size and neighbour[0]>=0 and neighbour[1]>=0):
                if(self.grid[neighbour[0]][neighbour[1]] == 0):
                    validNeighbours.append(neighbour)

        
        for neighbour in validNeighbours:
            self.grid[neighbour[0]][neighbour[1]] = color
            step+=1
            self.paintGridRec(neighbour,color,step)