
from __future__ import annotations

class StackUnderflow(Exception):
    pass

class Stack:
    def __init__(self) -> None:
        # TODO: implement the underlying container
        pass

    def push(self, value: complex) -> None:
        # TODO: append to stack
        raise NotImplementedError

    def pop(self) -> complex:
        # TODO: pop from stack or raise StackUnderflow
        raise NotImplementedError

def fmt_complex(z: complex) -> str:
    # TODO: format as 'a ± jI' with -0 → 0, drop .0 when int
    raise NotImplementedError
