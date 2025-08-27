# 🧠 Escopo Funcional — Sudoku com Python + HTML/CSS/JS


## 🔧 Backend (Python) — Responsável pela lógica do jogo

> [!NOTA]
> Arquivo principal: `sudoku_api.py`

### Estrutura

```python
matriz = [
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]], # 1º Vetor
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]], # 2º Vetor
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]], # 3º Vetor

    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]], # 4º Vetor
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]], # 5º Vetor
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]], # 6º Vetor

    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]], # 7º Vetor
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]], # 8º Vetor
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]], # 9º Vetor
    ]

# MATRIZ [] BRANCO
# VETOR [] ROSA
# LINHA [] AZUL

# EXIBIÇÃO
for contador_vetor, v in enumerate(matriz, start=1): # vai percorrer a matriz completa voltando com os vetores
    print(f'{contador_vetor}º Vetor:')
    print('[',end=' ')
    for contador_linhas, linhas in enumerate(v, start=1): # aqui ele vai percorrer as linhas dos vetores retornando com as linhas de cada um
        print(f'{contador_linhas}ª linha: ', end=' ')
        print(linhas, end='      ') if contador_linhas < 3 else print(linhas, end=' ') # vai printar todas as linhas das do vetor escolhido logo
        # FAZER MELHORIAS PARA PERCORRER LINHAS DE UMA FORMA MAIS FACIL
    print(']', end='\n\n')
    
    # print(v)
    if contador_vetor % 3 == 0:
        print('')
```

### 1. Gerar tabuleiro Sudoku (inicial)

- Função: 
```python
gerar_tabuleiro(dificuldade: str) -> list[list[int]]
```

- Objetivo: Gera uma matriz 9x9 com alguns números preenchidos conforme dificuldade (`fácil`, `médio`, `difícil`).

### 2. Validar movimento do jogador

- Função: 
```python
validar_jogada(tabuleiro: list[list[int]], linha: int, coluna: int, numero: int) -> bool
```

- Objetivo: Verifica se o número inserido é válido naquela posição (linha, coluna) de acordo com as regras do Sudoku.

### 3. Verificar se o tabuleiro está completo e correto

- Função: 
```python
tabuleiro_completo(tabuleiro: list[list[int]]) -> bool
```

- Objetivo: Retorna `True` se o tabuleiro está completamente preenchido e válido, `False` caso contrário.

### 4. Resolver Sudoku automaticamente (ajuda ou debug)

- Função: 
```python
resolver(tabuleiro: list[list[int]]) -> list[list[int]]
```

- Objetivo: Resolve o tabuleiro atual e retorna a solução (útil para dar “dica” ou checar erro do jogador).

### 5. Salvar e carregar progresso

- Função: 
```python
salvar_jogo(tabuleiro: list[list[int]]) -> None
```

- Função: 
```python
carregar_jogo() -> list[list[int]]
```

- Objetivo: Permite salvar o estado atual e carregar depois (simplesmente salvar em JSON local ou arquivo `.txt` com `json.dump/load`).

---

## 🌐 API Flask
- Endpoints REST que retornam JSON

| Rota      |   Método  |          Descrição            |
| ---       |   ---     |           ---                 |
|`/gerar`     |	GET	    |Gera um novo tabuleiro         |
|`/validar`   |	POST	|Valida uma jogada do jogador   |
|`/resolver`  |	POST	|Retorna a solução completa     |
|`/salvar`    |	POST	|Salva o estado atual do jogo   |
|`/carregar`  |	GET	    |Carrega o jogo salvo           |

---

## 🎨 Frontend (HTML/CSS/JS)

- HTML: Grid 9x9 com inputs (ou `divs` editáveis).

- CSS: Estilização do tabuleiro e níveis.

- JS:

    - Pega tabuleiro inicial da API (`/gerar`)

    - Envia jogadas para `/validar`

    - Se pedir ajuda, chama `/resolver`

    - Pode salvar e carregar progresso

## 🧩 Extras / Regras de Validação

- Um número é válido se:

    - Não existe na mesma linha

    - Não existe na mesma coluna

    - Não existe na mesma subgrade 3x3

Essas validações serão feitas usando listas e recortes de matrizes.

---

# 📁 Estrutura de Diretórios Sugerida

```bash
sudoku_project/
│
├── backend/
│   ├── sudoku_api.py
│   ├── logica.py  ← (funções separadas da API)
│   └── jogo_salvo.json
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── requirements.txt
└── README.md
```

---