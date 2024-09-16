from utils import move_predictor
class heuristica_soma(move_predictor.MovePredictor):
    def __init__(self, tabuleiro_state: list[list[int]], layers:int) -> None:
        super().__init__(tabuleiro_state, layers)
        pass

    def predict(self):
        pass