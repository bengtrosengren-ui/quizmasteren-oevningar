import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ovningar'))
from ovning_15 import normalisera_namn, bedöm_spelare, formatera_topplista

def test_normalisera_namn_mellanslag():
    assert normalisera_namn('  ali  ') == 'Ali'

def test_normalisera_namn_uppercase():
    assert normalisera_namn('NOOR') == 'Noor'

def test_normalisera_namn_tom():
    assert normalisera_namn('   ') is None

def test_normalisera_namn_tom_sträng():
    assert normalisera_namn('') is None

FRÅGOR = [
    {'text': 'A?', 'rätt_svar': 'paris'},
    {'text': 'B?', 'rätt_svar': 'berlin'},
    {'text': 'C?', 'rätt_svar': 'london'},
]

def test_bedöm_spelare_basic():
    result = bedöm_spelare(FRÅGOR, ['  PARIS ', 'berlin', 'Rom'])
    assert result == {'poäng': 2, 'procent': 67, 'svar': ['Rätt', 'Rätt', 'Fel']}

def test_bedöm_spelare_alla_rätt():
    result = bedöm_spelare(FRÅGOR, ['paris', 'berlin', 'london'])
    assert result['poäng'] == 3
    assert result['svar'] == ['Rätt', 'Rätt', 'Rätt']

def test_bedöm_spelare_alla_fel():
    result = bedöm_spelare(FRÅGOR, ['x', 'x', 'x'])
    assert result['poäng'] == 0
    assert result['svar'] == ['Fel', 'Fel', 'Fel']

def test_formatera_topplista_basic():
    result = formatera_topplista([
        {'namn': 'Ali', 'poäng': 8},
        {'namn': 'Noor', 'poäng': 10},
        {'namn': 'Bo', 'poäng': 5},
    ])
    assert result == '1. Noor - 10 poäng\n2. Ali - 8 poäng\n3. Bo - 5 poäng'

def test_formatera_topplista_ett_element():
    result = formatera_topplista([{'namn': 'Ali', 'poäng': 5}])
    assert result == '1. Ali - 5 poäng'
