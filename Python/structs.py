import ctypes

class Struct_IN(ctypes.Structure):
    _fields_ = [
          ("bHeat1", ctypes.c_bool),
          ("bOK", ctypes.c_bool)
     ]

    def __eq__(self, other):
        if not isinstance(other, Struct_IN):
             return False
        return all(getattr(self, f[0]) == getattr(other, f[0]) for f in self._fields_)

    def __str__(self):
         return ", ".join(f"{f[0]}: {getattr(self, f[0])}" for f in self._fields_)


class Struct_OUT(ctypes.Structure):
    _fields_ = [
          ("bHeat1", ctypes.c_bool),
          ("bOK", ctypes.c_bool)
     ]

    def __eq__(self, other):
        if not isinstance(other, Struct_OUT):
             return False
        return all(getattr(self, f[0]) == getattr(other, f[0]) for f in self._fields_)

    def __str__(self):
         return ", ".join(f"{f[0]}: {getattr(self, f[0])}" for f in self._fields_)