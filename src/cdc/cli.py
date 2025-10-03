
from __future__ import annotations
import sys

# NOTE: We intentionally avoid importing functions that aren't implemented yet.
# from .core import Stack, StackUnderflow, fmt_complex

def main(argv=None) -> int:
    argv = list(argv or sys.argv[1:])
    # TODO: implement command parsing (PUSH/POP first), then grow via TDD.
    # For now, signal that functionality isn't implemented.
    print("Error: invalid token")
    return 1

if __name__ == "__main__":
    raise SystemExit(main())
