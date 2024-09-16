import math
import copy
from utils.singleton_base import SingletonBase

class MovePredictor(SingletonBase):
    def __init__(self, tabuleiro_state:list[list[int]]) -> None:
        self
        self.state = tabuleiro_state

        

        self.winner_state = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

    def findPecaIndex(self, index:int, target:list[list[int]]):
        matrix = target
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == index:
                    return i, j

    def findPecaIndexAndNine(self, index, target:list[list[int]]):
        i9, j9 = self.findPecaIndex(index=9, target=target)
        i,j = self.findPecaIndex(index=index, target=target)

        return i, j, i9, j9

    def calculateDistance(self, i, j, i2, j2):
        return math.sqrt(((i - i2) ** 2) + ((j - j2) ** 2))

    def getDistanceToNine(self, index:int, target:list[list[int]]):
        i, j, i9, j9 = self.findPecaIndexAndNine(index, target=target)

        return self.calculateDistance(i=i, j=j, i2=i9, j2=j9)

    def isMovable(self, index:int, target:list[list[int]]):
        distance_to_nine = self.getDistanceToNine(index=index, target=target)

        if distance_to_nine > 1 :
            return False

        return True

    def swapPecas(self, i, j, i9, j9, target:list[list[int]]):

        pecas = target

        aux = pecas[i][j]

        pecas[i][j] = pecas[i9][j9]
        pecas[i9][j9] = aux

        target = pecas
        return target

    def virtual_move(self, index:int, target=list[list[int]]):

        buffer = target

        if self.isMovable(index=index, target=buffer):
            i, j, i9, j9 = self.findPecaIndexAndNine(index, target=buffer)
            buffer = self.swapPecas(i=i, j=j, i9=i9, j9=j9, target=buffer)
            return buffer
        return None

    def getMovablePecas(self, target:list[list[int]]) -> list[int]:

        result = [] 

        for rows in target:
            for peca in rows:
                distance_to_nine = self.getDistanceToNine(peca, target=target)
                if distance_to_nine == 1:
                    result.append(peca)

        return result

    def predict(self):
        pass