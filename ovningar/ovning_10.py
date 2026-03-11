# ============================================================
# Övning 10 — while-loopar: grundmönstret
# Ämne: while-loopar
# Nivå: ⭐ Enkel
# ============================================================
#
# while-loopen kör tills villkoret blir False:
#
#   räknare = 0
#   while räknare < 3:
#       räknare += 1   # OBS: villkoret måste ändras!
#
# Utan förändring → oändlig loop!
#
# ============================================================

# UPPGIFT A
# Funktionen tar ett positivt heltal n.
# Returnera en lista med alla heltal från 1 upp till och med n.
# Använd en while-loop (inte range eller for).
#
# Exempel:
#   räkna_upp(5)   →  [1, 2, 3, 4, 5]
#   räkna_upp(1)   →  [1]

def räkna_upp(n):
    # DIN KOD HÄR
    pass


# UPPGIFT B
# Funktionen tar en lista med tal.
# Returnera summan av alla tal — men SLUTA att addera om summan överstiger 100.
# Returnera summan vid det läget (det kan vara mer än 100 om ett enskillt tal är stort).
# Använd en while-loop.
#
# Exempel:
#   summera_till_hundra([30, 40, 20, 50])   →  90   (30+40+20=90, nästa är 50 → stannar vid 90)
#   summera_till_hundra([200, 5])            →  200  (200 > 100 direkt)
#   summera_till_hundra([10, 10, 10])        →  30

def summera_till_hundra(tallista):
    # DIN KOD HÄR
    pass


# UPPGIFT C
# Funktionen tar en lista med strängar (simulerade svar).
# Loopa igenom listan ett element i taget med while.
# Returnera det FÖRSTA elementet som INTE är en tom sträng.
# Om alla är tomma, returnera None.
#
# Exempel:
#   första_icke_tomma(['', '', 'hej', 'då'])   →  'hej'
#   första_icke_tomma(['', ''])                →  None
#   första_icke_tomma(['ja', ''])              →  'ja'

def första_icke_tomma(stränglista):
    # DIN KOD HÄR
    pass
