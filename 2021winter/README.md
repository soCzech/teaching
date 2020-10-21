Cviceni z Programovani 1 (NPRG030) a Algoritmizace (NPRG062)
================
zimni semestr 2020/2021, streda 9:00 a 9:50

Email na cviciciho: tomas.soucek@cvut.cz

Cviceni probihaji pres Zoom, link pred cvicenim dostanete mailem.

Casti cviceni se budou nahravat, budou pristupne pouze pro studenty tohoto cviceni. Veskera interakce studentu bude z videa vymazana, nemusite se tedy bat odpovidat na otazky.

:exclamation: Pozor, prvni cviceni bude probihat az v patek 2.10. v 16:30. :exclamation:

Konzultace po dohode na konci cviceni nebo mailem - nebojte se napsat, kdyz necemu nerozumite. Pokud mate problem, neco vam nejde, reste to hned, jsme tu od toho, abychom vam pomohli.


Podminky na zapocet
-------------------
#### Algoritmizace
- zapocet potrebujete na prihlaseni ke zkousce
- spravne vyresene 2/3 domacich uloh, ulohy budou zadavane nepravidelne zrejme s casovym limitem 14 dni, cast uloh bude teoreticka, kde sepisete dukaz reseni, cast bude prakticke programovani nejakeho algoritmu/ulohy v Pythonu

#### Programovani 1
- zapocet potrebujete k ziskani kreditu za predmet
- spravne vyresene urcite procento domacich uloh (alespon 2/3 uloh, vice viz zapoctovy test), zadavane obvykle kazde cviceni s casovym limitem do dalsiho cviceni, abychom si mohli na cviceni projit reseni
- zapoctovy program, do vanoc si musite zvolit tema, do konce zkouskoveho musite odevzdat hotovy program, vice informaci se dozvite az bude potreba, zatim si s tim nelamte hlavu:)
- zapoctovy test, pise se posledni cviceni, neco jako tezsi domaci uloha, casovy limit cca 75 minut. zapoctovy test bude mit neco jako lehci, stredni a tezkou variantu, pokud budete mit vice jak 95% bodu z domacich ukolu - bude vam stacit ke splneni testu vyresit lehkou variantu, pokud budete mit vice jak 80% bodu- bude vam stacit stredni varianta, v pripade 66% az 79% bodu budete muset vyresit tezkou variantu.


Ucast na online cvicenich neni vyzadovana, avsak za spravne odpovedi a aktivitu na cvicenich muzete ziskat body nad hranici 100% za domaci ulohy. Ucast na cvicenich vam taktez vyrazne usnadni reseni domacich uloh. Pri reseni domacich ukolu muzete spolupracovat ve dvojicich. Podotykam, ze muzete spolupracovat na vymysleni reseni, nikoliv ze od nekoho jineho reseni okopirujete. I v pripade spoluprace ve dvojici kazdy pak musi odevzdat svoje vlastni sepsane/naprogramovane reseni.

