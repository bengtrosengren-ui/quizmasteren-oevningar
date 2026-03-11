import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ovningar'))
from ovning_05 import hitta_vinnare, filtrera_aktiva, till_uppslagsbok

def test_hitta_vinnare_basic():
    assert hitta_vinnare({'Ali': 8, 'Noor': 12, 'Bo': 5}) == 'Noor'

def test_hitta_vinnare_ett_element():
    assert hitta_vinnare({'Ali': 8}) == 'Ali'

def test_hitta_vinnare_lika_poäng():
    result = hitta_vinnare({'Anna': 10, 'Karl': 10})
    assert result in ['Anna', 'Karl']

def test_filtrera_aktiva_basic():
    result = filtrera_aktiva([
        {'namn': 'Ali', 'poäng': 5},
        {'namn': 'Bo', 'poäng': 0},
        {'namn': 'Lea', 'poäng': 3},
    ])
    assert result == [{'namn': 'Ali', 'poäng': 5}, {'namn': 'Lea', 'poäng': 3}]

def test_filtrera_aktiva_alla_noll():
    result = filtrera_aktiva([{'namn': 'X', 'poäng': 0}])
    assert result == []

def test_filtrera_aktiva_alla_aktiva():
    inp = [{'namn': 'A', 'poäng': 1}, {'namn': 'B', 'poäng': 2}]
    assert filtrera_aktiva(inp) == inp

def test_till_uppslagsbok_basic():
    result = till_uppslagsbok([
        {'fråga': 'Kapital Frankrike?', 'svar': 'Paris'},
        {'fråga': 'Störst planet?', 'svar': 'Jupiter'},
    ])
    assert result == {'Kapital Frankrike?': 'Paris', 'Störst planet?': 'Jupiter'}

def test_till_uppslagsbok_tom():
    assert till_uppslagsbok([]) == {}
