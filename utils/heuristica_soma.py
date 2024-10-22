from utils.tree.tree import Tree
from utils.move_predictor import MovePredictor
from copy import deepcopy
from utils.move_history import MoveHistory
import random
class HeuristicaSoma():

    def __init__(self, tabuleiro_state: list[list[int]], layers:int) -> None:
        self.tabuleiro_state = tabuleiro_state
        self.layers = layers
        self.move_predictor:MovePredictor = MovePredictor()
        pass

    def solve(self):

        try:
            tree = Tree(self.tabuleiro_state, layers=self.layers)

            return tree.busca_em_largura()
        except ValueError:
            possible_moves = self.move_predictor.getMovablePecas(deepcopy(self.tabuleiro_state))
            

            return random.choice(possible_moves)
        except:
            return -1
