
from __future__ import annotations
import sys

# NOTE: We intentionally avoid importing functions that aren't implemented yet.
from .core import Stack, StackUnderflow, fmt_complex

def _parse_real(token: str) -> complex:
    # NOTE for First increment: real numbers only. Complex comes in later tests.
    return complex(float(token), 0.0)

def main(argv=None) -> int:
    argv = list(argv or sys.argv[1:])
    # TODO: implement command parsing (PUSH/POP first), then grow via TDD.
    
    #Implemented PUSH and POP commands
    st = Stack()
    i = 0
    try:
        while i < len(argv):
            tok = argv[i].upper()
            if tok == "PUSH":
                if i + 1 >= len(argv):
                    # not enough tokens after PUSH
                    print("Error: invalid token")
                    return 1
                z = _parse_real(argv[i + 1])
                st.push(z)
                i += 2
            elif tok == "POP":
                z = st.pop()
                print(fmt_complex(z))
                i += 1
            else:
                # unknown command (keeps scope minimal for now)
                print("Error: invalid token")
                return 1
        return 0
    except StackUnderflow:
        print("Error: stack underflow")
        return 1
    except Exception:
        # conservative catch-all as "invalid token" for early increments
        print("Error: invalid token")
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
