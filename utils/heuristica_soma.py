from utils.tree.tree import Tree
from utils.move_predictor import MovePredictor
class HeuristicaSoma():

    def __init__(self, tabuleiro_state: list[list[int]], layers:int) -> None:
        self.tabuleiro_state = tabuleiro_state
        self.layers = layers
        self.move_predictor:MovePredictor = MovePredictor()
        pass

    def solve(self):
        tree = Tree(self.tabuleiro_state, layers=self.layers)

        # tree.root.pre_order()
        # print("----")

        return tree.busca_em_largura()