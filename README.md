# TRANSFORMACJE WSPÓŁRZĘDNYCH

# SPIS TREŚCI
- [Opis działania programu](#OPIS-DZIAŁANIA-PROGRAMU)
- [Wymagania](#WYMAGANIA)
- [Obsługiwane systemy](#OBSŁUGIWANE-SYSTEMY)
- [Jak korzystać z programu](#JAK-KORZYSTAĆ-Z-PROGRAMU)
- [Błędy oraz nietypowe zachowania programu](#BŁĘDY-ORAZ-NIETYPOWE-ZACHOWANIA-PROGRAMU)



# OPIS DZIAŁANIA PROGRAMU

Program służy do przeliczania współrzędnych między różnymi układami na różnych elipsoidach odniesienia (WGS84, GRS80, elipsoida Krasowskiego). 
Są 5 opcje przeliczania współrzędnych:
- XYZ (geocentryczne) -> BLH (elipsoidalne fi, lambda, h)
- BLH (elipsoidalne fi, lambda, h) -> XYZ (geocentryczne)
- BL (elipsoidalne fi, lambda, h) -> NEU (topocentryczne northing, easting, up)
- BL (elipsoidalne fi, lambda, h) -> PL2000
- BL (elipsoidalne fi, lambda, h) -> PL1992

# WYMAGANIA

Żeby program poprawnie działał na danym komputerze użytkownik musi spełnić następujące wymagania:
- mieć zainstalowanego Pythona w wersji 3.9
- mieć zainstalowane biblioteki: numpy, math, argparse


# OBSŁUGIWANE SYSTEMY
- Windows 10
- Windows 11


# JAK KORZYSTAĆ Z PROGRAMU

W celu poprawnego korzystania z programu konieczne będzie utowrzenie pliku ze współrzędnymi (.txt). Jeden wiersz odpowiada współrzędnym jednego punktu i jego dane powinny być oddzielone "," (przecinkiem). Części dziesiętne muszą znajdować się po "." (kropce).

Przykładowy format pliku txt:


W celu wprowadzenia danych do programu należy uruchomić wiersz poleceń w lokalizacji, w której znajduje się plik z programem.


W celu wywołania funkcji należy użyć komendy:

	

## Nazwy obsługiwanych elipsoid:
- grs80
- wgs84
- Elipsoida Krasowskiego

## Nazwy obsługiwanych funkcji:
- flh2XYZ (przelicza współrzędne fi, lambda, h na współrzędne X, Y, Z)
- hirvonen (przelicza współrzędne X, Y, Z na współrzędne fi, lambda, h)
- pl1992 (przelicza współrzędne fi, lambda do układu PL1992)
- pl2000 (przelicza współrzędne fi, lambda do układu PL2000)
- XYZ2neu (przelicza współrzędne fi, lambda do układu NEU)


# BŁĘDY ORAZ NIETYPOWE ZACHOWANIA PROGRAMU
