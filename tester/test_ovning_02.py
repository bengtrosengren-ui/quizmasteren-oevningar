import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ovningar'))
from ovning_02 import numrera, hitta_första_större, kontrollera_svar

def test_numrera_basic():
    assert numrera(['katt', 'hund', 'fågel']) == ['1. katt', '2. hund', '3. fågel']

def test_numrera_ett_element():
    assert numrera(['bara']) == ['1. bara']

def test_numrera_tom():
    assert numrera([]) == []

def test_hitta_första_större_finns():
    assert hitta_första_större([3, 7, 2, 9, 1], 6) == 1

def test_hitta_första_större_finns_sist():
    assert hitta_första_större([1, 2, 9], 8) == 2

def test_hitta_första_större_finns_inte():
    assert hitta_första_större([1, 2, 3], 10) == -1

def test_kontrollera_svar_blandade():
    result = kontrollera_svar(['paris', 'berlin', 'paris'], 'paris')
    assert result == [(1, 'paris', 'Rätt'), (2, 'berlin', 'Fel'), (3, 'paris', 'Rätt')]

def test_kontrollera_svar_alla_rätt():
    result = kontrollera_svar(['x', 'x'], 'x')
    assert result == [(1, 'x', 'Rätt'), (2, 'x', 'Rätt')]

def test_kontrollera_svar_alla_fel():
    result = kontrollera_svar(['y'], 'x')
    assert result == [(1, 'y', 'Fel')]
