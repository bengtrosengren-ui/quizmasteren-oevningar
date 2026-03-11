import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ovningar'))
from ovning_11 import validera_ja_nej, fråga_efter_namn, meny_loop

def test_validera_ja_nej_hittar_ja():
    assert validera_ja_nej(['kanske', '', 'ja']) == 'ja'

def test_validera_ja_nej_direkt():
    assert validera_ja_nej(['nej']) == 'nej'

def test_validera_ja_nej_efter_flera_fel():
    assert validera_ja_nej(['x', 'y', 'nej']) == 'nej'

def test_fråga_efter_namn_hoppar_tomma():
    assert fråga_efter_namn(['', '  ', 'Ali']) == 'Ali'

def test_fråga_efter_namn_direkt():
    assert fråga_efter_namn(['Noor']) == 'Noor'

def test_fråga_efter_namn_strip():
    assert fråga_efter_namn(['  Bo  ']) == 'Bo'

def test_meny_loop_basic():
    åtgärder = {'1': 'Spelade', '2': 'Kollade highscore'}
    result = meny_loop(['1', '2', '1', '0'], åtgärder)
    assert result == ['Spelade', 'Kollade highscore', 'Spelade']

def test_meny_loop_okänt_val_ignoreras():
    åtgärder = {'1': 'A'}
    result = meny_loop(['9', '1', '0'], åtgärder)
    assert result == ['A']

def test_meny_loop_direkt_avslut():
    result = meny_loop(['0'], {'1': 'A'})
    assert result == []
