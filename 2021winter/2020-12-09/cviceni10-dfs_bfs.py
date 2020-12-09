# prohledavani do hloubky
# -----------------------
def dfs(stav, zbyvajici_hloubka):
    print(stav)
    if zbyvajici_hloubka > 0:
        for pismeno in "abc":
            dfs(stav + pismeno, zbyvajici_hloubka - 1)


dfs("", 3)


# prohledavani do sirky
# ---------------------
fronta = [""]

while len(fronta) > 0:
    stav = fronta.pop(0)
    print(stav)
    if len(stav) < 3:
        for pismeno in "abc":
            fronta.append(stav + pismeno)


# iterativni prohledavani do hloubky
# ----------------------------------
def iter_dfs(stav, zbyvajici_hloubka):
    if zbyvajici_hloubka == 0:
        print(stav)
    if zbyvajici_hloubka > 0:
        for pismeno in "abc":
            iter_dfs(stav + pismeno, zbyvajici_hloubka - 1)


max_hloubka = 3
for i in range(1, max_hloubka + 1):
    iter_dfs("", i)
