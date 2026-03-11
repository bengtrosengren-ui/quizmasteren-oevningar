# ============================================================
# Övning 14 — Strängmetoder: formatering och sökning
# Ämne: Strängmetoder
# Nivå: ⭐⭐ Medel
# ============================================================
#
# Fler strängmetoder:
#   text.startswith('hej')   → True/False
#   text.endswith('!')       → True/False
#   text.split(sep)          → lista av delar
#   sep.join(lista)          → sätt ihop lista till sträng
#   text.count('a')          → antal förekomster av 'a'
#   'hej' in text            → True om 'hej' finns i text
#
# ============================================================

# UPPGIFT A
# Funktionen tar en lista med strängar och ett sökord.
# Returnera en lista med de strängar som INNEHÅLLER sökordet
# (case-insensitiv sökning).
#
# Exempel:
#   sök_i_lista(['Paris är vackert', 'Berlin regnar', 'Jag är i paris'], 'paris')
#   →  ['Paris är vackert', 'Jag är i paris']

def sök_i_lista(stränglista, sökord):
    # DIN KOD HÄR
    pass


# UPPGIFT B
# Funktionen tar en sträng och returnerar en "censurerad" version
# där alla siffror ersätts med '*'.
# Tips: Loopa igenom varje tecken med for, kontrollera med tecken.isdigit()
#
# Exempel:
#   censurera_siffror('Ring 0701234567 idag!')   →  'Ring ********** idag!'
#   censurera_siffror('hej')                     →  'hej'

def censurera_siffror(text):
    # DIN KOD HÄR
    pass


# UPPGIFT C
# Funktionen tar en sträng med kommaseparerade svar (t.ex. från en fil).
# Returnera en lista med svaren, rensade (strip + lower varje).
#
# Exempel:
#   läs_svar('  Paris , berlin ,LONDON  ')
#   →  ['paris', 'berlin', 'london']

def läs_svar(rådata):
    # DIN KOD HÄR
    pass
