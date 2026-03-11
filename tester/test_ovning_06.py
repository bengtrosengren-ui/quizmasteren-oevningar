import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ovningar'))
from ovning_06 import kontrollera_svar, räkna_resultat, sortera_topplista

FRÅGA = {'text': 'Kapital i Frankrike?', 'alternativ': ['Paris', 'Lyon'], 'rätt_svar': 'Paris'}

def test_kontrollera_svar_rätt():
    assert kontrollera_svar(FRÅGA, 'Paris') is True

def test_kontrollera_svar_lowercase():
    assert kontrollera_svar(FRÅGA, 'paris') is True

def test_kontrollera_svar_uppercase():
    assert kontrollera_svar(FRÅGA, 'PARIS') is True

def test_kontrollera_svar_fel():
    assert kontrollera_svar(FRÅGA, 'Lyon') is False

def test_räkna_resultat_basic():
    frågor = [
        {'text': 'A?', 'alternativ': ['x','y'], 'rätt_svar': 'x'},
        {'text': 'B?', 'alternativ': ['p','q'], 'rätt_svar': 'p'},
    ]
    assert räkna_resultat(frågor, ['x', 'q']) == {'rätt': 1, 'fel': 1, 'total': 2}

def test_räkna_resultat_alla_rätt():
    frågor = [{'text': 'A?', 'alternativ': [], 'rätt_svar': 'x'}]
    assert räkna_resultat(frågor, ['x']) == {'rätt': 1, 'fel': 0, 'total': 1}

def test_sortera_topplista_basic():
    result = sortera_topplista([
        {'namn': 'Ali', 'poäng': 5},
        {'namn': 'Noor', 'poäng': 12},
        {'namn': 'Bo', 'poäng': 8},
    ])
    assert result[0]['namn'] == 'Noor'
    assert result[1]['namn'] == 'Bo'
    assert result[2]['namn'] == 'Ali'

def test_sortera_topplista_ett_element():
    inp = [{'namn': 'Ali', 'poäng': 5}]
    assert sortera_topplista(inp) == inp
