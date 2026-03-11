# ============================================================
# Övning 01 — Listor: hämta och loopa
# Ämne: Listor & enumerate
# Nivå: ⭐ Enkel
# ============================================================
#
# En lista lagrar flera värden på rad.
# Du når varje värde med ett index (börjar på 0).
#
#   djur = ['katt', 'hund', 'fågel']
#   djur[0]  →  'katt'
#   djur[1]  →  'hund'
#   djur[-1] →  'fågel'  (sista elementet)
#
# ============================================================

# UPPGIFT A
# Funktionen nedan tar en lista och ett index.
# Returnera det element som finns på det indexet.
#
# Exempel:
#   hamta_element(['a', 'b', 'c'], 0)  →  'a'
#   hamta_element(['a', 'b', 'c'], 2)  →  'c'
#   hamta_element(['a', 'b', 'c'], -1) →  'c'

def hamta_element(lista, index):
    # DIN KOD HÄR
    return lista[index]
    pass


# UPPGIFT B
# Funktionen nedan tar en lista med tal.
# Returnera summan av alla tal i listan.
# Tips: Loopa igenom listan och addera till en variabel.
#
# Exempel:
#   summera([1, 2, 3])      →  6
#   summera([10, 20, 30])   →  60
#   summera([])             →  0

def summera(tallista):
    # DIN KOD HÄR
    summa = 0
    for tal in tallista:
        summa += tal
    return summa
    pass


# UPPGIFT C
# Funktionen nedan tar en lista med strängar.
# Returnera en NY lista där varje sträng har ett "!" på slutet.
# Tips: Skapa en tom lista, loopa, lägg till med .append().
#
# Exempel:
#   lagg_till_utrop(['hej', 'hopp'])  →  ['hej!', 'hopp!']
#   lagg_till_utrop(['ja', 'nej'])    →  ['ja!', 'nej!']

def lagg_till_utrop(stränglista):
    # DIN KOD HÄR
    resultat = []
    for s in stränglista:
        resultat.append(s + '!')
    return resultat

    pass
