from utils.singleton_base import SingletonBase

class MoveHistory(SingletonBase):

    def __init__(self):
        self.history:list[list[list[int]]] = []

    def registrate(self, state:list[list[int]]):
        self.history.append(state)
    
    def state_exists(self, state: list[list[int]]) -> bool:
        """Checks if the given state is already in the history."""
        return any(self._compare_states(existing_state, state) for existing_state in self.history)

    def _compare_states(self, state1: list[list[int]], state2: list[list[int]]) -> bool:
        """Compares two 2D states for equality."""
        return state1 == state2  # Python allows direct list comparison
    
    def clear_history(self):
        """Clears all the history."""
        self.history = []