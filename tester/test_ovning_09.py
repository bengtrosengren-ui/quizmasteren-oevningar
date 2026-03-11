import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ovningar'))
from ovning_09 import välj_fråga, visa_fråga, kör_omgång, bygg_resultat

FRÅGOR = [
    {'text': 'Vad är 2+2?', 'alternativ': ['3', '4', '5'], 'rätt_svar': '4'},
    {'text': 'Störst planet?', 'alternativ': ['Mars', 'Jupiter'], 'rätt_svar': 'Jupiter'},
]

def test_välj_fråga_index_0():
    assert välj_fråga(FRÅGOR, 0) == FRÅGOR[0]

def test_välj_fråga_index_1():
    assert välj_fråga(FRÅGOR, 1) == FRÅGOR[1]

def test_visa_fråga_format():
    result = visa_fråga(FRÅGOR[0])
    assert result == 'Fråga: Vad är 2+2?\nAlternativ: 3, 4, 5'

def test_visa_fråga_två_alternativ():
    result = visa_fråga(FRÅGOR[1])
    assert result == 'Fråga: Störst planet?\nAlternativ: Mars, Jupiter'

def test_kör_omgång_returnerar_första():
    result = kör_omgång(FRÅGOR)
    assert result == 'Fråga: Vad är 2+2?\nAlternativ: 3, 4, 5'

def test_bygg_resultat_A():
    result = bygg_resultat('Ali', 8, 10)
    assert result == {'namn': 'Ali', 'poäng': 8, 'max': 10, 'procent': 80, 'betyg': 'A'}

def test_bygg_resultat_F():
    result = bygg_resultat('Bo', 0, 10)
    assert result['betyg'] == 'F'
    assert result['procent'] == 0

def test_bygg_resultat_innehåller_rätt_nycklar():
    result = bygg_resultat('X', 5, 10)
    assert all(k in result for k in ['namn', 'poäng', 'max', 'procent', 'betyg'])
