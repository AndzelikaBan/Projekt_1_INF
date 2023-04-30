# TRANSFORMACJE WSPÓŁRZĘDNYCH

# SPIS TREŚCI
- [Opis działania programu](#OPIS-DZIAŁANIA-PROGRAMU)
- [Wymagania](#WYMAGANIA)
- [Obsługiwane systemy](#OBSŁUGIWANE-SYSTEMY)
- [Jak korzystać z programu](#JAK-KORZYSTAĆ-Z-PROGRAMU)
- [Przykładowe transformacje](#PRZYKŁADOWE-TRANSFORMACJE)
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
- Elipsoida Krasowskiego

# Nazwy obsługiwanych funkcji
- flh2XYZ (przelicza współrzędne fi, lambda, h na współrzędne X, Y, Z)
- hirvonen (przelicza współrzędne X, Y, Z na współrzędne fi, lambda, h)
- pl1992 (przelicza współrzędne fi, lambda do układu PL1992)
- pl2000 (przelicza współrzędne fi, lambda do układu PL2000)
- XYZ2neu (przelicza współrzędne X, Y, Z do układu NEU)

***

# PRZYKŁADOWE TRANSFORMACJE DLA ELIPSOIDY GRS80
- *flh2XYZ*
 
dla pierwszego punktu z pliku wsp_flh.txt (kolejno fi, lambda, h)
  ```sh
  9.092689315350223067e-01,3.670695034002574020e-01,1.413986623911187053e+02
  ```
  otrzymujemy wyniki (kolejno X, Y, Z)
  ```sh
  3664940.5000059702, 1409153.5900022953, 5009571.17000816
  ```
  
  - *hirvonen*
  
  dla pierwszego punktu z pliku wsp_inp.txt (kolejno X, Y, Z)
  ```sh
 3664940.500,1409153.590,5009571.170
  ```
  otrzymujemy wyniki (kolejno fi, lambda, h)
  ```sh
 0.9092689315350223, 0.3670695034002574, 141.3986623911187
  ```
  
  - *pl1992*
  
  dla danych z pliku wsp_fl.txt (kolejno fi, lambda)
  ```sh
 9.092689305349122009e-01,3.670695001091316412e-01
  ```
  otrzymujemy wyniki (kolejno X92, Y92)
  ```sh
 cos tam
  ```
  
 - *pl2000*
 
  dla danych z pliku wsp_fl.txt (kolejno fi, lambda)
  ```sh
  9.092689305349122009e-01,3.670695001091316412e-01
  ```
  otrzymujemy wyniki (kolejno X2000, Y2000)
  ```sh
  cos tam
  ```
  
 - *XYZ2neu*
 
  dla danych z pliku wsp_neu.txt (kolejno X, Y, Z)
  ```sh
  3664940.500,1409153.590,5009571.170
  ```
  otrzymujemy wyniki (kolejno n, e, u)
  ```sh
 cos tam
  ```

***
# BŁĘDY ORAZ NIETYPOWE ZACHOWANIA PROGRAMU

W przypadku kiedy użytkownik wprowadzi nieobsługiwaną funkcję otrzyma komunikat "Ta operacja jest niemożliwa!". Podobnie w przypadku wprowadzenia niepoprawnej nazwy elipsoidy - program wyświetli komunikat "Ta operacja jest nie zostanie wykonana, niepoprawne dane!".