Domaci ukoly se odevzdavaji do [recodex.mff.cuni.cz](https://recodex.mff.cuni.cz/), kazdy se musi registrovat pres vas univerzitni ucet do SISu, pote se musite v zalozce *SIS integrace* prihlasit do skupin *Algoritmizace (20aNPRG062x12)* a *Programování 1 (20aNPRG030x13)*.

Program cviceni
---------------
#### 4. 11.
- predbezny program:
    - posloupnosti, binarni vyhledavani
    - implementace pole a spojoveho seznamu
    - zásobník, fronta, prioritní fronta (halda)


#### 28. 10. (cviceni neni, statni svatek)
V case cviceni bude probihat DOBROVOLNA konzultace pres Zoom (stejny meeting id jako cviceni).
Pokud chcete neco konzultovat, napiste mi mailem, co chcete konzultovat (napr. konkretni ulohu, konkretni nefunkcni kod, konkretni koncept).
Predpokladam, ze hlavni tema konzultace budou zaklady programovani. Konzultace se nebude nahravat.


#### 21. 10.
Algoritmizace
- spojovy seznam a pole
    - jak to asi funguje v pameti (RAM) pocitace
    - slozitosti operaci (v zavorce jejich python ekvivalenty, [viz dokumentace](https://docs.python.org/3/tutorial/datastructures.html)):
    length (`len`), get_at_index (`[]`), append, insert_at_index (`insert`), remove_at_index (`pop`), find_item (`index`), build
    - co se pouziva v pythonu a co je lepsi, kde a proc
- nedelali jsme **Eratostenovo sito** (**nastudujte/naprogramujte si doma**)

Programovani
- [kody z ctvrteho cviceni](https://github.com/soCzech/teaching/blob/master/2021winter/2020-10-21/cviceni4-vlastni_nacitani_vstupu_a_trizeni.py)
- while vs. for
- funkce a jak se chovaji seznamy uprovavane uvnitr funkci
- stringy
    - prevod stringu na cislo (vlastni funkce `int`)
    - nacitani vstupu (vlastni funkce `str.split(" ")`)

:hourglass_flowing_sand: Ukoly
- :keyboard: ukoly z programovani (v recodexu)
    - Formatovani textu = **1 bod**
    - Posun matice k nule = **1 bod**
    - English or Czech? = **1 bod**


#### 14.10.
Algoritmizace
- reseni ukolu z prvniho cviceni
- [program](https://github.com/soCzech/teaching/blob/master/2021winter/2020-10-14/cv3-algoritmizace.pdf)
    - O() notace
    - Priklad 1
- nalezeni K maxim - trideni seznamu cisel pomoci nalezeni N maxim

Programovani
- reseni ukolu z druheho cviceni

:hourglass_flowing_sand: Ukoly
- :page_with_curl: ukoly z algoritmizace (v recodexu), priklady [viz zadani ze cviceni](https://github.com/soCzech/teaching/blob/master/2021winter/2020-10-14/cv3-algoritmizace.pdf)
    - Priklad 1 (cast e, g, h) = **3 body**
    - Priklad 2 = **1 bonusovy bod** (nepocita se do zakladu pro zapocet)
    - Priklad 4 = **1 bonusovy bod** (nepocita se do zakladu pro zapocet)
- :keyboard: ukoly z programovani (v recodexu)
    - Rozklad na soucin prvocisel = **1 bod**
    - Soustavy = **1 bod**
    - K-ty nejvetsi prvek = **1 bod**
    - Vypsani pole v opacnem poradi = **1 bod**
    - Suda a licha = **1 bod**


#### 7.10.
Algoritmizace
- Eukleiduv algoritmus pro nejvetsiho spolecneho delitele (NSD, anglicky GCD)

Programovani
- [kody z druheho cviceni](https://github.com/soCzech/teaching/blob/master/2021winter/2020-10-07/cviceni2-prevod_minci.py)
    - rozklad ceny na bankovky a mince
    - prevod poctu sekund na hodiny a dny
    - pricitani urciteho poctu sekund k casu

:hourglass_flowing_sand: Ukoly
- :keyboard: v recodexu
    - Maximum = **1 bod**
    - Druha nejvetsi hodnota = **1 bod**
    - Scitani zlomku (vysledek v zakladnim tvaru !) = **1 bod**
    - Prevod do binarni soustavy = **1 bod**


#### 30.9. (presunuto na 2.10. 16:30 !!!)
Algoritmizace
- [program](https://github.com/soCzech/teaching/blob/master/2021winter/2020-09-30/cv1-algoritmizace.pdf)
    - Priklad 1 (mince), Priklad 4 (cokolada), Priklad 5 (porovnani, cast a)

Programovani
- :movie_camera: video, jak zprovoznit Python a Pycharm (odkaz v mailu)
- soucet dvou cisel:
    ```
    x = int(input())
    y = int(input())
    print(x+y)
    ```
- vyzkousjte si neco v Pythonu:
    - [codecademy.com/learn/learn-python](https://www.codecademy.com/learn/learn-python) - programovani v pythonu 2 pro zacatecniky (my pouzivame python 3, ale rozdily jsou male, napr. `print "ahoj"` vs. `print("ahoj")`)
    - [codingbat.com/python](https://codingbat.com/python) - jako recodex ale se zobrazenim spravnych a spatnych vstupu

:hourglass_flowing_sand: Ukoly
- prosim, nainstalujte si Python a Pycharm pred prvnim cvicenim, navod mate ve videu (v mailu), v pripade problemu s instalaci napiste mail
- zaregistrujte se v [recodexu](https://recodex.mff.cuni.cz/registration), ucet si vytvorite pres vas univerzitni ucet do SISu, pote se musite v zalozce *SIS integrace* prihlasit do skupin *Algoritmizace (20aNPRG062x12)* a *Programování 1 (20aNPRG030x13)*
- :keyboard: v recodexu najdete prvni ukol na Programovani 1, jedna se o jednoduche secteni cisel, jehoz cilem je si vyzkouset vkladani reseni do recodexu. **1 bod**
- :page_with_curl: ukoly z algoritmizace, odevzdavejte do recodexu jako txt soubor, pdf soubor, nebo naskenovany/kvalitne vyfoceny jpg soubor, doporucuji odevzdat v pdf pri vyuziti LaTeXu (napr. vytvoreny na [overleaf.com](https://www.overleaf.com/)), recodex vam da automaticky nula bodu - body dostanete ode me po manualni kontrole, samozrejme muzete odevzdat jen cast prikladu a dostat tak pomerove mnozstvi bodu, priklady [viz zadani ze cviceni](https://github.com/soCzech/teaching/blob/master/2021winter/2020-09-30/cv1-algoritmizace.pdf)
    - Priklad 2 (cast a + b) = **1 bod**
    - Priklad 5 (cast b) = **1 bod**
    - Priklad 5 (cast c) = **1 bod**
    - Priklad 5 (cast d) = **1 bonusovy bod** (nepocita se do zakladu pro zapocet)


