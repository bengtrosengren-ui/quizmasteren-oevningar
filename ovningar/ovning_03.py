# ============================================================
# Övning 03 — Listor: sortering och analys
# Ämne: Listor & enumerate
# Nivå: ⭐⭐⭐ Svårare
# ============================================================
#
# Användbara list-metoder:
#   lista.append(x)     — lägg till x sist
#   lista.sort()        — sortera på plats
#   sorted(lista)       — returnera ny sorterad lista
#   max(lista)          — störst värde
#   min(lista)          — minst värde
#   len(lista)          — antal element
#
# ============================================================

# UPPGIFT A
# Funktionen tar en lista med tal.
# Returnera en ny lista med bara de TAL som är JÄMNA.
# Tips: ett tal är jämnt om tal % 2 == 0
#
# Exempel:
#   bara_jämna([1, 2, 3, 4, 5, 6])  →  [2, 4, 6]
#   bara_jämna([1, 3, 5])           →  []

def bara_jämna(tallista):
    # DIN KOD HÄR
    pass


# UPPGIFT B
# Funktionen tar en lista med poäng (heltal).
# Returnera en dictionary med:
#   'högst'   → det högsta värdet
#   'lägst'   → det lägsta värdet
#   'medel'   → medelvärdet (avrunda till 1 decimal med round())
#   'antal'   → antalet poäng
#
# Exempel:
#   analysera_poäng([8, 5, 10, 3, 7])
#   →  {'högst': 10, 'lägst': 3, 'medel': 6.6, 'antal': 5}

def analysera_poäng(poänglista):
    # DIN KOD HÄR
    pass


# UPPGIFT C
# Funktionen tar två listor av samma längd: frågor och svar.
# Returnera en lista av dictionaries med nycklarna 'fråga' och 'svar'.
# Tips: Använd enumerate för att loopa med index.
#
# Exempel:
#   bygg_frågekort(['Vad är 2+2?', 'Europas huvudstad?'],
#                  ['4', 'Bryssel'])
#   →  [{'fråga': 'Vad är 2+2?', 'svar': '4'},
#        {'fråga': 'Europas huvudstad?', 'svar': 'Bryssel'}]

def bygg_frågekort(frågor, svar):
    # DIN KOD HÄR
    pass
