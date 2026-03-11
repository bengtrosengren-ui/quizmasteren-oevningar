import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ovningar'))
from ovning_01 import hamta_element, summera, lagg_till_utrop

def test_hamta_element_första():
    assert hamta_element(['a', 'b', 'c'], 0) == 'a'

def test_hamta_element_sista():
    assert hamta_element(['a', 'b', 'c'], 2) == 'c'

def test_hamta_element_negativt_index():
    assert hamta_element(['a', 'b', 'c'], -1) == 'c'

def test_summera_basic():
    assert summera([1, 2, 3]) == 6

def test_summera_tio():
    assert summera([10, 20, 30]) == 60

def test_summera_tom_lista():
    assert summera([]) == 0

def test_lagg_till_utrop_basic():
    assert lagg_till_utrop(['hej', 'hopp']) == ['hej!', 'hopp!']

def test_lagg_till_utrop_ett_element():
    assert lagg_till_utrop(['ja']) == ['ja!']

def test_lagg_till_utrop_tom_lista():
    assert lagg_till_utrop([]) == []
