import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ovningar'))
from ovning_03 import bara_jämna, analysera_poäng, bygg_frågekort

def test_bara_jämna_blandade():
    assert bara_jämna([1, 2, 3, 4, 5, 6]) == [2, 4, 6]

def test_bara_jämna_inga_jämna():
    assert bara_jämna([1, 3, 5]) == []

def test_bara_jämna_alla_jämna():
    assert bara_jämna([2, 4]) == [2, 4]

def test_analysera_poäng_basic():
    result = analysera_poäng([8, 5, 10, 3, 7])
    assert result == {'högst': 10, 'lägst': 3, 'medel': 6.6, 'antal': 5}

def test_analysera_poäng_ett_värde():
    result = analysera_poäng([7])
    assert result == {'högst': 7, 'lägst': 7, 'medel': 7.0, 'antal': 1}

def test_bygg_frågekort_basic():
    result = bygg_frågekort(['A?', 'B?'], ['x', 'y'])
    assert result == [{'fråga': 'A?', 'svar': 'x'}, {'fråga': 'B?', 'svar': 'y'}]

def test_bygg_frågekort_ett_kort():
    result = bygg_frågekort(['Q?'], ['svar'])
    assert result == [{'fråga': 'Q?', 'svar': 'svar'}]

def test_bygg_frågekort_tom():
    assert bygg_frågekort([], []) == []
