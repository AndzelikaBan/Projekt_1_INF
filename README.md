# TRANSFORMACJE WSPÓŁRZĘDNYCH

# SPIS TREŚCI
- [Opis działania programu](#OPIS-DZIAŁANIA-PROGRAMU)
- [Wymagania](#WYMAGANIA)
- [Obsługiwane systemy](#OBSŁUGIWANE-SYSTEMY)
- [Jak korzystać z programu](#JAK-KORZYSTAĆ-Z-PROGRAMU)
- [Przykładowe komendy wywołania programu](#PRZYKŁADOWE-KOMENDY-WYWOŁANIA-PROGRAMU)
- [Przykładowe transformacje](#PRZYKŁADOWE-TRANSFORMACJE-DLA-ELIPSOIDY-GRS80)
- [Błędy oraz nietypowe zachowania programu](#BŁĘDY-ORAZ-NIETYPOWE-ZACHOWANIA-PROGRAMU)

***

# OPIS DZIAŁANIA PROGRAMU

Program służy do przeliczania współrzędnych między różnymi układami na różnych elipsoidach odniesienia (WGS84, GRS80, elipsoida Krasowskiego). 
Jest 5 opcji przeliczania współrzędnych:
- XYZ (geocentryczne) -> BLH (elipsoidalne fi, lambda, h)
- BLH (elipsoidalne fi, lambda, h) -> XYZ (geocentryczne)
- BL (elipsoidalne fi, lambda, h) -> NEU (topocentryczne northing, easting, up)
- BL (elipsoidalne fi, lambda, h) -> PL2000
- BL (elipsoidalne fi, lambda, h) -> PL1992

***

# WYMAGANIA

Żeby program poprawnie działał na danym komputerze użytkownik musi spełnić następujące wymagania:
- mieć zainstalowanego Pythona w wersji 3.9
- mieć zainstalowane biblioteki: numpy, math, argparse

***

# OBSŁUGIWANE SYSTEMY
- Windows 10
- Windows 11

***

# JAK KORZYSTAĆ Z PROGRAMU

W celu poprawnego korzystania z programu konieczne będzie utowrzenie pliku ze współrzędnymi (.txt). Jeden wiersz odpowiada współrzędnym jednego punktu i jego dane powinny być oddzielone "," (przecinkiem). Części dziesiętne muszą znajdować się po "." (kropce).


W celu wprowadzenia danych do programu należy uruchomić wiersz poleceń w lokalizacji, w której znajduje się plik z programem. Następnie należy użyć komendy: ***python Projekt_1.py -plik nazwa_pliku.txt -trans [nazwa_funkcji](#Nazwy-obsługiwanych-funkcji) -model [nazwa_elipsoidy](#Nazwy-obsługiwanych-elipsoid)***. 

Po wyborze parametrów i załadowaniu pliku z danymi wygeneruje się plik tekstowy z wynikami naszej transformacji, a na konsoli pojawi się komunikat:
  ```sh
   Plik wynikowy zapisany.
  ```
Plik ten zapisany zostanie w folderze, w którym znajduje się skrypt z programem.

***	

# Nazwy obsługiwanych elipsoid
- grs80
- wgs84
- Krasowski

# Nazwy obsługiwanych funkcji
- flh2XYZ (przelicza współrzędne fi, lambda, h na współrzędne X, Y, Z)
- hirvonen (przelicza współrzędne X, Y, Z na współrzędne fi, lambda, h)
- pl1992 (przelicza współrzędne fi, lambda do układu PL1992)
- pl2000 (przelicza współrzędne fi, lambda do układu PL2000)
- XYZ2neu (przelicza współrzędne X, Y, Z do układu NEU)

***

# PRZYKŁADOWE KOMENDY WYWOŁANIA PROGRAMU 
- *flh2XYZ*

```sh
python Projekt_1.py -plik wsp_flh.txt -trans flh2XYZ -model grs80
```

- *hirvonen*

```sh
python Projekt_1.py -plik wsp_inp.txt -trans hirvonen -model grs80
```

- *pl1992*

```sh
python Projekt_1.py -plik wsp_flh.txt -trans pl1992 -model grs80
```

- *pl2000*

```sh
python Projekt_1.py -plik wsp_flh.txt -trans pl2000 -model grs80
```

- *XYZ2neu*

```sh
python Projekt_1.py -plik neu.txt -trans XYZ2neu -model grs80
```

***

# PRZYKŁADOWE TRANSFORMACJE DLA ELIPSOIDY GRS80

<ins>Poniżej podano w jakich jednostkach są współrzędne w plikach wejściowych i wyjściowych.</ins>
- *flh2XYZ*
 
dla pierwszego punktu z pliku wsp_flh.txt (kolejno fi[rad], lambda[rad], h[m])
  ```sh
  9.092689315350223067e-01,3.670695034002574020e-01,1.413986623911187053e+02
  ```
  otrzymujemy wyniki (kolejno X[m], Y[m], Z[m])
  ```sh
  3664940.500005, 1409153.590002, 5009571.170008
  ```
  
  - *hirvonen*
  
  dla pierwszego punktu z pliku wsp_inp.txt (kolejno X[m], Y[m], Z[m])
  ```sh
 3664940.500,1409153.590,5009571.170
  ```
  otrzymujemy wyniki (kolejno fi[rad], lambda[rad], h[m])
  ```sh
 0.909268931535022, 0.367069503400257, 141.3986623911187
  ```
  
  - *pl1992*
  
  dla pierwszego punktu z pliku wsp_flh.txt (kolejno fi[rad], lambda[rad], h[m])
  ```sh
 9.092689315350223067e-01,3.670695034002574020e-01,1.413986623911187053e+02
  ```
  otrzymujemy wyniki (kolejno X92[m], Y92[m])
  ```sh
 472071.341071, 639114.490922
  ```
  
 - *pl2000*
 
  dla pierwszego punktu z pliku wsp_flh.txt (kolejno fi[rad], lambda[rad], h[m])
  ```sh
  9.092689315350223067e-01,3.670695034002574020e-01,1.413986623911187053e+02
  ```
  otrzymujemy wyniki (kolejno X2000[m], Y2000[m])
  ```sh
  5773722.720951, 7502160.783244
  ```
  
 - *XYZ2neu*
 
  dla pierwszego punktu z pliku neu.txt (kolejno s[m], alfa[rad], z[rad], fi[rad], lambda[rad])
  ```sh
  31000,4.886921905584122,1.5707963267948966,0.9092689315350225,0.3670695034002574
  ```
  otrzymujemy wyniki (kolejno n[m], e[m], u[m])
  ```sh
  4680.53574901, -30427.18265275,  -3644.05555915
  ```

***
# BŁĘDY ORAZ NIETYPOWE ZACHOWANIA PROGRAMU

W przypadku kiedy użytkownik wprowadzi nieobsługiwaną funkcję otrzyma komunikat "Ta operacja jest niemożliwa!". Podobnie w przypadku wprowadzenia niepoprawnej nazwy elipsoidy - program wyświetli komunikat "Ta operacja jest nie zostanie wykonana, niepoprawne dane!".

<ins>Ponadto transformacje BLh -> PL2000 oraz BLh -> PL1992 na modelu elipsoidy Krasowskiego dają błędne wyniki i nie powinny być używane!</ins>
