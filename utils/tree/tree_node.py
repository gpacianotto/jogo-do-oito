from utils.move_predictor import MovePredictor
import copy

class TreeNode:
    def __init__(self, value:list[list[int]], processor:"MovePredictor",layer:int):
        self.processor = processor
        self.value:list[list[int]] = value 
        self.children:list[TreeNode]= []  # Array of child pointers
        self.layer = layer

        if self.layer > 0 :
            possible_moves = self.processor.getMovablePecas(self.value)

            for move in possible_moves:
                # print("value: ",self.value)
                # print("move: ", move)
                self.children.append(TreeNode(
                    value=self.processor.virtual_move(copy.deepcopy(move), copy.deepcopy(self.value)),
                    processor=processor,
                    layer=(copy.deepcopy(self.layer) - 1)
                ))
            pass

    def __str__(self):
        return f'Node(value={self.value},children={self.children})'
    
    def pre_order(self):
        if self.layer > 0:
            for child in self.children:
                print(child.value)
                child.pre_order()
                

        