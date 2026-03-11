# ============================================================
# Övning 12 — while-loopar: spelloopen
# Ämne: while-loopar
# Nivå: ⭐⭐⭐ Svårare
# ============================================================
#
# while True + flagga = klassisk spelloopstruktur:
#
#   kör = True
#   while kör:
#       val = input(...)
#       if val == 'q':
#           kör = False
#
# ============================================================

# UPPGIFT A
# Funktionen simulerar en spelomgång med flera försök.
# Den tar en lista med försök (strängar) och ett rätt svar (sträng).
# Loopa tills ett försök matchar rätt svar (case-insensitivt).
# Returnera antalet försök det tog (int).
#
# Exempel:
#   räkna_försök(['fel', 'FEL', 'Paris'], 'paris')   →  3
#   räkna_försök(['paris'], 'paris')                  →  1

def räkna_försök(försök_lista, rätt_svar):
    # DIN KOD HÄR
    pass


# UPPGIFT B
# Funktionen simulerar ett quiz med flera frågor.
# Den tar:
#   - frågekort_lista: lista med dicts {'text':..., 'rätt_svar':...}
#   - svar_lista: lista med ett svar per fråga
# Returnera en dictionary:
#   'poäng'    → antal rätta svar
#   'total'    → totalt antal frågor
#   'missade'  → lista med texterna för FELAKTIGT besvarade frågor
#
# Använd en while-loop med index-räknare (inte for).
#
# Exempel:
#   frågor = [
#       {'text': 'A?', 'rätt_svar': 'x'},
#       {'text': 'B?', 'rätt_svar': 'y'},
#       {'text': 'C?', 'rätt_svar': 'z'},
#   ]
#   kör_quiz(frågor, ['x', 'fel', 'z'])
#   →  {'poäng': 2, 'total': 3, 'missade': ['B?']}

def kör_quiz(frågekort_lista, svar_lista):
    # DIN KOD HÄR
    pass


# UPPGIFT C
# Funktionen tar en lista med rundor (dicts med 'spelare' och 'svar')
# och ett frågekort (dict med 'rätt_svar').
# Loopa med while tills ALLA spelare svarat rätt ELLER listan är slut.
# Returnera en lista med namnen på spelare som svarade rätt.
#
# Exempel:
#   frågekort = {'text': 'Q?', 'rätt_svar': 'x'}
#   rundor = [
#       {'spelare': 'Ali',  'svar': 'x'},
#       {'spelare': 'Noor', 'svar': 'y'},
#       {'spelare': 'Bo',   'svar': 'x'},
#   ]
#   rätta_spelare(rundor, frågekort)   →  ['Ali', 'Bo']

def rätta_spelare(rundor, frågekort):
    # DIN KOD HÄR
    pass
