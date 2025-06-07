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

    def find_nearest_navigable(self, start_coords):
        """Find the nearest navigable position (0) from start_coords using BFS"""
        from collections import deque
        
        # If current position is already navigable, return it
        if self.grid[start_coords[0]][start_coords[1]] == 0:
            return start_coords
        
        # BFS to find nearest navigable cell
        queue = deque([start_coords])
        visited = set([start_coords])
        
        while queue:
            current = queue.popleft()
            
            # Check all 4 directions
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            for dx, dy in directions:
                new_x, new_y = current[0] + dx, current[1] + dy
                
                # Check bounds
                if (0 <= new_x < self.size and 0 <= new_y < self.size and 
                    (new_x, new_y) not in visited):
                    
                    visited.add((new_x, new_y))
                    
                    # If found navigable cell, return it
                    if self.grid[new_x][new_y] == 0:
                        return (new_x, new_y)
                    
                    queue.append((new_x, new_y))
        
        # If no navigable cell found (shouldn't happen in normal cases)
        return start_coords

    def paint(self, visualizer=None):
        # Check if initial position is an obstacle
        if self.grid[self.initialCoords[0]][self.initialCoords[1]] == 1:
            print(f"⚠️  Posição inicial ({self.initialCoords[0]}, {self.initialCoords[1]}) é um obstáculo!")
            new_coords = self.find_nearest_navigable(self.initialCoords)
            print(f"✅ Posição mais próxima navegável encontrada: ({new_coords[0]}, {new_coords[1]})")
            self.initialCoords = new_coords
        
        color = 2
        self.grid[self.initialCoords] = color
        step = 1
        hasZero = True

        self.paintGridRec(self.initialCoords, color, step, visualizer)

        while hasZero:
            hasZero=False
            for i in range(0, self.size):
                for k in range(0, self.size):
                    if self.grid[i][k]==0:
                        color+=1
                        hasZero=True
                        self.grid[i][k] = color
                        self.paintGridRec((i,k), color, step, visualizer)

    def paintGridRec(self, curentCoords, color, step, visualizer=None):

        print(f'-----------Step {step}-----------')
        self.printGrid()
        print()

        # Update visual if visualizer is provided
        if visualizer:
            visualizer.show_step(step)

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
            self.paintGridRec(neighbour,color,step,visualizer)

    def show_final_result(self):
        """Show final result in console"""
        print("\n=== RESULTADO FINAL ===")
        self.printGrid()
        print("\nLegenda:")
        print("0 - Branco (Terreno navegável)")
        print("1 - Preto (Obstáculo)") 
        print("2 - Vermelho (Primeira região)")
        print("3 - Laranja (Segunda região)")
        print("4 - Amarelo (Terceira região)")
        print("5+ - Outras cores para regiões adicionais")