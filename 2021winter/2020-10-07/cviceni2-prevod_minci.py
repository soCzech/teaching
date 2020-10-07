# PREVOD CENA na MINCE
# --------------------
cena = int(input("zadejte cenu: "))

# 50, 20, 5, 1
mince50 = cena // 50
cena = cena % 50
mince20 = cena // 20
cena = cena % 20
mince5 = cena // 5
cena = cena % 5
mince1 = cena

print("50kc:", mince50)
print("20kc:", mince20)
print("5kc:", mince5)
print("1kc:", mince1)


# PREVOD MINCE na CENU
# --------------------
mince50 = int(input("Kolik 50kc minci:"))
mince20 = int(input("Kolik 20kc minci:"))
mince5 = int(input("Kolik 5kc minci:"))
mince1 = int(input("Kolik 1kc minci:"))

print("zaplatil jsi:", mince1 * 1 + mince5 * 5 + mince20 * 20 + mince50 * 50)


# PREVOD MINCE na CENU (cenu mince definuji na vstupu)
# ----------------------------------------------------
celkem = 0
while True:
    hodnota = int(input("Zadej hodnotu mince (nebo -1 pro konec):"))
    if hodnota == -1:
        break
    pocet = int(input(f"Zadej pocet {hodnota}kc minci:"))
    celkem += hodnota * pocet

print(f"celkem jsi zaplatil {celkem}kc")
