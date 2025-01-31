class TypeVar:
    def __init__(self, value, var_type):
        if not isinstance(value, var_type):
            raise TypeError(f"Expected type {var_type.__name__}, got {type(value).__name__}")
        self._value = value
        self._type = var_type

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, self._type):
            raise TypeError(f"Cannot change variable type from {self._type.__name__} to {type(new_value).__name__}")
        self._value = new_value

    @property
    def type(self):
        return self._type

    def __repr__(self):
        return f'TypedVariable(value={self._value}, type={self._type.__name__})'