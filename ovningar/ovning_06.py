# ============================================================
# Övning 06 — Dictionaries: nästlade strukturer
# Ämne: Dictionaries
# Nivå: ⭐⭐⭐ Svårare
# ============================================================
#
# En dictionary kan innehålla andra dictionaries eller listor:
#
#   fråga = {
#       'text':       'Vad är Frankrikes huvudstad?',
#       'alternativ': ['London', 'Paris', 'Berlin'],
#       'rätt_svar':  'Paris'
#   }
#   fråga['text']           →  'Vad är Frankrikes...'
#   fråga['alternativ'][1]  →  'Paris'
#
# ============================================================

# UPPGIFT A
# Funktionen tar ett frågekort (dict med 'text', 'alternativ', 'rätt_svar')
# och ett svar (str).
# Returnera True om svaret matchar 'rätt_svar', annars False.
# Jämförelsen ska vara case-insensitiv (ignorera stora/små bokstäver).
#
# Exempel:
#   fråga = {'text': 'Kapital i Frankrike?', 'alternativ': ['Paris', 'Lyon'], 'rätt_svar': 'Paris'}
#   kontrollera_svar(fråga, 'paris')   →  True
#   kontrollera_svar(fråga, 'PARIS')   →  True
#   kontrollera_svar(fråga, 'Lyon')    →  False

def kontrollera_svar(frågekort, svar):
    # DIN KOD HÄR
    pass


# UPPGIFT B
# Funktionen tar en lista med frågekort (se ovan) och ett svar per fråga.
# Returnera en dictionary:
#   'rätt'  → antal rätta svar
#   'fel'   → antal fel
#   'total' → totalt antal frågor
#
# Exempel:
#   frågor = [
#       {'text': 'A?', 'alternativ': ['x','y'], 'rätt_svar': 'x'},
#       {'text': 'B?', 'alternativ': ['p','q'], 'rätt_svar': 'p'},
#   ]
#   räkna_resultat(frågor, ['x', 'q'])
#   →  {'rätt': 1, 'fel': 1, 'total': 2}

def räkna_resultat(frågekort_lista, svar_lista):
    # DIN KOD HÄR
    pass


# UPPGIFT C
# Funktionen tar en lista med spelar-dictionaries (med 'namn' och 'poäng').
# Returnera en ny lista sorterad efter poäng, HÖGST FÖRST.
# Tips: Använd sorted() med key=lambda x: x['poäng'] och reverse=True.
#
# Exempel:
#   sortera_topplista([
#       {'namn': 'Ali', 'poäng': 5},
#       {'namn': 'Noor','poäng': 12},
#       {'namn': 'Bo',  'poäng': 8},
#   ])
#   →  [{'namn': 'Noor', 'poäng': 12},
#        {'namn': 'Bo',   'poäng': 8},
#        {'namn': 'Ali',  'poäng': 5}]

def sortera_topplista(spelarlista):
    # DIN KOD HÄR
    pass
