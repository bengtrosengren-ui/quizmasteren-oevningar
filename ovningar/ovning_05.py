# ============================================================
# Övning 05 — Dictionaries: loopa och transformera
# Ämne: Dictionaries
# Nivå: ⭐⭐ Medel
# ============================================================
#
# Loopa igenom nyckel-värde-par:
#   d = {'a': 1, 'b': 2}
#   for nyckel, värde in d.items():
#       print(nyckel, värde)
#
# Loopa bara nycklar:
#   for nyckel in d:
#       print(nyckel)
#
# ============================================================

# UPPGIFT A
# Funktionen tar en dictionary med namn→poäng.
# Returnera namnet på spelaren med HÖGST poäng.
# Tips: Håll koll på vem som har mest, uppdatera när du hittar mer.
#
# Exempel:
#   hitta_vinnare({'Ali': 8, 'Noor': 12, 'Bo': 5})   →  'Noor'
#   hitta_vinnare({'Anna': 10, 'Karl': 10})            →  'Anna'  (första vid lika)

def hitta_vinnare(poängboard):
    # DIN KOD HÄR
    pass


# UPPGIFT B
# Funktionen tar en lista med dictionaries (spelarposter).
# Varje post har 'namn' och 'poäng'.
# Returnera en ny lista med bara de spelare som har poäng > 0.
#
# Exempel:
#   filtrera_aktiva([
#       {'namn': 'Ali', 'poäng': 5},
#       {'namn': 'Bo',  'poäng': 0},
#       {'namn': 'Lea', 'poäng': 3},
#   ])
#   →  [{'namn': 'Ali', 'poäng': 5}, {'namn': 'Lea', 'poäng': 3}]

def filtrera_aktiva(spelarlista):
    # DIN KOD HÄR
    pass


# UPPGIFT C
# Funktionen tar en lista med dictionaries (frågekort).
# Varje kort har 'fråga' och 'svar'.
# Returnera en ny dictionary: {fråga: svar, fråga: svar, ...}
#
# Exempel:
#   till_uppslagsbok([
#       {'fråga': 'Frankrikes huvudstad?', 'svar': 'Paris'},
#       {'fråga': 'Störst planet?',        'svar': 'Jupiter'},
#   ])
#   →  {'Frankrikes huvudstad?': 'Paris', 'Störst planet?': 'Jupiter'}

def till_uppslagsbok(frågekort):
    # DIN KOD HÄR
    pass
