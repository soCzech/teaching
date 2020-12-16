mince = [int(x) for x in "5 2 1".split()]
suma = 9


def rekurze(zbyva_zaplatit, mince_kterymi_jsme_platili):
    if zbyva_zaplatit == 0:
        print(" ".join([str(x) for x in mince_kterymi_jsme_platili]))
        return

    for m in mince:
        if not(len(mince_kterymi_jsme_platili) > 0 and mince_kterymi_jsme_platili[-1] < m):
            continue
        if zbyva_zaplatit - m >= 0:
            rekurze(zbyva_zaplatit - m, mince_kterymi_jsme_platili + [m])


rekurze(suma, [])




pole = """X.XS
....
.XXX
..C."""

row, col = 0, 3

sachovnice = [list(radek) for radek in pole.split("\n")]
print(sachovnice)
vzdalenosti = [[-1] * 4 for _ in range(4)]

fronta = [(row, col)]
vzdalenosti[row][col] = 0


while len(fronta) > 0:
    row, col = fronta.pop(0)

    for drow, dcol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nova_row, nova_col = row + drow, col + dcol
        if nova_row < 0 or nova_col < 0 or nova_row >= 4 or nova_col >= 4:
            continue
        if sachovnice[nova_row][nova_col] == "X":
            continue

        if vzdalenosti[nova_row][nova_col] != -1:
            continue

        fronta.append((nova_row, nova_col))
        vzdalenosti[nova_row][nova_col] = vzdalenosti[row][col] + 1

print(*[" ".join([f"{x:3}" for x in r]) for r in sachovnice], sep="\n")
print(*[" ".join([f"{x:3d}" for x in r]) for r in vzdalenosti], sep="\n")
