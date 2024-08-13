

class InstanceManager:

    # essa classe pode ser útil no futuro para salvar estados globais

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

