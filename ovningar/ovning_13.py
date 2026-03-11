# ============================================================
# Övning 13 — Strängmetoder: grunderna
# Ämne: Strängmetoder
# Nivå: ⭐ Enkel
# ============================================================
#
# Vanliga strängmetoder:
#   text.strip()         → ta bort mellanslag vid kanterna
#   text.lower()         → gör allt gemener
#   text.upper()         → gör allt versaler
#   text.replace(a, b)   → byt ut alla a mot b
#   len(text)            → antal tecken
#
# Kedja dem: text.strip().lower()
#
# ============================================================

# UPPGIFT A
# Funktionen tar en sträng.
# Returnera strängen utan mellanslag vid kanterna, i gemener.
#
# Exempel:
#   rensa('  Hej  ')     →  'hej'
#   rensa('PARIS ')      →  'paris'
#   rensa('  ali')       →  'ali'

def rensa(text):
    # DIN KOD HÄR
    pass


# UPPGIFT B
# Funktionen tar ett svar och ett facit (strängar).
# Returnera True om svaret matchar facit, oavsett mellanslag och versaler.
#
# Exempel:
#   svar_stämmer('  Paris  ', 'paris')   →  True
#   svar_stämmer('BERLIN', 'berlin')     →  True
#   svar_stämmer('Rom', 'paris')         →  False

def svar_stämmer(svar, facit):
    # DIN KOD HÄR
    pass


# UPPGIFT C
# Funktionen tar en sträng.
# Returnera antalet ord i strängen.
# Tips: text.split() delar upp strängen på mellanslag och returnerar en lista.
#
# Exempel:
#   räkna_ord('hej hopp')            →  2
#   räkna_ord('ett två tre fyra')    →  4
#   räkna_ord('ett')                 →  1

def räkna_ord(text):
    # DIN KOD HÄR
    pass
