import terrain
import terrain_visualizer

print("=== FLOODFILL - COLORINDO REGIÕES DE TERRENO ===\n")

coords = input("Digite as coordenadas iniciais (ex: 00 para (0,0)): ")
size = int(input("Digite o tamanho do terreno: "))
buildMode = input("Digite o modo de construir o terreno (1 para automático, 2 para manual): ")

terrain_obj = terrain.Terrain(initalCoords=(int(coords[0]), int(coords[1])), size=size)

print("\n=== CONSTRUINDO TERRENO ===")

if int(buildMode) == 2:
    print("Modo Manual: Digite o terreno como uma sequência de números")
    print("0 = Terreno navegável, 1 = Obstáculo")
    print(f"Exemplo para grid {size}x{size}: {'0' * (size*size)}")
    terrain_obj.buildGridManual()
else:
    print("Modo Automático: Gerando obstáculos aleatoriamente")
    terrain_obj.buildGridAuto()

print("\n=== TERRENO INICIAL ===")
terrain_obj.printGrid()

# Ask for visual mode after terrain is built
visual_mode = input("\nDeseja visualização gráfica? (s/n): ").lower().strip() == 's'

# Create visualizer if requested
visualizer = None
if visual_mode:
    visualizer = terrain_visualizer.TerrainVisualizer(terrain_obj)
    print("Visualização gráfica ativada - observe a janela que abriu!")
    print("As cores serão preenchidas automaticamente conforme o algoritmo executa.")
    visualizer.show_initial_state()

print(f"\n=== INICIANDO FLOODFILL A PARTIR DE ({terrain_obj.initialCoords[0]}, {terrain_obj.initialCoords[1]}) ===")

terrain_obj.paint(visualizer)

# Show final result
if visual_mode:
    visualizer.show_final_result()
    
    # Save GIF after visualization is complete
    print("\n=== SALVANDO GIF ===")
    visualizer.save_gif('terrain_floodfill.gif', duration=2000)
    print("GIF salvo! Feche a janela para continuar...")
    visualizer.close()
else:
    terrain_obj.show_final_result()