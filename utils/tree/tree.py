from utils.tree.tree_node import TreeNode
from utils.move_predictor import MovePredictor
from collections import deque
class Tree:
    def __init__(self, target:list[list[int]], layers:int):
        self.processor = MovePredictor(
            tabuleiro_state=target
        )
        self.layers = layers
        self.root = TreeNode(target, self.processor, layers)

        self.possible_moves = self.root.get_possible_moves()
    
    def busca_em_largura(self):
        if self.root.soma == 0:
            return -1
        if self.root is None:
            return -1
        
        queue = deque([self.root])

        finalNodes:list[TreeNode] = []

        while queue:
            node = queue.popleft()

            print(node.value," layer ", node.layer, " soma: ", node.soma, " par_mov ", node.parent_moves)

            if node.layer == 0:
                finalNodes.append(node)

            for child in node.children:
                queue.append(child)
        
        smallestValue = min(finalNodes, key=lambda x: getattr(x, "soma"))

        
        return smallestValue.parent_moves[1]

