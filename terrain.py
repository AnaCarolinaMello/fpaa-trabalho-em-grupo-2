import numpy

class Terrain:


    symbols = {
        0: "", #Empty terrain
        1: "\033[1m", #Obstacle
        2: "\033[94m", #Blue
        3: "\033[96m", #Cyan
        4: "\033[92m", #Green
        5: "\033[1m", #Bold
        9: "\033[91m" #Error
    }


    def __init__(self, height = 5, width = 5 , initalCoords = (0,0)):
        self.height = height
        self.width = width
        self.initialCoords = initalCoords
        self.grid = numpy.zeros((height, width))

        pass

    def buildGridManual(self):
        inputGrid = input("Digite o terreno de entrada:")
        iter = 0
        for i in range(0, self.height):
            for k in range(0, self.width):
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
        print(self.grid)

        for i in range(0, self.height):
            for k in range(0, self.width):
                print(self.symbols[self.grid[i][k]] + str(int(self.grid[i][k])), end='')
                print('\t', end='')
            print('\n', end='')


