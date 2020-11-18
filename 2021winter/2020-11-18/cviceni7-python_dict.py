# dictionary == slovnik == hash table
t = dict()
t = {}

klic, hodnota = "Tomas", 25
# ulozeni klice a hodnoty
t[klic] = hodnota
# precteni hodnoty pro dany klic
print(t[klic])

print(t)

# zkontrolovani, zda je "Honza" ve slovniku
if "Honza" in t:
    print(t["Honza"])
else:
    print("honza neni v tabulce")

# ziskani hodnoty pro dany klic ze slovniku, pokud tam neni vrat nejakou 'vychozi' hodnotu (v nasem pripade "N/A")
print(t.get("Honza", "N/A"))
print(t.get("Tomas", "N/A"))

# smaz klic a jeho hodnotu ze slovniku, dva ekvivalentni pristupy
# del t[klic]
# t.pop(klic)
# print(t)

# ulozeni klice a hodnoty, potencialne premazani stare hodnoty novou hodnotou
t[klic] = 99
print(t)
t["Honza"] = 11
print(t)


# projiti celeho slovniku - klice, klice a hodnoty, hodnoty
for key in t.keys():
    print(key)

for key, value in t.items():
    print(key, value)

for value in t.values():
    print(value)


print("""
-----------------
UKOL ZE CVICENI, spocitani slov s velkym pismenem z clanku
https://edition.cnn.com/2020/11/17/politics/chris-krebs-fired-by-trump/index.html
-----------------
""")


# sem vlozte text clanku
# text mezi trojitymi uvozovkami muze byt na vice radku
text = """
Sem vloz text clanku...
"""

# rozdeleni textu na slova
slova = text.replace("\n", " ").split(" ")

pocty = {}
for slovo in slova:
    if slovo == "":  # preskoc prazdna slova
        continue

    if ord("A") <= ord(slovo[0]) <= ord("Z"):  # pokud slovo zacina velkym pismenem ...
        # inkrementuj counter pro dane slovo
        pocet = pocty.get(slovo, 0)  # kdyz slovo jeste neni ve slovniku, vrat nulu
        pocty[slovo] = pocet + 1

        # ekvivalentne jde udelat i pomoci ...
        # if slovo in pocty:
        #     pocty[slovo] = pocty[slovo] + 1
        # else:
        #     pocty[slovo] = 1

print(pocty)

# vypis 10 nejpouzivanejsich slov
for _ in range(10):
    max_pocet, max_slovo = 0, None

    for slovo, pocet in pocty.items():
        if max_pocet < pocet:
            max_pocet = pocet
            max_slovo = slovo
    print(max_slovo, max_pocet)

    # odeber nejpouzivanejsi slovo, aby v pristi iteraci mohlo byt nove slovo jako nejpouzivanejsi
    pocty.pop(max_slovo)
