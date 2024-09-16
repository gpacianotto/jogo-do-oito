from utils.tree.tree_node import TreeNode
from utils.move_predictor import MovePredictor

class Tree:
    def __init__(self, target:list[list[int]], layers:int):
        self.processor = MovePredictor(
            tabuleiro_state=target,
            layers=layers
        )
        self.root = TreeNode(target, self.processor, layers)
