
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

def test_T_ADD_CPLX1():
    code, out, err = run_cli("push", "3+j4", "push", "1-j2", "add", "pop")
    assert code == 0
    assert out == "4 + j2"
    assert err == ""

def test_T_ADD_ERR1():
    code, out, err = run_cli("push", "3", "add")
    assert code == 1
    assert out == "Error: stack underflow"
    assert err == ""

def test_T_SUB_REAL1():
    code, out, err = run_cli("push", "5", "push", "2", "sub", "pop")
    assert code == 0
    assert out == "3 + j0"
    assert err == ""

def test_T_SUB_CPLX1():
    code, out, err = run_cli("push", "3+j4", "push", "1-j2", "sub", "pop")
    assert code == 0
    assert out == "2 + j6"
    assert err == ""

def test_T_SUB_ERR1():
    code, out, err = run_cli("sub")
    assert code == 1
    assert out == "Error: stack underflow"
    assert err == ""

def test_T_MUL_REAL1():
    code, out, err = run_cli("push", "3", "push", "-2", "mul", "pop")
    assert code == 0
    assert out == "-6 + j0"
    assert err == ""

def test_T_MUL_CPLX1():
    code, out, err = run_cli("push", "1+j2", "push", "3-j4", "mul", "pop")
    assert code == 0
    assert out == "11 + j2"
    assert err == ""

def test_T_MUL_ERR1():
    code, out, err = run_cli("mul")
    assert code == 1
    assert out == "Error: stack underflow"
    assert err == ""

def test_T_DIV_REAL1():
    code, out, err = run_cli("push", "8", "push", "2", "div", "pop")
    assert code == 0
    assert out == "4 + j0"
    assert err == ""

def test_T_DIV_CPLX1():
    code, out, err = run_cli("push", "4+j2", "push", "1+j1", "div", "pop")
    assert code == 0
    assert out == "3 - j1"
    assert err == ""

