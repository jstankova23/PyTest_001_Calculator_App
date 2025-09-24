import pytest
from src.calculator import divide

@pytest.mark.parametrize(
    "a, b, expected_exception",
    [
        (5, 0, ValueError),  # Nedovolené dělení nulou, výjimka
        (10, 2, None),       # Platné dělení nenulovými čísly, bez výjimky
    ],
)
def test_divide_parametrized(a, b, expected_exception):
    if expected_exception:
        with pytest.raises(expected_exception):
            divide(a, b)
    else:
        assert divide(a, b) == a / b

        