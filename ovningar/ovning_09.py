# ============================================================
# Övning 09 — Return: modulstruktur (som Quizmästaren)
# Ämne: Returnera & använda värden
# Nivå: ⭐⭐⭐ Svårare
# ============================================================
#
# I Quizmästaren har vi fyra moduler som anropar varandra.
# Den här övningen tränar just det mönstret.
#
# Tumregeln:
#   - Funktioner som HÄMTAR eller BERÄKNAR → använd return
#   - Den som KOORDINERAR anropar och sparar returvärden i variabler
#
# ============================================================

# UPPGIFT A
# Implementera tre funktioner som bygger en komplett spelomgång.
#
# 1. välj_fråga(frågekort_lista, index) — returnerar frågekort (dict) på det indexet
#
# 2. visa_fråga(frågekort) — returnerar en sträng med frågan formaterad:
#    "Fråga: <text>\nAlternativ: <alt1>, <alt2>, ..."
#    Tips: ', '.join(frågekort['alternativ'])
#
# 3. kör_omgång(frågekort_lista) — anropar välj_fråga(0) och visa_fråga(),
#    returnerar den formaterade strängen för FÖRSTA frågan.
#
# Exempel:
#   frågor = [
#       {'text': 'Vad är 2+2?', 'alternativ': ['3', '4', '5'], 'rätt_svar': '4'},
#       {'text': 'Störst planet?', 'alternativ': ['Mars', 'Jupiter'], 'rätt_svar': 'Jupiter'},
#   ]
#   välj_fråga(frågor, 0)
#   →  {'text': 'Vad är 2+2?', 'alternativ': ['3', '4', '5'], 'rätt_svar': '4'}
#
#   visa_fråga(frågor[0])
#   →  'Fråga: Vad är 2+2?\nAlternativ: 3, 4, 5'
#
#   kör_omgång(frågor)
#   →  'Fråga: Vad är 2+2?\nAlternativ: 3, 4, 5'

def välj_fråga(frågekort_lista, index):
    # DIN KOD HÄR
    pass

def visa_fråga(frågekort):
    # DIN KOD HÄR
    pass

def kör_omgång(frågekort_lista):
    # DIN KOD HÄR — Anropa välj_fråga() och visa_fråga() härifrån!
    pass


# UPPGIFT B
# Funktionen tar en poäng (int), ett maxpoäng (int) och ett namn (str).
# Returnera ett resultat-dictionary med:
#   'namn'     → namnet
#   'poäng'    → poängen
#   'max'      → maxpoängen
#   'procent'  → int(round(poäng / max * 100))
#   'betyg'    → 'F'/'E'/'C'/'A' (0–39 / 40–59 / 60–74 / 75–100 %)
#
# Exempel:
#   bygg_resultat('Ali', 8, 10)
#   →  {'namn': 'Ali', 'poäng': 8, 'max': 10, 'procent': 80, 'betyg': 'A'}

def bygg_resultat(namn, poäng, maxpoäng):
    # DIN KOD HÄR
    pass
