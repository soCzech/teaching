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


Zapoctovy program
-----------------
#### Zadání
- tema zapoctoveho programu si volite vy - idealne neco, co si chcete naprogramovat, napriklad:
    - webovka zobrazujici info z vaseho chytreho kvetinace
    - program zpracovavajici vase fotky z mikroskopu
    - hra (napr. snake v prikazove radce)
- :exclamation: do **24. 12. 2020** mi napište e-mail (na tomas.soucek@cvut.cz!!!) s předmětem 'NPRG030 Zapoctovy program [vase_jmeno]' s podrobnejsim zadanim, nezapomente zminit:
    - jake vstupy bude mit program (textovy soubor s nejakymi daty? - jakymi?, fotka?, url?)
    - co bude vystupem programu
    - jak se bude spoustet (napr. python detect_cells.py /cesta/k/fotce.jpg)
    - jake balicky chcete pouzivat (napr. numpy, opencv, flask, atd.)
- tema samozrejme podleha memu schvaleni ;)
- inspirace, pokud fakt nevite co...:
    - https://ksvi.mff.cuni.cz/~holan/zap_zs_2019-20_python.txt
    - http://mj.ucw.cz/vyuka/zap/
    - https://www.ms.mff.cuni.cz/~dvoram30/zapoctak.html
    - https://www.ms.mff.cuni.cz/~forstova/pgmZ/Zapoctaky.html
    
#### Reseni
- odevzdani na totozny mail s totoznym predmetem **do konce zkouskoveho** (tj. pred zacatkem letniho semestru)
    - preferovany zpusob odevzdani je odkaz na vas repozitar s kodem na githubu (nebo obdobne sluzbe)
    - jinak jako zip, v mailu na nej poslete odkaz, neposilejte primo jako prilohu mailu
- soucasti reseni musi byt:
    - jak program spustit (melo by to jit z prikazove radky jednim prikazem a melo by to byt spustitelne i na linuxu)
        - pokud je spusteni zavisle na necem specifickem (napr. na chytrem kvetinaci), nutnost predvest program osobne (nebo pres zoom)
    - jake balicky potrebuji na spusteni (pokud nejake specialni pouzivate)
    - co program umi, s jakymi argumenty ho mohu spoustet?
    - vse toto popsane v 'README' souboru
    - ukazkove vstupy, pokud program ocekava neco na vstupu (napr. fotku)
- kod...:
    - musi byt citelny, s komentari co ktera cast, radek, funkce dela (pokud to okamzite nevyplyva z nazvu funkce ci obsahu radku)
    - by mel byt rozumne strukturovany - vicekrat volany kod ve funkcich, spravne pouziti trid
    - v kodu be mela byt pouzita python jmenna konvence - def jmeno_funkce(), class MojeTrida, atd. (NE mojeTrida ani Moje_trida!)
- program musi fungovat a nesmi na nejaky jednoduchy ocekavany vstup spadnout
    - napr. pokud argumentem programu je cesta k souboru - program nesmi skoncit vyjimkou, pokud soubor neexistuje
- pokud vse nebude nadherne vysvetlene, citelne a jasne, budu vyzadovat predvedeni osobne / pres zoom,
  potencialne i dopracovani (proto nenechte odevzdani na posledni chvili)


Program cviceni
---------------
#### 6. 1.
- zapoctovy test


