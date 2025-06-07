# FloodFill - Colorindo regiões de um terreno com obstáculos

**Grupo:**
- Ana Carolina Caldas de Mello
- Gustavo Menezes
- Pedro Henrique Dias Camara

## Descrição do Projeto

Este projeto implementa um sistema de mapeamento inteligente usando o **Algoritmo Flood Fill** para identificar e colorir automaticamente regiões conectadas em um terreno bidimensional. O sistema foi desenvolvido para auxiliar robôs autônomos na identificação e classificação de áreas navegáveis em terrenos com obstáculos.

## Problema Resolvido

O sistema resolve o problema de **identificação e preenchimento de regiões conectadas** em um grid 2D, onde:
- **Células navegáveis (0)** representam terreno livre (branco)
- **Obstáculos (1)** representam barreiras que não podem ser atravessadas (preto)
- **Regiões coloridas (2, 3, 4...)** representam áreas mapeadas com cores distintas

O algoritmo identifica todas as células conectadas ortogonalmente (acima, abaixo, esquerda, direita) e as preenche com cores distintas, respeitando obstáculos e limites do grid.

## Algoritmo Flood Fill

O **Flood Fill** é um algoritmo de preenchimento que funciona de forma similar ao "balde de tinta" em editores de imagem. Nosso algoritmo:

1. **Inicia** em uma célula específica fornecida pelo usuário
2. **Identifica** todas as células navegáveis (valor 0) conectadas à célula inicial
3. **Preenche** essas células com uma cor específica (valores 2, 3, 4...)
4. **Procura** por novas regiões não preenchidas automaticamente
5. **Repete** o processo até que todo o terreno seja mapeado

### Como Funciona o Algoritmo:

#### 1. Inicialização
```python
def paint(self, visualizer=None):
    color = 2  # Primeira cor a ser usada
    self.grid[self.initialCoords] = color  # Marca célula inicial
    step = 1
    hasZero = True
```

#### 2. Preenchimento Recursivo
O algoritmo usa recursão para visitar todas as células conectadas:
```python
def paintGridRec(self, curentCoords, color, step):
    # Encontra vizinhos válidos (dentro dos limites e navegáveis)
    neighbours = [
        (curentCoords[0]+1, curentCoords[1]),  # Baixo
        (curentCoords[0]-1, curentCoords[1]),  # Cima
        (curentCoords[0], curentCoords[1]+1),  # Direita
        (curentCoords[0], curentCoords[1]-1)   # Esquerda
    ]
    
    # Para cada vizinho válido, preenche e chama recursivamente
    for neighbour in validNeighbours:
        self.grid[neighbour[0]][neighbour[1]] = color
        step += 1
        self.paintGridRec(neighbour, color, step)
```

#### 3. Busca por Novas Regiões
Após preencher uma região, o algoritmo procura automaticamente por novas áreas:
```python
while hasZero:
    hasZero = False
    for i in range(0, self.size):
        for k in range(0, self.size):
            if self.grid[i][k] == 0:  # Encontrou célula não preenchida
                color += 1  # Nova cor para nova região
                hasZero = True
                self.grid[i][k] = color
                self.paintGridRec((i,k), color, step)
```

### Características da Implementação:
- **Recursivo**: Utiliza chamadas recursivas para percorrer células adjacentes
- **Visualização passo a passo**: Mostra cada etapa do preenchimento
- **Cores distintas**: Cada região recebe uma cor automaticamente (2, 3, 4...)
- **Respeita obstáculos**: Não atravessa células com valor 1
- **Busca automática**: Localiza novas regiões automaticamente após completar uma área

## Como Executar o Projeto

### Pré-requisitos
- Python 3.6 ou superior
- Biblioteca NumPy
- Biblioteca Matplotlib (para visualização gráfica - opcional)

### Instalação das Dependências
```bash
# Instale as dependências necessárias
pip install numpy matplotlib
```

### Execução
```bash
python main.py
```

### Interação com o Sistema

1. **Digite as coordenadas iniciais**: 
   - Exemplo: `00` para começar na posição (0,0)
   - Exemplo: `12` para começar na posição (1,2)

2. **Digite o tamanho do terreno**: 
   - Exemplo: `5` para um grid 5x5

3. **Escolha o modo de construção**:
   - `1`: **Automático** (gera obstáculos aleatoriamente)
   - `2`: **Manual** (você define o terreno)

4. **Escolha visualização gráfica**: 
   - `s` para sim (abre janela gráfica)
   - `n` para não (apenas console)

#### Modo Automático
- Digite a porcentagem de chance de obstáculos (0-100)
- Exemplo: `30` para 30% de chance de cada célula ser um obstáculo

#### Modo Manual
- Digite uma string representando o terreno
- Cada dígito representa uma célula: `0` = navegável, `1` = obstáculo
- Exemplo para grid 5x5: `1100010010010101010000001`
- O sistema preenche da esquerda para direita, linha por linha

## Exemplos de Uso

### Exemplo 1: Grid 4x4 Manual

**Entrada:**
```
Digite as coordenadas iniciais: 00
Digite o tamanho do terreno: 4
Digite o modo de construir: 2
Digite o terreno de entrada: 0010011010110110
```

**Grid Inicial:**
```
0	0	1	0	
0	1	1	0	
1	0	1	1	
0	1	1	0	
```

