from grin.base_object_class import *
import grin.float_grin_object as fl
import grin.str_grin_object as sr

class intGrinObj(grinObject):
    """
    Derived class of grinObject for integer grin objects.
    Modified methods:
        init, lt, le
    Added methods:
        add, sub, mul, truediv
    """
    def __init__(self, value):
        """
        Initialize the object's value, ensuring the value is integer.
        """
        super().__init__(int(value))

    def __add__(self, other):
        """
        Adds two grin objects with numerical value.
        If other is an intGrinObj, returns new intGrinObj having summed value.
        If other is a floatGrinObj, returns new floatGrinObj having summed value.
        Otherwise, raise runtimeError indicating types of self and other.
        """
        if type(other) is intGrinObj:
            return intGrinObj(self.value + other.value)
        elif type(other) is fl.floatGrinObj:
            return fl.floatGrinObj(float(self.value) + other.value)
        else:
            raise runtimeError(f'Tried to add invalid types. Tried to add: {type(self).__name__} and {type(other).__name__}')

    def __sub__(self, other):
        """
        Subtracts two grin objects with numerical value.
        If other is an intGrinObj, returns new intGrinObj having subtracted value.
        If other is a floatGrinObj, returns new floatGrinObj having subtracted value.
        Otherwise, raise runtimeError indicating types of self and other.
        """
        if type(other) is intGrinObj:
            return intGrinObj(self.value - other.value)
        elif type(other) is fl.floatGrinObj:
            return fl.floatGrinObj(float(self.value) - other.value)
        else:
            raise runtimeError(f'Tried to subtract invalid types. Tried to subtract: {type(self).__name__} and {type(other).__name__}')

    def __mul__(self, other):
        """
        Multiplies two grin objects.
        If other is an intGrinObj, returns new intGrinObj having Multiplied value.
        If other is a floatGrinObj, returns new floatGrinObj having Multiplied value.
        If other is a strGrinObj, returns new strGrinObj having Multiplied value.
        Otherwise, raise runtimeError indicating types of self and other.
        """
        if type(other) is intGrinObj:
            return intGrinObj(self.value * other.value)
        elif type(other) is fl.floatGrinObj:
            return fl.floatGrinObj(float(self.value) * other.value)
        elif type(other) is sr.strGrinObj:
            return sr.strGrinObj(other.value[1:-1] * self.value)
        else:
            raise runtimeError(f'Tried to multiply invalid types. Tried to multiply: {type(self).__name__} and {type(other).__name__}')

    def __truediv__(self, other):
        """
        Divides two grin objects with numerical value.
        If other is an intGrinObj, returns new intGrinObj having divided value.
        If other is a floatGrinObj, returns new floatGrinObj having divided value.
        If other is intGrinObj or floatGrinObj with value of 0, raise runtimeError with appropriate message.
        Otherwise, raise runtimeError indicating types of self and other.
        """
        if type(other) is intGrinObj:
            if other.value == 0:
                raise runtimeError('Cannot divide by 0.')
            else:
                return intGrinObj(self.value // other.value)
        elif type(other) is fl.floatGrinObj:
            if other.value == 0:
                raise runtimeError('Cannot divide by 0.')
            else:
                return fl.floatGrinObj(self.value / other.value)
        else:
            raise runtimeError(f'Tried to divide invalid types. Tried to divide: {type(self).__name__} and {type(other).__name__}')

    def __lt__(self, other):
        """
        Modifies base class' lt method.
        if other is a floatGrinObj, compare other to another floatGrinObj with same value as self.
        """
        if type(other) is fl.floatGrinObj:
            return fl.floatGrinObj(float(self.value)) < other
        else:
            return super().__lt__(other)

    def __le__(self, other):
        """
        Modifies base class' le method.
        if other is a floatGrinObj, compare other to another floatGrinObj with same value as self.
        """
        if type(other) is fl.floatGrinObj:
            return fl.floatGrinObj(float(self.value)) <= other
        else:
            return super().__le__(other)