#### 16. 12.
- predbezny program:
    - tema podle prani studentu (:exclamation: poslete mi pred cvicenim mail, co byste chteli zopakovat, dovysvetlit, nebo probrat neco noveho / pokrocileho)
    - pouziti funkce/tridy z jineho souboru
    - balicky
        - built-in: os, glob, shutil, sys, argparse, random, time, datetime, curses ([ukazka](https://gist.github.com/claymcleod/b670285f334acd56ad1c))
        - pip install: numpy, PIL (pillow), matplotlib, pandas, scikit-learn
        - jupyter notebook
    - prace s obrazky a grafy


#### 9. 12.
#### 2. 12.
- predbezny program na nasledujici dve cviceni:
    - rekurze
    - prohledavani stavoveho prostoru
    - dynamicke programovani

#### 25. 11.
Algoritmizace
- reseni ukolu Dory ([viz zadani](https://github.com/soCzech/teaching/blob/master/2021winter/2020-11-04/cv5-algoritmizace.pdf))
- jak funguje hesovaci tabulka pod poklickou

Programovani
- viz [kody z osmeho cviceni](https://github.com/soCzech/teaching/blob/master/2021winter/2020-11-25/cviceni8-soubory_bajty_vyjimky.py)
- prace se soubory
    - cteni, nasobne cteni se `seek`
    - zapis, proc musime volat `close`, nebo `flush` kdyz soubor nechceme zavirat
- prace s raw bajty
    - cteni a zapis do souboru v rezimu `rb`, `wb`
    - jak zapsat do souboru nulovy bajt (`\x00`)
    - jak prevest cislo na sadu (napr. ctyr) bajtu `cislo.to_bytes(4, "little")`
        - v jakem poradi se zapisuji bajty (little-endian a big-endian)
    - **zapomeli jsme na zpetny prevod** (pridano do kodu z cviceni)
        - `int.from_bytes(cislo.to_bytes(4, "little"), "little") == cislo`
- vyjimky
    - vyjimky jsou dobre, ukazuji nam kde mame chybu v programu :)
    - existuji situace, kdy nemuzeme ovlivnit, zda vyjimka nastane
        - ilustrovano na situaci s oteviranim souboru
        - jak vyjimku odchytit a pokracovat v programu (`try` + `except`)
    - jak "vyhodit" vyjimku v nasem kodu
    - **vyjimky chceme eliminovat**, "vyhozeni" vyjimky je casove narocne, radsi pouzijme `if` kde to jde

:hourglass_flowing_sand: Ukoly
- zadne nove
- **dodelejte si vsechny ukoly v recodexu zpetne**, ktere nemate jeste hotove (zvlast pokud si nejste v programovani 100% jisti)
- pokud s necim (i starsim domacim ukolem) mate problem, **napiste mi mail**!

#### 18. 11.
Algoritmizace
- shrnuti ruznych datovych struktur a slozitosti jejich `insert`, `find` a `get_min` operaci
    - spojovy seznam
    - nafukovaci pole
    - setridene pole
    - halda
    - strom
    - hesovaci tabulka (=slovnik)
- klic vs. klic a hodnota
    - princip klic a hodnota lze aplikovat u vsech struktur, nejen u slovniku (samozrejme s jinymi slozitostmi)

Programovani
- diskuze nad problemy ukolu 'Hledani v setridenem poli' - deadline prodlouzena
- `dict` (=hesovaci tabulka), viz [kody ze sedmeho cviceni](https://github.com/soCzech/teaching/blob/master/2021winter/2020-11-18/cviceni7-python_dict.py)
    - najdete top 10 slov zacinajici velkym pismenem v novinovem clanku
    
:hourglass_flowing_sand: Ukoly
- :keyboard: ukol z programovani (v recodexu bude zadan az o vikendu, pracovat na nem muzete ale uz ted)
    - Halda = **3 body** - naimplementujte `class Halda` s operacemi `insert`, `get_min` (odebere nejmensi prvek) a `build`,
      ktere pobezi v case O(log n) pro insert, get_min a O(n) pro build. Detaily nacitani vstupu a vypisovani vystupu budou pote v recodexu.
      
      Hint: jednotliva cisla haldy si udrzujte v poli (standardni python `list`).
      Nezapomente, ze list.append a list.pop z konce seznamu trva v prumeru O(1), ale insert a pop do/ze zacatku nebo prostredka seznamu trva O(n).   

    
#### 11. 11.
Algoritmizace
- zásobník, fronta, prioritní fronta
    - rychlosti operaci:
        - push/pop (zasobnik)
        - enqueue/dequeue ((prioritni) fronta)
    - implementace nafukovacim polem (`list`) nebo spojovym seznamem a jejich casove slozitosti

Programovani
- tridy (`class`)
    - vlastni implementace nafukovaciho pole (`list`)
    - [kody z sesteho cviceni](https://github.com/soCzech/teaching/blob/master/2021winter/2020-11-11/cviceni6-vlastni_implementace_listu.py)

:hourglass_flowing_sand: Ukoly
- :keyboard: ukol z algoritmizace (v recodexu)
    - Spojový seznam = **2 body** + **1 bonusovy bod** za video, na kterem spolupracujete ve dvojici na reseni ukolu,
      video musi byt prilozene do pred pristim cvicenim (tj. 17. 11.), vice info v recodexu,
      spoluprace ve dvojici neznamena, ze odevzdate stejny kod - spolecne spolupracujete nad logikou reseni a pomahate si vzajemne odhalit chyby v programu


#### 4. 11.
Algoritmizace
- reseni domacich ukolu
- [program](https://github.com/soCzech/teaching/blob/master/2021winter/2020-11-04/cv5-algoritmizace.pdf)
    - Priklad 3, 4, 5
    - :movie_camera: reseni prikladu 4, 5a, 5b; binarni vyhledavani; a zadani domacich ukolu ve videu (video je standardne v playlistu cviceni na youtube)

Programovani
- reseni domacich ukolu

:hourglass_flowing_sand: Ukoly
- :page_with_curl: ukol z algoritmizace (v recodexu), [viz zadani ze cviceni](https://github.com/soCzech/teaching/blob/master/2021winter/2020-11-04/cv5-algoritmizace.pdf)
    - Priklad 5c = **1 bod** (spocitejte i presne *c* pro vasi strategii)
- :keyboard: ukoly z programovani (v recodexu)
    - Hledani v setridenem poli = **2 body**

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
    - vypisani listu na vystup
- list
    - sezareni seznamu v O(n^2), inplace
    - list v listu
    - otoceni listu (`seznam[::-1]` nebo pomoci prohazovani prvku - prvni s poslednim atd.)

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


