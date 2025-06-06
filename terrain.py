import numpy, random

class Terrain:

    symbols = {
        0: "\033[0m", #Empty terrain
        1: "\033[0m", #Obstacle
        2: "\033[94m", 
        3: "\033[33m", 
        4: "\033[92m", 
        5: "\033[35m", 
        6: "\033[95m",  
        7: "\033[31m", 
        8: "\033[36m", 
        9: "\033[92m", 
        10: "\033[34m",
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
                        self.grid[i][k] = 0
                        iter += 1
                    
                else:
                    self.grid[i][k] = 0

    def buildGridAuto(self):
        inputChance = input("Digite a porcentagem chance de um obstáculo:")
        for i in range(0, self.size):
            for k in range(0, self.size):
                if(random.randint(0,99)<int(inputChance)):
                    self.grid[i][k] = 1

    def printGrid(self):

        for i in range(0, self.size):
            for k in range(0, self.size):
                if(int(self.grid[i][k])<self.symbols.__len__()):
                    print(self.symbols[self.grid[i][k]] + str(int(self.grid[i][k])), end='')
                else:
                    print(str(int(self.grid[i][k])), end='')
                print('\t', end='')
            print('\n', end='')

    def paint(self):
        color = 2
        self.grid[self.initialCoords] = color
        step = 1
        hasZero = True

        self.paintGridRec(self.initialCoords, color, step)

        while hasZero:
            hasZero=False
            for i in range(0, self.size):
                for k in range(0, self.size):
                    if self.grid[i][k]==0:
                        color+=1
                        hasZero=True
                        self.grid[i][k] = color
                        self.paintGridRec((i,k), color, step)

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