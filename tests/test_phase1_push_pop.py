
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

def test_T_PUSH_CPLX1():
    code, out, err = run_cli("push", "-2.5-j0.25", "pop")
    assert code == 0
    assert out == "-2.5 - j0.25"
    assert err == ""

def test_T_PUSH_CPLX2():
    code, out, err = run_cli("push", "3", "+", "j", "4", "pop")
    assert code == 0
    assert out == "3 + j4"
    assert err == ""

def test_T_POP_ERR1():
    code, out, err = run_cli("pop")
    # expected error once implemented:
    assert code == 1
    assert out == "Error: stack underflow"
    assert err == ""

def test_T_ADD_REAL1():
    code, out, err = run_cli("push", "2", "push", "5", "add", "pop")
    assert code == 0
    assert out == "7 + j0"
    assert err == ""


