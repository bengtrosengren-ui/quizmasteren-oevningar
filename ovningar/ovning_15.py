# ============================================================
# Övning 15 — Strängmetoder: allt ihop (Quizmästaren-stil)
# Ämne: Strängmetoder
# Nivå: ⭐⭐⭐ Svårare
# ============================================================
#
# Den sista övningen kombinerar ALLA fem koncept.
# Det här är samma typ av funktioner som ni ska skriva i projektet.
#
# ============================================================

# UPPGIFT A
# Funktionen tar en sträng (namn) och returnerar den "normaliserad":
#   - strip() bort kantmellanslag
#   - capitalize() (stor första bokstav, resten gemener)
# Om strängen är tom efter strip → returnera None.
#
# Exempel:
#   normalisera_namn('  ali  ')   →  'Ali'
#   normalisera_namn('NOOR')      →  'Noor'
#   normalisera_namn('   ')       →  None
#   normalisera_namn('')          →  None

def normalisera_namn(namn):
    # DIN KOD HÄR
    pass


# UPPGIFT B
# Funktionen tar en lista med frågekort (dicts med 'text' och 'rätt_svar')
# och en lista med råa svar (strängar med möjliga mellanslag/versaler).
# Returnera en dictionary per spelare:
#   'poäng'    → antal rätta svar (int)
#   'procent'  → int(round(poäng / total * 100))
#   'svar'     → lista med 'Rätt'/'Fel' per fråga
#
# Tips: rensa varje svar med strip().lower() innan jämförelse.
#
# Exempel:
#   frågor = [
#       {'text': 'A?', 'rätt_svar': 'paris'},
#       {'text': 'B?', 'rätt_svar': 'berlin'},
#       {'text': 'C?', 'rätt_svar': 'london'},
#   ]
#   bedöm_spelare(frågor, ['  PARIS ', 'berlin', 'Rom'])
#   →  {'poäng': 2, 'procent': 67, 'svar': ['Rätt', 'Rätt', 'Fel']}

def bedöm_spelare(frågekort_lista, råa_svar):
    # DIN KOD HÄR
    pass


# UPPGIFT C
# Funktionen tar en lista med spelarresultat (dicts med 'namn' och 'poäng')
# och genererar en topplista som en sträng, formaterad så här:
#
#   "1. Noor - 10 poäng\n2. Ali - 8 poäng\n3. Bo - 5 poäng"
#
# Sortera högst poäng först. Numreringen börjar på 1.
# Tips: sorted(..., key=..., reverse=True), enumerate med start=1, '\n'.join(rader)
#
# Exempel:
#   formatera_topplista([
#       {'namn': 'Ali',  'poäng': 8},
#       {'namn': 'Noor', 'poäng': 10},
#       {'namn': 'Bo',   'poäng': 5},
#   ])
#   →  '1. Noor - 10 poäng\n2. Ali - 8 poäng\n3. Bo - 5 poäng'

def formatera_topplista(resultat_lista):
    # DIN KOD HÄR
    pass
