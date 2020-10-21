# vstup = input()
vstup = "54 2 634 73 5345 3 6 3 120"


# WHILE vs. FOR
# -------------
i = 0
while i < len(vstup):
    pismeno = vstup[i]
    # kod
    i += 1

for i in range(len(vstup)):
    pismeno = vstup[i]
    # kod
# nebo
for pismeno in vstup:
    # kod
    pass


# SPLIT textu podle znaku
# -----------------------
print("\nSPLIT textu podle znaku\n=======")
start_index = -1
vstup_split = []
# range(start, stop, step)
# range(stop) = range(0, stop, 1)
for i in range(len(vstup)):
    pismeno = vstup[i]
    # if pismeno == "0" or pismeno == "1" or pismeno == "2" or ...
    # if pismeno.isdigit():
    if ord("0") <= ord(pismeno) <= ord("9"):
        if start_index == -1:
            start_index = i
    elif pismeno == " ":
        if start_index != -1:
            vstup_split.append(vstup[start_index:i])
            start_index = -1
# nesmime zapomenout na posledni cislo na radku
if start_index != -1:
    vstup_split.append(vstup[start_index:])

print("vstup:", vstup)
print("vstup_split:", vstup_split)
# misto tohoto sloziteho kodu nam staci zavolat `vstup.split(" ")`
print(vstup_split == vstup.split(" "))


# PREVEDENI STRINGU NA CISLO
# --------------------------
print("\nPREVEDENI STRINGU NA CISLO\n=======")
vstup_split_copy = vstup_split.copy()

# inplace, menim primo hodnoty v poli `vstup_split_copy`
for i in range(len(vstup_split_copy)):
    vstup_split_copy[i] = int(vstup_split_copy[i])
print(vstup_split_copy)

# nemenim promo hodnoty v poli `vstup_split`
vstup_int = [int(cislo_str) for cislo_str in vstup_split]
print(vstup_int)

# vlastni implementace funkce `int`
# "hornerovo schema"
def muj_int(cislo_jako_str):
    cislo = 0
    for cislice in cislo_jako_str:
        cislo = cislo * 10 + (ord(cislice) - ord("0"))
    return cislo

vstup_int = [muj_int(cislo_str) for cislo_str in vstup_split]
print(vstup_int)
print(vstup_int == [int(cislo_str) for cislo_str in vstup_split])


# FUNKCE a LISTY
# --------------
print("\nFUNKCE a LISTY\n=======")
seznam = [35, 6, 2, 462]

def update_seznam(seznam_uvnitr_funkce):
    seznam_uvnitr_funkce[2] = -1
    return seznam_uvnitr_funkce

# POZOR: funkce update_seznam aktualizuje originalni `seznam` !!!
upraveny_seznam = update_seznam(seznam)
print("seznam:", seznam)
print("upraveny_seznam:", upraveny_seznam)


# spravna implementace pokud nechceme puvodni seznam menit
seznam = [35, 6, 2, 462]

def update_seznam(seznam_uvnitr_funkce):
    seznam_uvnitr_funkce = seznam_uvnitr_funkce.copy()
    seznam_uvnitr_funkce[2] = -1
    return seznam_uvnitr_funkce

upraveny_seznam = update_seznam(seznam)
print("seznam:", seznam)
print("upraveny_seznam:", upraveny_seznam)


# TRIDENI v O(n^2) pomoci hledani maxima
# --------------------------------------
print("\nTRIDENI v O(n^2) pomoci hledani maxima\n=======")
# funkce najde maximum v seznamu a prohodi maximum s poslednim prvkem seznamu
# funkce dela zmeny inplace - primo meni `seznam`
def najdi_max_a_dej_nakonec(seznam, delka_seznamu):
    max_index = 0
    for i in range(1, delka_seznamu):
        if seznam[max_index] < seznam[i]:
            max_index = i
    seznam[delka_seznamu - 1], seznam[max_index] = seznam[max_index], seznam[delka_seznamu - 1]

# cele serazeni je volani `najdi_max_a_dej_nakonec`
# nejdrive na cely seznam, pak na prvnich n-1 prvku, pak n-2, .., pak na prvni 2 prvky
def serad_inplace(vstupni_seznam):
    delka = len(vstupni_seznam)
    # n, n-1, ..., 3, 2
    for prvni_n in range(delka, 1, -1):
        najdi_max_a_dej_nakonec(vstupni_seznam, prvni_n)
        print(vstupni_seznam)

print(vstup_int)
serad_inplace(vstup_int)
print(vstup_int)

# pokud nechceme delat trizeni inplace musime si udelat kopii seznamu
seznam = [53, 2, 67, 41236, 34, 2]

def serad_a_nemen_puvodni_seznam(puvodni_seznam):
    novy_seznam = puvodni_seznam.copy()
    serad_inplace(novy_seznam)
    return novy_seznam

novy_seznam = serad_a_nemen_puvodni_seznam(seznam)
print("seznam:", seznam)
print("novy_seznam:", novy_seznam)


# VYPISOVANI POLE
# ---------------
print("\nVYPISOVANI POLE\n=======")
seznam_string = ""
for x in seznam:
    seznam_string += " " + str(x)
print(seznam_string)
print(seznam_string[1:])
print(" ".join([str(x) for x in seznam]))
