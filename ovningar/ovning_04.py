# ============================================================
# Övning 04 — Dictionaries: skapa och hämta
# Ämne: Dictionaries
# Nivå: ⭐ Enkel
# ============================================================
#
# En dictionary lagrar nyckel–värde-par:
#
#   person = {'namn': 'Ali', 'ålder': 16}
#   person['namn']    →  'Ali'
#   person['ålder']   →  16
#
# Lägg till eller uppdatera:
#   person['stad'] = 'Malmö'
#
# Kontrollera om nyckel finns:
#   'namn' in person   →  True
#
# ============================================================

# UPPGIFT A
# Funktionen tar ett namn (str) och en poäng (int).
# Returnera en dictionary med nycklarna 'namn' och 'poäng'.
#
# Exempel:
#   skapa_spelare('Noor', 0)   →  {'namn': 'Noor', 'poäng': 0}
#   skapa_spelare('Ali', 10)   →  {'namn': 'Ali', 'poäng': 10}

def skapa_spelare(namn, poäng):
    # DIN KOD HÄR
    pass


# UPPGIFT B
# Funktionen tar en dictionary och en nyckel.
# Om nyckeln finns, returnera dess värde.
# Om nyckeln INTE finns, returnera strängen 'saknas'.
#
# Exempel:
#   hämta_säkert({'namn': 'Ali'}, 'namn')    →  'Ali'
#   hämta_säkert({'namn': 'Ali'}, 'ålder')   →  'saknas'

def hämta_säkert(d, nyckel):
    # DIN KOD HÄR
    pass


# UPPGIFT C
# Funktionen tar en dictionary (spelare) och ett antal poäng (int).
# Lägg till poängen till 'poäng'-nyckeln och returnera den uppdaterade dict.
# Obs: returnera SAMMA dictionary, inte en ny.
#
# Exempel:
#   spelare = {'namn': 'Ali', 'poäng': 5}
#   lägg_till_poäng(spelare, 3)   →  {'namn': 'Ali', 'poäng': 8}

def lägg_till_poäng(spelare, extra_poäng):
    # DIN KOD HÄR
    pass
