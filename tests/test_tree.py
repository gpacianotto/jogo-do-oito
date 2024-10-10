from utils.tree.tree import Tree

tabuleiro_ficticio = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Tree: Classe que gera uma árvore de possibilidades dado um tabuleiro
# target: é uma matriz com a posição do tabuleiro
# layers: é a quantidade de camadas que a árvore é gerada

# Exemplo de uso:
tree = Tree(target=tabuleiro_ficticio, layers=2)

tree.root.pre_order()
