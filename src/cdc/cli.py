
from __future__ import annotations
import re
import sys

# NOTE: We intentionally avoid importing functions that aren't implemented yet.
from .core import Stack, StackUnderflow, fmt_complex

def _parse_real(token: str) -> complex:
    token = token.strip().replace("−", "-")
    ## if complex number
    if "j" in token:
        # remove j
        token = token.replace("j", "")
        # split number for real and imaginary
        if "+" in token[1:]:
            real, imag = token.split("+", 1)
        elif "-" in token[1:]:
            for i in range(len(token)):
                if token[i] == "-" and i > 0:
                    real = token[:i]
                    imag = token[i:]
        return complex(float(real), float(imag))
    # if real only
    else: 
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
                j = i + 1
                number_tokens = []
                while j < len(argv) and argv[j].upper() not in ("PUSH", "POP", "ADD", "SUB", "MUL", "DIV", "DELETE"):
                    number_tokens.append(argv[j])
                    j += 1

                z_str = "".join(number_tokens)    
                z = _parse_real(z_str)
                st.push(z)
                i = j
            elif tok == "POP":
                z = st.pop()
                print(fmt_complex(z))
                i += 1
            elif tok == "ADD":
                st.add()
                i += 1
            elif tok == "SUB":
                st.sub()
                i += 1
            elif tok == "MUL":
                st.mul()
                i += 1
            elif tok == "DIV":
                st.div()
                i += 1
            elif tok == "DELETE":               
                st.delete()
                i += 1
            else:
                # unknown command (keeps scope minimal for now)
                print("Error: invalid token")
                return 1
        return 0
    except StackUnderflow:
        print("Error: stack underflow")
        return 1
    except ZeroDivisionError:
        print("Error: division by zero")
        return 1 
    except Exception:
        # conservative catch-all as "invalid token" for early increments
        print("Error: invalid token")
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
