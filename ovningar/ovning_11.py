# ============================================================
# Övning 11 — while-loopar: validering och menylogik
# Ämne: while-loopar
# Nivå: ⭐⭐ Medel
# ============================================================
#
# Vanligt mönster — validera input tills den är giltig:
#
#   svar = ''
#   while svar not in ['ja', 'nej']:
#       svar = input('Ja eller nej? ')
#
# Simulera input med en lista (för att kunna testa automatiskt):
#   def fråga_tills_giltig(input_lista):
#       i = 0
#       while ...:
#           svar = input_lista[i]
#           i += 1
#       return svar
#
# ============================================================

# UPPGIFT A
# Funktionen tar en lista med simulerade inmatningar (strängar).
# Loopa tills du hittar ett svar som är antingen 'ja' eller 'nej'.
# Returnera det giltiga svaret.
# Anta att listan alltid innehåller minst ett giltigt svar.
#
# Exempel:
#   validera_ja_nej(['kanske', '', 'ja'])   →  'ja'
#   validera_ja_nej(['nej'])                →  'nej'
#   validera_ja_nej(['x', 'y', 'nej'])      →  'nej'

def validera_ja_nej(input_lista):
    # DIN KOD HÄR
    pass


# UPPGIFT B
# Funktionen tar en lista med simulerade inmatningar (strängar).
# Loopa tills du hittar en inmatning som INTE är tom (inte '').
# Returnera den första icke-tomma inmatningen (strip:ad).
# Anta att listan alltid innehåller minst ett icke-tomt värde.
#
# Exempel:
#   fråga_efter_namn(['', '  ', 'Ali'])   →  'Ali'
#   fråga_efter_namn(['Noor'])            →  'Noor'
#   fråga_efter_namn(['', 'Bo'])          →  'Bo'

def fråga_efter_namn(input_lista):
    # DIN KOD HÄR
    pass


# UPPGIFT C
# Funktionen simulerar en enkel meny-loop.
# Den tar en lista med val (strängar) och en dictionary med åtgärder.
# Loopa igenom valen ett i taget.
# Om valet finns som nyckel i åtgärder → lägg till åtgärdens värde i resultatlistan.
# Om valet är '0' → avbryt loopen.
# Returnera resultatlistan.
#
# Exempel:
#   åtgärder = {'1': 'Spelade', '2': 'Kollade highscore'}
#   meny_loop(['1', '2', '1', '0'], åtgärder)
#   →  ['Spelade', 'Kollade highscore', 'Spelade']

def meny_loop(val_lista, åtgärder):
    # DIN KOD HÄR
    pass
