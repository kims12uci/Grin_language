from grin.base_object_class import *
import grin.int_grin_object as intG

class strGrinObj(grinObject):
    """
    Derived class of grinObject for string grin objects.
    Modified methods:
        init
    Added methods:
        add, mul
    """
    def __init__(self, value):
        """
        Initialize the object's value, ensuring the value is string.
        """
        super().__init__(str(value))

    def __add__(self, other):
        """
        Adds two string grin objects.
        If other is a strGrinObj, returns new strGrinObj having summed value.
        Otherwise, raise runtimeError indicating types of self and other.
        """
        if type(other) is strGrinObj:
            return strGrinObj(self.value[1:-1] + other.value[1:-1])
        else:
            raise runtimeError(f'Tried to add invalid types. Tried to add: {type(self).__name__} and {type(other).__name__}')

    def __mul__(self, other):
        """
        Multiplies a string grin object with an integer grin object.
        If other is an intGrinObj, returns new strGrinObj having value repeated appropriate times.
        Otherwise, raise runtimeError indicating types of self and other.
        """
        if type(other) is intG.intGrinObj:
            return strGrinObj(self.value[1:-1] * other.value)
        else:
            raise runtimeError(f'Tried to multiply invalid types. Tried to multiply: {type(self).__name__} and {type(other).__name__}')
