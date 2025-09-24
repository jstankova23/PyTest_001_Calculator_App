# TEST FIXTURES (number, add_tupples, subtract_tuples, multiply_tuples, divide_tuples, temp_file, db_connection)
# definice fixtures v conftest.py, není třeba fixtures sem importovat

from src.calculator import add, subtract, multiply, divide  # pro test funkce
######################################################################################################################
# 1) Fixture numbers - test
# fixture numbers s definicí jedné dvojice hodnot pro a,b v zákl. matematických operacích (+,-,*,/)
# pouze jedna dvojice hodnot pro a,b, bez proměnné expected, tak je fixture možno použít u všech 4 operací
# pro testování na více hodnotách použít parametrizovanou fixture
def test_add_fix(numbers):
    a, b = numbers
    assert add(a, b) == 9

def test_subract_fix(numbers):
    a, b = numbers
    assert subtract(a, b) == 3

def test_multiply_fix(numbers):
    a, b = numbers
    assert multiply(a, b) == 18

def test_multiply_divide_fix(numbers):
    a, b = numbers
    assert divide(a, b) == 2

#######################################################################################################################
# 2) Parametrizované fixtures xxx_tuples - test
# 4 parametrizované fixture pro opakující se argumenty a, b ve funkcích add, subtract, multiply, divide (bez výjimky);
# sady předdefinovaných scénářů pro automatizované otestování jednotlivých funkcí pro zákl. matematické operace;
# na rozdíl od parametrizované funkce numbers u této parametrizované funkce s fixture mohu zadat neomezené
# množství dvojic hodnot pro a,b, navíc s očekávaným výsledkem expected, tím ale zároveň omezuji tyto tuples
# pro konkrétní matematickou operaci;
# každá matematická operace musí mít svoji testovací parametrizovanou funkci s fixture

# 2a)ADD
# testovací funkce pracující s parametrizovanou fixture add_tuples
def test_fix_param_add(add_tuples):
    a, b, expected = add_tuples
    assert add(a, b) == expected

# 2b) SUBTRACT
# testovací funkce pracující s parametrizovanou fixture subract_tuples
def test_fix_param_subtract(subtract_tuples):
    a, b, expected = subtract_tuples
    assert subtract(a, b) == expected

# 2c) MULTIPLY
# testovací funkce pracující s parametrizovanou fixture multiply_tuples
def test_fix_param_multiply(multiply_tuples):
    a, b, expected = multiply_tuples
    assert multiply(a, b) == expected

# 2d) DIVIDE
# testovací funkce pracující s parametrizovanou fixture divide_tuples
# zde netestuji výjimku nedovolené dělení nulou
def test_fix_param_divide(divide_tuples):
    a, b, expected = divide_tuples
    assert divide(a, b) == expected

######################################################################################################################

