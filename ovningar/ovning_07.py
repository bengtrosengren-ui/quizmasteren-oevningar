# ============================================================
# Övning 07 — Return: returnera värden
# Ämne: Returnera & använda värden
# Nivå: ⭐ Enkel
# ============================================================
#
# En funktion med return SKICKAR TILLBAKA ett värde:
#
#   def dubbla(x):
#       return x * 2
#
#   resultat = dubbla(5)   # resultat är nu 10
#
# Utan return får du None — värdet försvinner!
#
# ============================================================

# UPPGIFT A
# Funktionen tar ett namn (str).
# Returnera strängen "Välkommen, <namn>!"
# OBS: Använd return, inte print.
#
# Exempel:
#   välkomstmeddelande('Ali')    →  'Välkommen, Ali!'
#   välkomstmeddelande('Noor')   →  'Välkommen, Noor!'

def välkomstmeddelande(namn):
    # DIN KOD HÄR
    pass


# UPPGIFT B
# Funktionen tar två tal (int eller float).
# Returnera det STÖRRE av de två.
# Om de är lika, returnera vilket som helst av dem.
#
# Exempel:
#   störst(3, 7)    →  7
#   störst(10, 2)   →  10
#   störst(5, 5)    →  5

def störst(a, b):
    # DIN KOD HÄR
    pass


# UPPGIFT C
# Funktionen tar en poäng (int) och ett maxpoäng (int).
# Returnera poängen som en procentsats (int, avrundad).
# Tips: int(round(poäng / maxpoäng * 100))
#
# Exempel:
#   beräkna_procent(8, 10)   →  80
#   beräkna_procent(3, 4)    →  75
#   beräkna_procent(0, 10)   →  0

def beräkna_procent(poäng, maxpoäng):
    # DIN KOD HÄR
    pass
