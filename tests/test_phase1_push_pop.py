
import subprocess, sys

def run_cli(*args: str) -> tuple[int, str, str]:
    p = subprocess.run([sys.executable, "-m", "cdc", *args], capture_output=True, text=True)
    return p.returncode, p.stdout.strip(), p.stderr.strip()

def test_T_PUSH_REAL1():
    code, out, err = run_cli("push", "5", "pop")
    # expected behavior once implemented:
    assert code == 0
    assert out == "5 + j0"
    assert err == ""

def test_T_POP_ERR1():
    code, out, err = run_cli("pop")
    # expected error once implemented:
    assert code == 1
    assert out == "Error: stack underflow"
    assert err == ""
