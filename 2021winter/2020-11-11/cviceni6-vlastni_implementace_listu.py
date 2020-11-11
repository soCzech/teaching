class NafukovaciPole:
    """nase reimplementace python tridy list"""

    def __init__(self, inicialni_velikost=10):
        """inicializace tridy"""

        # nechceme resit problemy, kdy je pole prazdne nebo ma jen jeden prvek atd.
        # takze si rekneme ze minimalni velikost pole je napr. 10 a i kdyz je prvku v poli mene, tak budeme mit velikost 10
        self.pole = [-1] * inicialni_velikost
        # zapamatujeme si jeji hodnotu, hodi se nam na zmensovani pole ve funkci pop
        self.minimalni_velikost = inicialni_velikost

        self.aktualni_delka = 0  # na zacatku je pole prazdne
        self.realna_delka = inicialni_velikost  # vzdy totozne s len(self.pole)

    def append(self, hodnota):
        """pridani prvku na konec pole"""

        # pokud je pole uz plne, musime ho zvetsit a prekopirovat hodnoty do vetsiho pole
        if self.aktualni_delka == self.realna_delka:
            nove_pole = [-1] * (self.realna_delka * 2)

            for i in range(self.aktualni_delka):
                nove_pole[i] = self.pole[i]

            self.pole = nove_pole
            self.realna_delka *= 2

        # ted uz mame urcite v poli misto, takze muzeme na konec pridat hodnotu a zvetsit jeho "aktualni delku"
        self.pole[self.aktualni_delka] = hodnota
        self.aktualni_delka += 1

    def __len__(self):
        """funkce, ktera se zavola pri volani len(instance_meho_nafukovaciho_pole)"""
        return self.aktualni_delka

    def __str__(self):
        """funkce, ktera se zavola pri volani str(instance_meho_nafukovaciho_pole),
           tj. i pokud volam print(instance_meho_nafukovaciho_pole)"""
        return "[" + ", ".join([str(x) for x in self.pole[:self.aktualni_delka]]) + f"] (capacity: {self.realna_delka})"

    def insert(self, index, hodnota):
        """pridani prvku na index"""

        # nejdrive musim zkontrolovat jestli se mi tam prvek vejde
        # to uz jsme delali v append, takze muzu vyuzit append a pridat na konec nejakou "placeholder" hodnotu
        self.append(0)

        # naposouvam prvky smerem ke konci pole, vim ze poslednim prvkem je 0 - tu prepisu predposlednim prvkem atd.
        # ukazkovy prubeh for cyklu:
        #   pole: hodnota0 hodnota1 hodnota2 hodnota3 0
        #   aktualni_delka: 5
        #   index: 2
        #   pole[4] = pole[3]
        #   pole[3] = pole[2]
        #   >> pole: hodnota0 hodnota1 hodnota2 hodnota2 hodnota3
        for i in range(self.aktualni_delka - 1, index, -1):
            self.pole[i] = self.pole[i - 1]

        # na to spravne misto umistim novou hodnotu
        # z ukazky:
        #   >> pole: hodnota0 hodnota1 nova_hodnota hodnota2 hodnota3
        self.pole[index] = hodnota

    def pop(self, index=None):
        """odstraneni prvku z indexu"""

        # pokud neuvedeme hodnotu index, tak jako u implementace list.pop budeme odstranovat posledni prvek
        if index is None:
            index = self.aktualni_delka - 1

        # naposouvam prvky smerem na zacatek listu
        # ukazkovy prubeh for cyklu:
        #   pole: hodnota0 hodnota1 hodnota2 hodnota3
        #   aktualni_delka: 4
        #   index: 1
        #   pole[1] = pole[2]
        #   pole[2] = pole[3]
        #   >> pole: hodnota0 hodnota2 hodnota3 hodnota3
        for i in range(index + 1, self.aktualni_delka):
            self.pole[i - 1] = self.pole[i]

        # nastavim posledni hodnotu na -1 a zmensim aktualni delku listu
        self.pole[self.aktualni_delka - 1] = -1
        self.aktualni_delka -= 1

        # co kdyz nejdrive udelam 1000000 appendu, pole ma tedy delku alespon 1000000, a pak udelam 999000 popu?
        # v tu chvili pole obsahuje 1000 prvku ale v pameti zabira alespon 1000000 "jednotek" (napr. bajtu nebo nejakych nasobku bajtu)
        # obcas bychom tedy chteli pole i zmensovat, musime byt ale obezretni, abychom se nedostali do situace,
        # kdy volame vzdy pop, ktery zpusobi zmenseni pole, a hned potom append, ktery zpusobi zase zvetseni,
        # tj. by kazdy append/pop trval O(n) a to nechceme
        if self.realna_delka > self.minimalni_velikost:  # zmensovat chceme pouze pokud mame pole vetsi nez je jeho inicialni delka (napr. 10 prvku)
            # zmensovat chceme prave kdyz je realna delka 4x vetsi nez aktualni delka, ale zmensujeme jen na polovicni velikost !!!
            # kdybychom chteli zmensovat kdyz je realna delka jen 2x vetsi nez aktualni delka, dostali bychom se do problemu viz vyse.
            if self.realna_delka == self.aktualni_delka * 4:
                nove_pole = [-1] * (self.realna_delka // 2)
                for i in range(self.aktualni_delka):
                    nove_pole[i] = self.pole[i]

                self.pole = nove_pole
                self.realna_delka //= 2


print("""=================
TESTY NASEHO NAFUKOVACIHO POLE
=================
""")
p = NafukovaciPole(inicialni_velikost=10)

print(p)
p.append(1)
p.append(3)
print(p)
p.insert(1, 2)
print(p)
p.insert(0, 0)
print(p)
print("---")
for _ in range(20):
    p.append(10)
    print(p)
print("---")
p.pop(0)
print(p)
for _ in range(20):
    p.pop()
    print(p)

print(len(p))


# =================
# Spatne nafukovaci pole, ktere nezvetsuje pole vzdy dvakrat, ale pouze o jedna
# pro porovnani, proto je implementovany jen append
# =================
class SpatneNafukovaciPole:

    def __init__(self, inicialni_velikost=10):
        self.pole = [-1] * inicialni_velikost
        self.aktualni_delka = 0
        self.realna_delka = inicialni_velikost
        self.inicialni_velikost = inicialni_velikost

    def append(self, hodnota):
        if self.aktualni_delka == self.realna_delka:
            nove_pole = [-1] * (self.realna_delka + 1)

            for i in range(self.aktualni_delka):
                nove_pole[i] = self.pole[i]

            self.pole = nove_pole
            self.realna_delka += 1

        self.pole[self.aktualni_delka] = hodnota
        self.aktualni_delka += 1


# =================
# POROVNANI NafukovaciPole vs. SpatneNafukovaciPole
# =================
# balicek time je na mereni casu
# balicek matplotlib (a jeho podbalicek pyplot) je na vykresleni grafu
import time
import matplotlib.pyplot as plt


delky = [100, 10000, 50000, 100000, 200000, 300000, 400000, 500000, 650000, 800000, 1000000]

casy = []
for d in delky:
    # vzdy si vytvorime nase nafukovaci pole a d-krat zavolame append
    p = NafukovaciPole()

    start = time.time()
    for _ in range(d):
        p.append(0)
    end = time.time()
    # zmerime cas
    casy.append(end - start)

# vytvorime graf kde na xove ose budou delky a na yove casy
plt.scatter(x=delky, y=casy, label="O(n)")
# zobrazime popisek (label)
plt.legend()
# zobrazime okno s grafem
print("Otevira se okno s grafem, zavrenim okna bude script pokracovat...")
plt.show()
# !!! Nezapomente, ze casy jsou jen orientacni, zalezi taktez na tom, co vas pocitac dela na pozadi
#     tj. pokazde budou jine - pro presnejsi odhad je potreba pro kazdou delku namerit vicekrat a zprumerovat !!!


# ======================
# cele udelame znovu, ted jiz porovnavame i se spatnym polem
# protoze spatne pole trva hrozne dlouho, tak musime taktez delky pouzit vyrazne kratsi
delky = [100, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000]

casy = []
for d in delky:
    p = NafukovaciPole()

    start = time.time()
    for _ in range(d):
        p.append(0)
    end = time.time()
    casy.append(end - start)

casy2 = []
for d in delky:
    p = SpatneNafukovaciPole()

    start = time.time()
    for _ in range(d):
        p.append(0)
    end = time.time()
    casy2.append(end - start)

plt.scatter(delky, casy, label="O(n)")
plt.scatter(delky, casy2, label="O(n^2)")
plt.legend()
print("Otevira se okno s grafem, zavrenim okna bude script pokracovat...")
plt.show()
