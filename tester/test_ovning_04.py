import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ovningar'))
from ovning_04 import skapa_spelare, hämta_säkert, lägg_till_poäng

def test_skapa_spelare_basic():
    assert skapa_spelare('Noor', 0) == {'namn': 'Noor', 'poäng': 0}

def test_skapa_spelare_med_poäng():
    assert skapa_spelare('Ali', 10) == {'namn': 'Ali', 'poäng': 10}

def test_hämta_säkert_finns():
    assert hämta_säkert({'namn': 'Ali'}, 'namn') == 'Ali'

def test_hämta_säkert_saknas():
    assert hämta_säkert({'namn': 'Ali'}, 'ålder') == 'saknas'

def test_hämta_säkert_tom_dict():
    assert hämta_säkert({}, 'namn') == 'saknas'

def test_lägg_till_poäng_basic():
    spelare = {'namn': 'Ali', 'poäng': 5}
    result = lägg_till_poäng(spelare, 3)
    assert result['poäng'] == 8

def test_lägg_till_poäng_från_noll():
    spelare = {'namn': 'Bo', 'poäng': 0}
    result = lägg_till_poäng(spelare, 7)
    assert result['poäng'] == 7

def test_lägg_till_poäng_returnerar_samma_dict():
    spelare = {'namn': 'Ali', 'poäng': 0}
    result = lägg_till_poäng(spelare, 1)
    assert result is spelare  # ska vara SAMMA objekt, inte en ny dict
