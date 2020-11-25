import os
import time

# otevreni souboru pro cteni
soubor = open("text.txt") # relativni cesta
# soubor = open("/Users/souce/Desktop/text.txt") # absolutni cesta
# soubor = open("C:\\Users\\souce\\Desktop\\text.txt") # Windows ma v ceste zpetna lomitka, to napiseme jako '\\'
# # python ale zvladne cestu i s doprednymi lomitky

# open("text.txt") je zkratka pro open("text.txt", "r"), kde 'r' znamena read (pro cteni)
soubor = open("text.txt", "r")
print(soubor.read()) # precte cely soubor
# pokud chceme cist soubor znovu, musime se vratit na zacatek souboru
soubor.seek(0)
print(soubor.read(3)) # precte 3 znaky souboru
print(soubor.readlines()) # precte soubor po radcich, avsak zde uz bez prvnich trech znaku kvuli soubor.read(3)
soubor.close() # zavreme soubor pro cteni

# ========================================================

# otevreme soubor pro zapis ('w')
soubor = open("text2.txt", "w")
for i in range(10):
    soubor.write(f"{i}\n")

print("Vypsano 0 - 9")
# ve skutecnosti je soubor porad prazdny
time.sleep(10) # pockame 10 sekund

for i in range(10):
    soubor.write(f"{i}\n")

# data se do souboru zapisi najednou pri jeho zavreni
soubor.close()

# ========================================================

# abychom nezapomeli zavolat close, muzeme vyuzit 'with'
with open("text2.txt", "w") as soubor:
    for i in range(10):
        soubor.write(f"{i}\n")
# po konci 'with' bloku je soubor automaticky zavren

# ========================================================

# pokud chceme zapsat data hned, musime zavolat soubor.flush()
soubor = open("text2.txt", "w")
for i in range(10):
    soubor.write(f"{i}\n")
soubor.flush()

print("Vypsano 0 - 9")
# ve skutecnosti je soubor porad prazdny
time.sleep(10) # pockame 10 sekund

for i in range(10):
    soubor.write(f"{i}\n")

# data se do souboru do-zapisi najednou pri jeho zavreni
soubor.close()

# ========================================================

# zapisovani do zavreneho souboru nam vyhodi vyjimku
soubor = open("text2.txt", "w")
for i in range(10):
    soubor.write(f"{i}\n")
soubor.close()
soubor.write("jeste neco")

# ========================================================

# jinou vyjimku nam vyhodi pristupovani do pole na neexistujici index
seznam = [1,2,3]
seznam[3]

# ========================================================

# jindy se muze stat (ikdyz treba je to naprosto nepravdepodobne), ze vyjimku nemuzeme ovlivnit
if os.path.exists("text.txt"): # zkontrolujeme zda soubor existuje, on doopravdy existuje
    # ted nejaky jiny program soubor smaze
    soubor = open("text.txt", "r") # zde kod vyhodi vyjimku protoze soubor uz neexistuje
else:
    soubor = open("text.txt", "w")

# ========================================================

try:
    soubor = open("text.txt", "r")
    print("precetli jsme soubor")
except:
    print("soubor neexistuje")
print("pokracujeme dal")

# ========================================================

# vyjimky jsou drahe (trvaji hodne casu), takze je dobre jejich pravdepodobnost vyskytu snizit (pokud to lze)
# napr. tim ze zkontrolujeme zda soubor existuje standardnim zpusobem

if not os.path.exists("text.txt"):
    print("soubor neexistuje")
else:
    try:
        soubor = open("text.txt", "r")
        print("precetli jsme soubor")
    except:
        print("soubor neexistuje")
print("pokracujeme dal")

# ========================================================

# i ja si muzu v kodu vyhodit vyjimku pomoci
if ...:
    raise Exception("volitelny text popisujici chybu")

# dobre pouziti by bylo v pripade haldy, kdyz se vola extract_min na prazdnou haldu:
def extract_min(self):
    if self.pocet_prvku_v_halde == 0:
        raise Exception("halda obsahuje nula prvku, extract_min nema co vratit")
    ... # klasiciky kod extract_min funkce

# mame vice pojmenovanych vyjimek
Exception
IndexError
LookupError
IOError
FileNotFoundError
NotImplemented
... # mnoho dalsich
# kazda je pouzivana v jine situaci aby uzivatel mohl odlisit typ chyby
# my si muzeme vybrat pro pouziti tu, ktera nam nejlepe sedi nebo dokonce vytvorit si i vlastni (to jsme nemeli, neni dulezite:)

# ========================================================

# soubor muzu cist (a zapisovat do nej) po bajtech misto po znacich ('rb' resp. 'wb')
with open("text2.txt", "rb") as soubor:
    bajty = soubor.read()
    print("prvni bajt (pokud ma bajt hodnotu tisknutelneho znaku - vytiskne se ten):", bajty[0])
    print("vsechny bajty:", bajty)
    print("ve skutecnosti jsou bajty cisla od 0 do 255:", list(bajty))

with open("text2.txt", "wb") as soubor:
    soubor.write(b"\x00") # zapisu do souboru bajt o hodnote 0
    soubor.write(b"\xFF") # zapisu do souboru bajt o hodnote 255 (cislo je v 16-ove soustave tj. cislice jsou 0,1,...,9,A,B,C,D,E,F - kde A ma hodnotu 10, B 11 az F 15)
    cislo = 64
    cislo_jako_bajty = cislo.to_bytes(4, "big")
    print(cislo_jako_bajty)
    print(list(cislo_jako_bajty))
    soubor.write(cislo_jako_bajty)
    # zalezi na tom v jakem poradi zapisujeme jednotlive bajty (zleva doprava nebo opacne?)
    cislo_jako_bajty = cislo.to_bytes(4, "little")
    print(cislo_jako_bajty)
    print(list(cislo_jako_bajty))

# prevod z bajtu na cisla
int.from_bytes(b'\x00\x01', "big")     # 1
int.from_bytes(b'\x00\x01', "little")  # 256

# prevod z bajtu na cislo
list(b'a') == [97] == list(b'\x61') == [ord('a')] # 61 v 16-ove soustave je 97

# prevod cisla znak
chr(97) == chr(ord("a"))
