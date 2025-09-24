import pytest
from src.calculator import add, subtract, multiply, divide

# ADD - parametrizovaná funkce
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),    # Případ 1: 1 + 2 = 3
        (0, 0, 0),    # Případ 2: 0 + 0 = 0
        (-1, -1, -2), # Případ 3: -1 + -1 = -2
        (100, 200, 300) # Případ 4: 100 + 200 = 300
    ]
)
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected


# SUBTRACT - parametrizovaná funkce
@pytest.mark.parametrize(
    "a, b, expected",
    [(10, 2, 8),                 # 10-2=8
     (87, 90, -3),               # 87-90=-3
     (100, 100, 0)               # 100-100=0
    ]
)
def test_subtract_parametrized(a, b, expected):
    assert subtract(a, b) == expected


# MULTIPLY - parametrizovaná funkce
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 15),             # 5*3=15
        (-5, 3, -15),           # -5*3=-15
        (-5, -3, 15),           # -5*-3=15
        (0, 5, 0)               # 0*5=0   
    ]
)
def test_param_multiply(a, b, expected):
    assert multiply(a, b) == expected


# DIVIDE - parametrizovaná funkce
# Výjimka o nemožnosti dělení nulou je testována zvlášť v souboru test_divide_zero.py
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (18, 6, 3),          # 18/6=3
        (18, -6, -3),        # 18/-6=-3
        (-18, -6, 3),        # -18/-6=3
    ]
)
def test_param_divide(a, b, expected):
    assert divide(a, b) == expected


