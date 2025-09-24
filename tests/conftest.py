# FIXTURES - jejich definice (testování fixtures v test_fixtures.py)
import pytest       # pro všechna fixtures
import os           # pro fixture temp_file

#######################################################################################################################

# 1) Fixture numbers
# pro opakující se argumenty a, b ve funkcích add, subtract, multiply, divide
# pouze jedna dvojice hodnot pro a,b, bez proměnné expected, tak je fixture možno použít u všech 4 operací
@pytest.fixture
def numbers():
    return 6, 3
#######################################################################################################################

# 2) Parametrizované fixtures pro základní matematické operace
# 4 parametrizované fixture pro opakující se argumenty a, b ve funkcích add, subtract, multiply, divide (bez výjimky);
# sady předdefinovaných scénářů pro automatizované otestování jednotlivých funkcí pro zákl. matematické operace;
# na rozdíl od parametrizované funkce numbers u této parametrizované funkce s fixture mohu zadat neomezené
# množství dvojic hodnot pro a,b, navíc s očekávaným výsledkem expected, tím ale zároveň omezuji tyto tuples
# pro konkrétní matematickou operaci;
# každá matematická operace musí mít svoji testovací parametrizovanou funkci s fixture

# 2a) ADD
# parametrizovaná fixture add_tuples
@pytest.fixture(params=[(1, 2, 3), (0, 0, 0), (-1, -1, -2), (100, 200, 300)]) # seznam parametrů, které fix iteruje
def add_tuples(request):
    return request.param            # vrací aktuální hodnotu parametru

# 2b) SUBTRACT
# parametrizovaná fixture subtract_tuples
@pytest.fixture(params=[(10, 2, 8), (87, 90, -3), (100, 100, 0)])
def subtract_tuples(request):
    return request.param

# 2c) MULTIPLY
# parametrizovaná fixture multiply_tuples
@pytest.fixture(params=[(5, 3, 15), (-5, 3, -15), (-5, -3, 15), (0, 5, 0)]) 
def multiply_tuples(request):
    return request.param        

# 2d) DIVIDE
# parametrizovaná fixture divide_tuples
# zde netestuji výjimku nedovolené dělení nulou
@pytest.fixture(params=[(18, 6, 3), (18, -6, -3), (-18, -6, 3)])
def divide_tuples(request):
    return request.param
#######################################################################################################################