from utils.move_predictor import MovePredictor
import copy
from utils.move_history import MoveHistory

class TreeNode:
    def __init__(self, value:list[list[int]], processor:"MovePredictor",layer:int, parent_move:int=0, parent_moves:list[int]=[]):
        self.processor = processor
        self.value:list[list[int]] = value 
        self.children:list[TreeNode]= []  # Array of child pointers
        self.layer = layer
        self.parent_move = parent_move
        self.parent_moves = copy.deepcopy(parent_moves)
        self.parent_moves.append(parent_move)

        self.soma = self.calculate_soma(self.value)

        if self.layer > 0 :
            possible_moves = self.get_possible_moves()

            for move in possible_moves:
                
                virtual_move = self.processor.virtual_move(copy.deepcopy(move), copy.deepcopy(self.value))

                # fazer condição para ver se virtual_move é repetido

                moveHistory = MoveHistory()

                if not moveHistory.state_exists(virtual_move):
                    self.children.append(TreeNode(
                        value=virtual_move,
                        processor=processor,
                        layer=(copy.deepcopy(self.layer) - 1),
                        parent_move=copy.deepcopy(move),
                        parent_moves=copy.deepcopy(self.parent_moves)
                    ))
            pass
    
    def get_possible_moves(self):
        return self.processor.getMovablePecas(self.value)
    
    def __str__(self):
        return f'Node(value={self.value},children={self.children})'
    
    def do_nothing():
        pass
    
    def calculate_soma(self, target:list[list[int]]):
        winner_position = self.processor.winner_state

        soma = 0

        for i in range(len(target)):
            for j in range(len(target)):
                soma = soma + pow(base=(target[i][j] - winner_position[i][j]), exp=2)
        
        return soma


    # def find_minor_move(self):
    #     if self.layer > 0:
    #         if self.layer == 1:
                
    #         for child in self.children:
    #             child.find_minor_move()

    def pre_order(self, action:callable=do_nothing):
        if self.layer > 0:
            for child in self.children:
                print(child.value, " camada: ", child.layer, " parent_move: ", child.parent_move, " soma: ", child.soma)
                action()
                child.pre_order()
                

        