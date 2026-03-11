import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ovningar'))
from ovning_12 import räkna_försök, kör_quiz, rätta_spelare

def test_räkna_försök_tre_försök():
    assert räkna_försök(['fel', 'FEL', 'Paris'], 'paris') == 3

def test_räkna_försök_ett_försök():
    assert räkna_försök(['paris'], 'paris') == 1

def test_räkna_försök_case_insensitivt():
    assert räkna_försök(['PARIS'], 'paris') == 1

def test_kör_quiz_basic():
    frågor = [
        {'text': 'A?', 'rätt_svar': 'x'},
        {'text': 'B?', 'rätt_svar': 'y'},
        {'text': 'C?', 'rätt_svar': 'z'},
    ]
    result = kör_quiz(frågor, ['x', 'fel', 'z'])
    assert result == {'poäng': 2, 'total': 3, 'missade': ['B?']}

def test_kör_quiz_alla_rätt():
    frågor = [{'text': 'A?', 'rätt_svar': 'x'}]
    result = kör_quiz(frågor, ['x'])
    assert result == {'poäng': 1, 'total': 1, 'missade': []}

def test_kör_quiz_alla_fel():
    frågor = [{'text': 'A?', 'rätt_svar': 'x'}, {'text': 'B?', 'rätt_svar': 'y'}]
    result = kör_quiz(frågor, ['z', 'z'])
    assert result['poäng'] == 0
    assert 'A?' in result['missade']

def test_rätta_spelare_basic():
    frågekort = {'text': 'Q?', 'rätt_svar': 'x'}
    rundor = [
        {'spelare': 'Ali', 'svar': 'x'},
        {'spelare': 'Noor', 'svar': 'y'},
        {'spelare': 'Bo', 'svar': 'x'},
    ]
    assert rätta_spelare(rundor, frågekort) == ['Ali', 'Bo']

def test_rätta_spelare_inga_rätt():
    frågekort = {'text': 'Q?', 'rätt_svar': 'x'}
    rundor = [{'spelare': 'Ali', 'svar': 'z'}]
    assert rätta_spelare(rundor, frågekort) == []
