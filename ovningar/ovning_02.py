# ============================================================
# Övning 02 — Listor: enumerate och filtrering
# Ämne: Listor & enumerate
# Nivå: ⭐⭐ Medel
# ============================================================
#
# enumerate() ger dig BÅDE index och värde när du loopar:
#
#   for i, värde in enumerate(['a', 'b', 'c']):
#       print(i, värde)   # 0 a, 1 b, 2 c
#
#   for i, värde in enumerate(['a', 'b', 'c'], start=1):
#       print(i, värde)   # 1 a, 2 b, 3 c
#
# ============================================================

# UPPGIFT A
# Funktionen tar en lista med strängar.
# Returnera en lista med strängar på formatet "N. värde"
# där N börjar på 1.
# Tips: Använd enumerate med start=1.
#
# Exempel:
#   numrera(['katt', 'hund', 'fågel'])
#   →  ['1. katt', '2. hund', '3. fågel']

def numrera(lista):
    # DIN KOD HÄR
    pass


# UPPGIFT B
# Funktionen tar en lista med tal.
# Returnera index för det FÖRSTA talet som är större än gränsen.
# Om inget tal är större, returnera -1.
#
# Exempel:
#   hitta_första_större([3, 7, 2, 9, 1], 6)  →  1   (7 är på index 1)
#   hitta_första_större([1, 2, 3], 10)        →  -1

def hitta_första_större(tallista, gräns):
    # DIN KOD HÄR
    pass


# UPPGIFT C
# Funktionen tar en lista med svar (strängar) och ett facit (sträng).
# Returnera en lista med tuples: (nummer, svar, 'Rätt'/'Fel')
# Numreringen börjar på 1.
#
# Exempel:
#   kontrollera_svar(['paris', 'berlin', 'paris'], 'paris')
#   →  [(1, 'paris', 'Rätt'), (2, 'berlin', 'Fel'), (3, 'paris', 'Rätt')]

def kontrollera_svar(svarlista, facit):
    # DIN KOD HÄR
    pass
