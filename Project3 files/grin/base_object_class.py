class runtimeError(Exception):
    """
    A custom exception storing its reason for being raised.
    Will be handled in project3 module.
    """
    def __init__(self, reason):
        self.reason = reason
class grinObject:
    """
    Base class for grin objects.
    """
    def __init__(self, value):
        """
        Initialize the object's value.
        """
        self.value = value

    def __hash__(self):
        """
        Define hash value.
        """
        return hash(self.value)

    def __eq__(self, other) -> bool:
        """
        Define eq method.
        If other is an instance of grinObject, return True if self has same value as it.
        Otherwise, return False.
        """
        if isinstance(other, grinObject):
            return self.value == other.value
        else:
            return False

    def __lt__(self, other) -> bool:
        """
        Define lt method.
        If type of self and other are the same, return True if self has less value than the other, False if not.
        Otherwise, raise runtimeError with an error message indicating types of self and the other.
        """
        if type(self) == type(other):
            return self.value < other.value
        else:
            raise runtimeError(f'Cannot compare objects of different types. Tried to compare: {type(self).__name__} and {type(other).__name__}')

    def __le__(self, other) -> bool:
        """
        Define le method.
        If type of self and other are the same, return True if self has less or equal value than the other, False if not.
        Otherwise, raise runtimeError with an error message indicating types of self and the other.
        """
        if type(self) == type(other):
            return self.value <= other.value
        else:
            raise runtimeError(f'Cannot compare objects of different types. Tried to compare: {type(self).__name__} and {type(other).__name__}')

    def __repr__(self) -> str:
        """
        Define class object's representation.
        Returns its type followed by its value.
        """
        return self.value
