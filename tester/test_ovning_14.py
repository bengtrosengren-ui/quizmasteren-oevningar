import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ovningar'))
from ovning_14 import sök_i_lista, censurera_siffror, läs_svar

def test_sök_i_lista_hittar_två():
    result = sök_i_lista(['Paris är vackert', 'Berlin regnar', 'Jag är i paris'], 'paris')
    assert result == ['Paris är vackert', 'Jag är i paris']

def test_sök_i_lista_hittar_ingen():
    assert sök_i_lista(['Berlin', 'Rom'], 'paris') == []

def test_sök_i_lista_case_insensitivt():
    assert sök_i_lista(['PARIS'], 'paris') == ['PARIS']

def test_censurera_siffror_basic():
    assert censurera_siffror('Ring 0701234567 idag!') == 'Ring ********** idag!'

def test_censurera_siffror_inga_siffror():
    assert censurera_siffror('hej') == 'hej'

def test_censurera_siffror_bara_siffror():
    assert censurera_siffror('123') == '***'

def test_läs_svar_basic():
    assert läs_svar('  Paris , berlin ,LONDON  ') == ['paris', 'berlin', 'london']

def test_läs_svar_ett_svar():
    assert läs_svar('paris') == ['paris']

def test_läs_svar_med_mellanslag():
    assert läs_svar(' STOCKHOLM ') == ['stockholm']
