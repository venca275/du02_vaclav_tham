# du02_vaclav_tham
Uživatelská dokumentace
- Program načte csv soubor s daty o průtoku
- data musí být ve formátu viz příklad
    - 115100,QD,1988,11,01,  19.6000
    - databázové číslo, označení typu dat, rok, měsíc, den, průměrný denní průtok (m3/s)
- Program projede celý soubor s daty (postupně čte řádky)
    - přitom počítá:
        - sedmidenní průměr
        - roční průměr
        - nejvyšší denní průtok v souboru
        - nejnižší denní průtok v souboru
    - pokud nastane chyba program ji vypíše do konzole
        - např. pokud nastane nulový nebo záporný průtok
    - program zapisuje sedmidenní průměry do vystup_7dni.csv
    - program zapisuje roční průměry do vystup_rok.csv

Programátorská dokumentace

- Příprava vstupu a výstupů
    - První část načte csv soubor a zapíše do READERu
    - Poté jsou definovány zápisové soubory writertyden a writerrok
    - definovány potřebné proměnné v programu
- Poté začíná FOR cyklus čtoucí všechny řádky postupně

- Zápis týdenních průměrů
    - Přeformátování denního průměru na float s výjimkou nesprávnosti hodnoty (float) a délkou řetězce v řádku
    - Existence podmínky, kdy se vybere řádek s prvním dnem týdne (zbytek čísla řádku dělitelné sedmi) a celý řádek se přiřadí do nové proměnné
    - Výpočet součtu hodnot v týdnu obalený
    - Podmínka, kdy se vybere řádek s posledním dnem v týdnu (zbytek čísla řádku dělitelné sedmi)
    - výpočet a zápis hodnot
    - Po skončení FOR cyklu dopsání posledního řádku
        - Podmínka, že se poslední řádek nesmí rovnat posledním dni v týdnu
        - Výpočet zbylého počtu řádku a zápis do souboru

- Zápis ročních průměru
    - přičte do proměnné roční průměr hodnotu denního průměru
    - Podmínka pro první řádek v souboru
        - prvnímu dni v roce přiřadíme aktuální řádku
        - do proměnné počítaný rok si přiřadíme ze sloupce 2 rok s kterým budeme počítat
    - přiřadíme do proměnnné aktuální rok sloupec 2
    - Podmínka, pokud počítány rok není stejný jako aktuální rok
        - výpočet ročního průměru, vypočtený počtem dní v roce, které se přičítají než nastane podmínka výše.
        - zápis do výstupního souboru
        - vynulování proměnných, počet dní v roce a roční průměr
        - přiřazení aktuálního řádku do proměnné první den v roce
        - přiřazení sloupce 2 do proměnné počítaný rok
    - Po skončení FOR cyklu dopsání posledního řádku, což je totožné jako zápis ročních průměru ale bez podmínky

- Maximum a minimum
    - podmínka, že pokud bude denní průtok větší (menší) než doposud nejvyšší (nejnižší) průtok
        - zapíše se do proměnné maximální (minimální) průtok hodnota denního průtoku z aktuální řádky
    - po skončení cyklu výpis řádku s nejmenší a největší hodnotou
