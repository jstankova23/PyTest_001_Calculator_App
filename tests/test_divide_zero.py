# Test na ověřování výjimky dělitelnosti nulou u zdrojáku src\calculator.py

# Ověření výjimky při dělení nulou BEZ zprávy
import pytest
from src.calculator import divide

def test_divide_zero():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(5, 0)

# Ověření výjimky při dělení nulou SE zprávou
def test_divide_zero_message():
    with pytest.raises(ValueError) as exc:
        divide(5, 0)
    assert str(exc.value) == "Cannot divide by zero!"
