# PJN lab1

1. Korpus dokumentów utworzony jest poprzez funkcję request wszystkie dokumenty przechowywane są w osobnych zmiennych, na ich podstawie utworzyłem plik bag-of-words i bag-of-chars ktroe odpowiednio zawieraja w sobie liczbę występowania poszczególnych wyrazów oraz liter we wszystkich dokumentach łącznie pozwoliłoby to na obliczenie entropii wystepowania znaków / wyrazów lub obliczenie term frequency w kontekście całego korpusu.

2. W folderze zatytułowanym wykresy znajdują się wykresy utworzone na podstawie 10 najczesciej wystepujących wyrazów w każdym dokumencie, modyfikacja funkcji rysującej może sprawić, że więcej wyrazów będzie branych pod uwagę w trakcie tworzenia wykresu, wiąże się to jednak z koniecznością obrócenia 'labeli' na osi x w celu umożliwienia jakiejkolwiek przejrzystości. Osobiście uznałem, że w celu zilustrowania rozkładu empirycznego charakterystycznego dla prawa Ziph'a 10 najpopularniejszych wyrazów całkowicie wystarcza. Wniosek : Rozkład empiryczny pokrywa się z prawem Ziph'a

3. W linijkach 83-97 dokumenty przekształcane są na zmienne haszofalne ( slownikiowe )
jednoczześnie porównując czy dany wyraz nie występuje w stopliście dodanej jako osobny plik oraz inicjalizowanej do programu w linijce 9-21.

4. Utworzone funkcje TF - term frequency oraz IDF - inverted document frequency pozwalają na obliczenie korespondujących wartości dla zmiennych słownikowych oraz zwracają obliczoną wartość w postaci key value ; gdzie value jest odpowiednio wartością TF , IDF w zależności od zastosowanej funkcji. Następnie funkcji tf_idf
pobierane są tylko wartości słownika ponieważ kolejność kluczy jest spójna z kolejnością kluczy w podanym słowniku stąd wykorzystanie build-inu .values() i przerobienie zmiennej słownikowej na na listę w celu możliwości odwołania się iteracyjnego. Następnie wartości te są przemnażane do siebie i umieszczane w nowej zmiennej słownikowej o postaci key : tf_idf. Nie dokonywałem złączenia poszczególnych macierzy tf_idf ponieważ pozostała część programu została napisana została z uwzglednieniem występowania wielu macierzy tf_idf jednowymiarowych.

5. Jako że dokumenty mają różną długość w funkcji odległość_cos porównuje długość macierzy następnie podstawiam kolejne wartości do wzoru w celu obliczenia odległości, zabezpieczenie funkcji przed podziałem na 0 wynika z początkowego błedu w implementacji źle zaindeksowałem warunek przeciwny naturalnie nie będzie miało miejsce dzielenia przez 0 ale postanowiłem pozostawić tą funkcjonalność funkcji.
Obliczone wartości umieszczam w macierzy dwu wymiarowej ze śladem None w celu prostej analizy otrzymanych wyników.

6. Jako że z założenia pisałem program z myślą o ograniczeniu korzystania z funkcji zewnętrznych takich jak vectorizer(), nie wystarczyło mi czasu na implemnetację ręczną tego podpunktu (nie mam pomysłu z której strony to ugryźć to zagadnienie pod kątem implementacyjnym na podtawie znalezionych informacji, mimo iż rozumiem ideę redukcji wymiarów PCA) 

7. Podobieństwo cosinusowe w porównaniu z macierzami tf-idf dają bardzo zbliżone wyniki na podstawie uzyskanych wyników można stwiedzić żże najbardziej podobne do siebie teksty to anioł i poetyka.

UWAGI : W zestawieniu podobieństwa tekstów jak i macierzy TF-IDF nie brałem pod uwagę tesktu dolina trwogi; z niewiadomych dla mnie przyczyn przy tymtekscie otrzymywałem błąd segmentacji wynikający z przekroczenia indeksu zmiennych co moim zdaniem w mojej implementacji nie ma prawa bytu oraz nie wyjaśnia to dlaczego dla pozostałych tekstów program działa poprawnie.
