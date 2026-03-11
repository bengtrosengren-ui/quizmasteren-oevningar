import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ovningar'))
from ovning_07 import välkomstmeddelande, störst, beräkna_procent

def test_välkomstmeddelande_ali():
    assert välkomstmeddelande('Ali') == 'Välkommen, Ali!'

def test_välkomstmeddelande_noor():
    assert välkomstmeddelande('Noor') == 'Välkommen, Noor!'

def test_störst_b_störst():
    assert störst(3, 7) == 7

def test_störst_a_störst():
    assert störst(10, 2) == 10

def test_störst_lika():
    assert störst(5, 5) == 5

def test_beräkna_procent_80():
    assert beräkna_procent(8, 10) == 80

def test_beräkna_procent_75():
    assert beräkna_procent(3, 4) == 75

def test_beräkna_procent_noll():
    assert beräkna_procent(0, 10) == 0

def test_beräkna_procent_hundra():
    assert beräkna_procent(10, 10) == 100
