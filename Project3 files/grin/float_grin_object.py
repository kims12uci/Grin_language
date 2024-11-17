from grin.base_object_class import *
import grin.int_grin_object as intG

class floatGrinObj(grinObject):
    """
    Derived class of grinObject for float grin objects.
    Modified methods:
        init, lt, le
    Added methods:
        add, sub, mul, truediv
    """
    def __init__(self, value):
        """
        Initialize the object's value, ensuring the value is float.
        """
        super().__init__(float(value))

    def __add__(self, other):
        """
        Adds two grin objects with numerical value.
        If other is an intGrinObj or floatGrinObj, returns new floatGrinObj having summed value.
        Otherwise, raise runtimeError indicating types of self and other.
        """
        if (type(other) is intG.intGrinObj) or (type(other) is floatGrinObj):
            return floatGrinObj(self.value + other.value)
        else:
            raise runtimeError(f'Tried to add invalid types. Tried to add: {type(self).__name__} and {type(other).__name__}')

    def __sub__(self, other):
        """
        Subtracts two grin objects with numerical value.
        If other is an intGrinObj or floatGrinObj, returns new floatGrinObj having subtracted value.
        Otherwise, raise runtimeError indicating types of self and other.
        """
        if (type(other) is intG.intGrinObj) or (type(other) is floatGrinObj):
            return floatGrinObj(self.value - other.value)
        else:
            raise runtimeError(f'Tried to subtract invalid types. Tried to subtract: {type(self).__name__} and {type(other).__name__}')

    def __mul__(self, other):
        """
        Multiplies two grin objects with numerical value.
        If other is an intGrinObj or floatGrinObj, returns new floatGrinObj having multiplied value.
        Otherwise, raise runtimeError indicating types of self and other.
        """
        if (type(other) is intG.intGrinObj) or (type(other) is floatGrinObj):
            return floatGrinObj(self.value * other.value)
        else:
            raise runtimeError(f'Tried to multiply invalid types. Tried to multiply: {type(self).__name__} and {type(other).__name__}')

    def __truediv__(self, other):
        """
        Divides two grin objects with numerical value.
        If other is an intGrinObj or floatGrinObj, returns new floatGrinObj having divided value.
        If other is intGrinObj or floatGrinObj with value of 0, raise runtimeError with appropriate message.
        Otherwise, raise runtimeError indicating types of self and other.
        """
        if (type(other) is intG.intGrinObj) or (type(other) is floatGrinObj):
            if other.value == 0:
                raise runtimeError('Cannot divide by 0.')
            else:
                return floatGrinObj(self.value / other.value)
        else:
            raise runtimeError(f'Tried to divide invalid types. Tried to divide: {type(self).__name__} and {type(other).__name__}')
    
    def __lt__(self, other):
        """
        Modifies base class' lt method.
        if other is a intGrinObj, make it a floatGrinObj, keeping its value.
        """
        if type(other) is intG.intGrinObj:
            other = floatGrinObj(other.value)
        
        return super().__lt__(other)
    
    def __le__(self, other):
        """
        Modifies base class' le method.
        if other is a intGrinObj, make it a floatGrinObj, keeping its value.
        """
        if type(other) is intG.intGrinObj:
            other = floatGrinObj(other.value)
        
        return super().__le__(other)