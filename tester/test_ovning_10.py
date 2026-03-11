import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ovningar'))
from ovning_10 import räkna_upp, summera_till_hundra, första_icke_tomma

def test_räkna_upp_5():
    assert räkna_upp(5) == [1, 2, 3, 4, 5]

def test_räkna_upp_1():
    assert räkna_upp(1) == [1]

def test_räkna_upp_3():
    assert räkna_upp(3) == [1, 2, 3]

def test_summera_till_hundra_stannar():
    assert summera_till_hundra([30, 40, 20, 50]) == 90

def test_summera_till_hundra_direkt_över():
    assert summera_till_hundra([200, 5]) == 200

def test_summera_till_hundra_aldrig_når():
    assert summera_till_hundra([10, 10, 10]) == 30

def test_summera_till_hundra_exakt_hundra():
    # 50+50=100 → stannar (>100 är villkoret, 100 är inte > 100)
    assert summera_till_hundra([50, 50, 10]) == 100

def test_första_icke_tomma_finns():
    assert första_icke_tomma(['', '', 'hej', 'då']) == 'hej'

def test_första_icke_tomma_första():
    assert första_icke_tomma(['ja', '']) == 'ja'

def test_första_icke_tomma_saknas():
    assert första_icke_tomma(['', '']) is None
