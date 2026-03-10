Nowoczesne Technologie Przetwarzania Danych 
Lab 01 
Temat: Tworzenie modelu ML w Pythonie. Zapisywanie i wersjonowanie modelu
Dominika Liszkiewicz


Polityka wersjonowania modelu.
Pliki zapisywane są według wzoru model_v{x}.joblib, gdzie {x} oznacza numer kolejnej wersji modelu. 
Nowa wersja modelu jest tworzona w sytuacji, gdy:
- zmieniają się dane wejściowe,
- zmieniają się kolumny modelu
- zmianie ulegają parametry modelu
- zmiana algorytmu 

Różnice między środowiskiem deweloperskim a produkcyjnym:
- system w środowisku deweloperskim może popełniać błędy, ale system w środowisku produkcyjnym powinien być niezawodny
- wersjonowanie w środowisku deweloperskim może być ręczne, za to w środowisku produkcyjnym powinno być automatyczne 

Jak można sobie radzić z wyzwaniami?
- można wykorzystywać dockera, aby kod działał tak samo na każdym serwerze
- automatyczne dotrenowywanie modelu
- monitorowanie wyników modelu, w raie wyników ponieżej minimalnego progu informacja do jest wysyłana do inżyniera
- wykorzystywanie gotowych narzęzi jak GitHub Actions aby zapobiegać błędom 
