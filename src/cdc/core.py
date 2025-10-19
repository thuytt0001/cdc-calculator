
from __future__ import annotations

class StackUnderflow(Exception):
    pass

class Stack:
    def __init__(self) -> None:
        # TODO: implement the underlying container
        # pass
        #DONE
        self._s: list[complex] = []

    def push(self, value: complex) -> None:
        # TODO: append to stack
        # raise NotImplementedError

        #DONE
        self._s.append(value)

    def pop(self) -> complex:
        # TODO: pop from stack or raise StackUnderflow
        # raise NotImplementedError
        #DONE
        if not self._s:
            raise StackUnderflow("empty stack")
        return self._s.pop()
    
    def add(self):
        if len(self._s) < 2:
            raise StackUnderflow("Not enough elements to perform ADD")
        b = self.pop()  # top of stack
        a = self.pop()  # next element
        self.push(a + b)
    
    def sub(self):
        if len(self._s) < 2:
            raise StackUnderflow("Not enough elements to perform SUB")
        b = self.pop()
        a = self.pop()
        self.push(a - b)
    
    def mul(self):
        b = self.pop()
        a = self.pop()
        self.push(a * b)

def fmt_complex(z: complex) -> str:
    # TODO: format as 'a ± jI' with -0 → 0, drop .0 when int
    # raise NotImplementedError
    #DONE
    a = 0.0 if abs(z.real) == 0 else z.real
    b = 0.0 if abs(z.imag) == 0 else z.imag
    sign = "+" if b >= 0 else "-"
    return f"{_trim(a)} {sign} j{_trim(abs(b))}"

def _trim(x: float) -> str:
    # normalize -0.0 → 0 and drop .0 if integer
    x = 0.0 if abs(x) == 0 else x
    return str(int(x)) if float(x).is_integer() else str(x)
