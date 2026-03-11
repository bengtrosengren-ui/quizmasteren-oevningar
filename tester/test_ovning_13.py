import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ovningar'))
from ovning_13 import rensa, svar_stämmer, räkna_ord

def test_rensa_mellanslag():
    assert rensa('  Hej  ') == 'hej'

def test_rensa_uppercase():
    assert rensa('PARIS ') == 'paris'

def test_rensa_vänster_mellanslag():
    assert rensa('  ali') == 'ali'

def test_svar_stämmer_mellanslag():
    assert svar_stämmer('  Paris  ', 'paris') is True

def test_svar_stämmer_versaler():
    assert svar_stämmer('BERLIN', 'berlin') is True

def test_svar_stämmer_fel():
    assert svar_stämmer('Rom', 'paris') is False

def test_räkna_ord_två():
    assert räkna_ord('hej hopp') == 2

def test_räkna_ord_fyra():
    assert räkna_ord('ett två tre fyra') == 4

def test_räkna_ord_ett():
    assert räkna_ord('ett') == 1
