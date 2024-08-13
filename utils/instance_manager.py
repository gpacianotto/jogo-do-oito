

class InstanceManager:
    _instance = None
    _state = {}

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(InstanceManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def set_state(self, key, value):
        """Set the state for a given key."""
        self._state[key] = value

    def get_state(self, key):
        """Get the state for a given key."""
        return self._state.get(key, None)

    def reset_state(self):
        """Reset all states."""
        self._state.clear()

    def __str__(self):
        return f"StateManager(state={self._state})"

# Example usage:
# state_manager = StateManager()
# state_manager.set_state('user', 'Alice')
# print(state_manager.get_state('user'))
# state_manager.reset_state()
# print(state_manager)