**Processo de Preenchimento (alguns passos):**
```
-----------Step 1-----------
2	0	1	0	
0	1	1	0	
1	0	1	1	
0	1	1	0	

-----------Step 2-----------
2	2	1	0	
0	1	1	0	
1	0	1	1	
0	1	1	0	

-----------Step 3-----------
2	2	1	0	
2	1	1	0	
1	0	1	1	
0	1	1	0	
```

**Grid Final:**
```
2	2	1	3	
2	1	1	3	
1	4	1	1	
4	1	1	5	
```

### Exemplo 2: Grid 5x5 do Enunciado

**Entrada:**
```
Grid inicial:
0 0 1 0 0
0 1 1 0 0
0 0 1 1 1
1 1 0 0 0
Coordenadas iniciais: (0, 0)
```

**Grid Final:**
```
2 2 1 3 3
2 1 1 3 3
2 2 1 1 1
1 1 4 4 4
```

### Exemplo 3: Visualização Automática

**Entrada:**
```
Digite as coordenadas iniciais: 12
Digite o tamanho do terreno: 6
Deseja visualização gráfica? s
Digite o modo de construir: 1
Digite a porcentagem chance de um obstáculo: 25
```

O sistema gera um grid aleatório e mostra a visualização gráfica em tempo real.

## Visualizações Disponíveis

### 1. Console (Terminal)
- Saída textual colorida no terminal
- Cada número representa uma cor diferente
- Cores ANSI para melhor visualização

### 2. Gráfica (Matplotlib)
- Janela interativa com cores visuais
- Atualização em tempo real durante o preenchimento
- Salvamento automático em GIF (terrain_floodfill.gif)

### Legenda de Cores (Console)
- **0**: Branco (Terreno navegável)
- **1**: Preto (Obstáculo)
- **2**: Azul (Primeira região)
- **3**: Amarelo (Segunda região)
- **4**: Verde (Terceira região)
- **5**: Magenta (Quarta região)
- **6**: Rosa (Quinta região)
- **7**: Vermelho (Sexta região)
- **8**: Ciano (Sétima região)
- **9**: Verde claro (Oitava região)
- **10**: Azul escuro (Nona região)

## Estrutura do Projeto

```
fpaa-trabalho-em-grupo-2/
├── main.py                  # Interface principal do usuário
├── terrain.py               # Classe Terrain com algoritmo Flood Fill
├── terrain_visualizer.py    # Visualização gráfica (matplotlib)
└── README.md               # Documentação do projeto
```

### Arquivos do Projeto

#### `main.py` - Interface Principal
- Coleta entrada do usuário (coordenadas, tamanho, modo)
- Cria instância do terreno
- Executa visualização (console ou gráfica)
- Coordena execução do algoritmo

#### `terrain.py` - Algoritmo Core
- **Classe Terrain**: Implementação do algoritmo Flood Fill
- **`__init__()`**: Inicializa grid com numpy
- **`buildGridManual()`**: Constrói grid a partir de string de entrada
- **`buildGridAuto()`**: Gera grid com obstáculos aleatórios
- **`paint()`**: Método principal do Flood Fill
- **`paintGridRec()`**: Implementação recursiva do algoritmo
- **`printGrid()`**: Visualização colorida no console

#### `terrain_visualizer.py` - Visualização Gráfica
- **Classe TerrainVisualizer**: Interface gráfica com matplotlib
- **Visualização em tempo real**: Atualiza durante execução
- **Salvamento em GIF**: Gera animação do processo
- **Cores visuais**: Mapeamento de números para cores RGB

## Características Técnicas

- **Complexidade Temporal**: O(n×m) onde n e m são as dimensões do grid
- **Complexidade Espacial**: O(n×m) para o grid + O(k) para pilha de recursão
- **Linguagem**: Python 3.6+
- **Dependências**: NumPy (obrigatório), Matplotlib (opcional)
- **Visualização**: Console com cores ANSI + Interface gráfica matplotlib
- **Flexibilidade**: Suporta grids de qualquer tamanho quadrado

## Casos de Teste Suportados

O sistema foi testado e funciona corretamente com:
- ✅ Grids pequenos (3x3) e médios (10x10)
- ✅ Grids sem obstáculos (uma única região)
- ✅ Grids completamente bloqueados por obstáculos
- ✅ Grids com múltiplas regiões desconectadas
- ✅ Diferentes posições iniciais
- ✅ Modo manual e automático
- ✅ Visualização console e gráfica

## Exemplos de Entrada para Testes

### Teste 1: Grid Simples 3x3
```
Coordenadas: 00
Tamanho: 3
Modo: 2 (manual)
Terreno: 010101010
```

### Teste 2: Grid Complexo 5x5
```
Coordenadas: 22
Tamanho: 5  
Modo: 2 (manual)
Terreno: 1100010010010101010000001
```

### Teste 3: Grid Aleatório 7x7
```
Coordenadas: 33
Tamanho: 7
Modo: 1 (automático)
Chance de obstáculo: 20
```

## Contribuições

Este projeto foi desenvolvido como trabalho em grupo para a disciplina de **Fundamentos de Projeto e Análise de Algoritmos (FPAA)**, implementando o algoritmo Flood Fill de forma educativa e interativa, com foco no aprendizado prático de algoritmos de busca e preenchimento em estruturas de dados bidimensionais.