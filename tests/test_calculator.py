import pytest
from src.calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(4, 5) == 20

def test_divide():
    assert divide(10, 2) == 5

# Ověření výjimky při dělení nulou BEZ zprávy
def test_divide_zero():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(5, 0)

# Ověření výjimky při dělení nulou SE zprávou
def test_divide_zero_message():
    with pytest.raises(ValueError) as exc:
        divide(5, 0)
    assert str(exc.value) == "Cannot divide by zero!"