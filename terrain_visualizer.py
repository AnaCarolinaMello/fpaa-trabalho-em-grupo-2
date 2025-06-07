import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.animation as animation
import numpy as np
import time
from PIL import Image
import io

class TerrainVisualizer:
    """Visual interface for FloodFill terrain coloring"""
    
    # Colors for visual display
    visual_colors = {
        0: 'white',      # Empty terrain - navigable
        1: 'black',      # Obstacle
        2: 'red',        # First filled region
        3: 'orange',     # Second filled region  
        4: 'yellow',     # Third filled region
        5: 'green',      # Fourth filled region
        6: 'blue',       # Fifth filled region
        7: 'purple',     # Sixth filled region
        8: 'cyan',       # Seventh filled region
        9: 'magenta',    # Eighth filled region
        10: 'brown',     # Ninth filled region
    }
    
    def __init__(self, terrain_obj):
        """Initialize visualizer with a terrain object"""
        self.terrain = terrain_obj
        self.fig = None
        self.ax = None
        self.im = None
        self.frames = []  # Store PIL Images for gif
        self.setup_visual()
    
    def setup_visual(self):
        """Setup matplotlib figure for visual display"""
        self.fig, self.ax = plt.subplots(figsize=(10, 8))
        self.ax.set_title('FloodFill - Terrain Coloring Visualization')
        self.ax.set_xticks(range(self.terrain.size))
        self.ax.set_yticks(range(self.terrain.size))
        self.ax.grid(True, linewidth=2, color='gray')
        
        # Create initial display
        self.update_display()
    
    def get_color_map(self):
        """Create a color map for the grid values"""
        # Get the maximum value in grid to create proper range
        max_val = int(np.max(self.terrain.grid))
        
        # Create colors list for values 0 to max_val
        colors = []
        for val in range(max_val + 1):
            if val in self.visual_colors:
                colors.append(self.visual_colors[val])
            else:
                # Generate consistent color for values beyond predefined
                np.random.seed(val)  # Consistent color for same value
                colors.append(np.random.rand(3,))
        
        cmap = mcolors.ListedColormap(colors)
        return cmap, max_val
    
    def update_display(self):
        """Update the visual display with current grid state"""
        self.ax.clear()
        self.ax.set_title('FloodFill - Terrain Coloring Visualization')
        
        # Create color mapping
        display_grid = self.terrain.grid.copy()
        
        # Create custom colormap
        cmap, max_val = self.get_color_map()
        
        # Display the grid
        im = self.ax.imshow(display_grid, cmap=cmap, vmin=0, vmax=max_val)
        
        # Add grid lines
        self.ax.set_xticks(np.arange(-0.5, self.terrain.size, 1), minor=True)
        self.ax.set_yticks(np.arange(-0.5, self.terrain.size, 1), minor=True)
        self.ax.grid(which="minor", color="gray", linestyle='-', linewidth=2)
        self.ax.tick_params(which="minor", size=0)
        
        # Add text annotations
        for i in range(self.terrain.size):
            for j in range(self.terrain.size):
                val = int(self.terrain.grid[i, j])
                color = 'white' if val == 1 else 'black'  # Black text on white, white text on black
                self.ax.text(j, i, str(val), ha='center', va='center', 
                           fontsize=12, fontweight='bold', color=color)
        
        # Highlight initial coordinates
        self.ax.add_patch(plt.Circle((self.terrain.initialCoords[1], self.terrain.initialCoords[0]), 0.3, 
                                   color='red', fill=False, linewidth=3))
        
        self.ax.set_xticks(range(self.terrain.size))
        self.ax.set_yticks(range(self.terrain.size))
        
        plt.pause(0.5)  # Pause to show animation
        plt.draw()
    
    def show_initial_state(self):
        """Show the initial terrain state"""
        self.ax.set_title('FloodFill - Initial Terrain')
        self.update_display()
        self.capture_frame()  # Capture frame for gif
        print("=== TERRENO INICIAL ===")
        self.terrain.printGrid()
    
    def show_step(self, step_num):
        """Show a step in the flood fill process"""
        self.ax.set_title(f'FloodFill - Step {step_num}')
        self.update_display()
        self.capture_frame()  # Capture frame for gif
    
    def show_final_result(self):
        """Show final colored result"""
        self.ax.set_title('FloodFill - Final Result')
        self.update_display()
        self.capture_frame()  # Capture frame for gif
        
        print("\n=== RESULTADO FINAL ===")
        self.terrain.printGrid()
        print("\nLegenda:")
        print("0 - Branco (Terreno navegável)")
        print("1 - Preto (Obstáculo)") 
        print("2 - Vermelho (Primeira região)")
        print("3 - Laranja (Segunda região)")
        print("4 - Amarelo (Terceira região)")
        print("5+ - Outras cores para regiões adicionais")
        
        plt.show()
    
    def capture_frame(self):
        """Capture current state as PIL Image for gif creation"""
        # Save figure to bytes buffer
        buf = io.BytesIO()
        self.fig.savefig(buf, format='png', bbox_inches='tight', dpi=100)
        buf.seek(0)
        
        # Convert to PIL Image
        img = Image.open(buf)
        self.frames.append(img.copy())
        buf.close()
    
    def save_gif(self, filename='terrain_floodfill.gif', duration=1500):
        """Save captured frames as animated gif"""
        if not self.frames:
            print("Nenhum frame capturado. Use capture_frame() durante a visualização.")
            return
        
        # Save as animated GIF
        try:
            self.frames[0].save(
                filename,
                save_all=True,
                append_images=self.frames[1:],
                duration=duration,
                loop=0
            )
            print(f"GIF salvo como: {filename}")
            print(f"Frames capturados: {len(self.frames)}")
        except Exception as e:
            print(f"Erro ao salvar GIF: {e}")
            print("Certifique-se de ter o Pillow instalado: pip install Pillow")
    
    def close(self):
        """Close the visualization window"""
        if self.fig:
            plt.close(self.fig)