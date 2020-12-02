def pokladna(s, d, obsah_pokladny, poradi):
    if s == 0 and d == 0:
        print(poradi)
        return

    if s > 0:
        pokladna(s - 1, d, obsah_pokladny + 1, poradi + "S")
    if d > 0 and obsah_pokladny > 0:
        pokladna(s, d - 1, obsah_pokladny - 1, poradi + "D")


pokladna(s=4, d=5, obsah_pokladny=0, poradi="")


def hanoi(pocet_disku, tyc_start, tyc_end, tyc_pomocna):
    if pocet_disku == 1:
        print(f"presun disk {pocet_disku} z tyce {tyc_start} na tyc {tyc_end}")
        return

    hanoi(pocet_disku - 1, tyc_start, tyc_pomocna, tyc_end)
    print(f"presun disk {pocet_disku} z tyce {tyc_start} na tyc {tyc_end}")
    hanoi(pocet_disku - 1, tyc_pomocna, tyc_end, tyc_start)


hanoi(3, "A", "B", "C")
