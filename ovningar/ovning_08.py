# ============================================================
# Övning 08 — Return: fånga och kedja returvärden
# Ämne: Returnera & använda värden
# Nivå: ⭐⭐ Medel
# ============================================================
#
# När en funktion returnerar ett värde kan du använda det:
#
#   def hälsa(namn):
#       return f'Hej, {namn}!'
#
#   text   = hälsa('Ali')        # text = 'Hej, Ali!'
#   längd  = len(text)            # längd = 9
#   stor   = text.upper()         # stor = 'HEJ, ALI!'
#
# ============================================================

# UPPGIFT A
# Implementera TWO funktioner som ANROPAR varandra.
#
# 1. formatera_namn(namn) — returnerar namnet med stor bokstav (str.capitalize())
# 2. skapa_hälsning(namn) — anropar formatera_namn(), och returnerar
#    strängen "Hej, <formaterat_namn>! Du är välkommen."
#
# Exempel:
#   formatera_namn('ali')         →  'Ali'
#   skapa_hälsning('ali')         →  'Hej, Ali! Du är välkommen.'
#   skapa_hälsning('NOOR')        →  'Hej, Noor! Du är välkommen.'

def formatera_namn(namn):
    # DIN KOD HÄR
    pass

def skapa_hälsning(namn):
    # DIN KOD HÄR — Anropa formatera_namn() härifrån!
    pass


# UPPGIFT B
# Implementera TWO funktioner.
#
# 1. räkna_rätta(svar_lista, facit_lista) — tar två listor av samma längd,
#    returnerar antalet positioner där de matchar (int).
#
# 2. betygsätt(svar_lista, facit_lista) — anropar räkna_rätta() och
#    returnerar ett betyg som sträng:
#      0–39%  → 'F'
#      40–59% → 'E'
#      60–74% → 'C'
#      75–100%→ 'A'
#
# Exempel:
#   räkna_rätta(['a','b','c'], ['a','x','c'])  →  2
#   betygsätt(['a','b','c'], ['a','x','c'])    →  'C'   (2/3 = 67%)
#   betygsätt(['x','x','x'], ['a','b','c'])    →  'F'   (0/3 = 0%)

def räkna_rätta(svar_lista, facit_lista):
    # DIN KOD HÄR
    pass

def betygsätt(svar_lista, facit_lista):
    # DIN KOD HÄR — Anropa räkna_rätta() härifrån!
    pass
