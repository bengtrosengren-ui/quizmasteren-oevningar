import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ovningar'))
from ovning_08 import formatera_namn, skapa_hälsning, räkna_rätta, betygsätt

def test_formatera_namn_lowercase():
    assert formatera_namn('ali') == 'Ali'

def test_formatera_namn_uppercase():
    assert formatera_namn('NOOR') == 'Noor'

def test_formatera_namn_redan_rätt():
    assert formatera_namn('Bo') == 'Bo'

def test_skapa_hälsning_lowercase():
    assert skapa_hälsning('ali') == 'Hej, Ali! Du är välkommen.'

def test_skapa_hälsning_uppercase():
    assert skapa_hälsning('NOOR') == 'Hej, Noor! Du är välkommen.'

def test_räkna_rätta_basic():
    assert räkna_rätta(['a', 'b', 'c'], ['a', 'x', 'c']) == 2

def test_räkna_rätta_alla_rätt():
    assert räkna_rätta(['x', 'x'], ['x', 'x']) == 2

def test_räkna_rätta_alla_fel():
    assert räkna_rätta(['a'], ['b']) == 0

def test_betygsätt_A():
    # 3/3 = 100% → A
    assert betygsätt(['a', 'b', 'c'], ['a', 'b', 'c']) == 'A'

def test_betygsätt_C():
    # 2/3 ≈ 67% → C
    assert betygsätt(['a', 'b', 'c'], ['a', 'x', 'c']) == 'C'

def test_betygsätt_F():
    # 0/3 = 0% → F
    assert betygsätt(['x', 'x', 'x'], ['a', 'b', 'c']) == 'F'
