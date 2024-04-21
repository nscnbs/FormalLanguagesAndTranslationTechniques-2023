# Implementacja algorytmu Knutha-Morrisa-Pratta
import sys


# Funkcja obliczająca tablicę lps dla danego wzorca
def compute_lps_array(pattern):
    lps = [0] * len(pattern)  # Inicjalizacja tablicy lps (Najdłuższy wspólny sufiks i prefiks)
    length = 0
    i = 1
    while i < len(pattern):  # Pętla while dla indeksu i
        if pattern[i] == pattern[length]:  # Sprawdzenie warunku porównania znaków
            length += 1  # Zwiększenie length o 1
            lps[i] = length  # Przypisanie wartości length do tablicy lps
            i += 1  # Zwiększenie i o 1
        else:
            if length != 0:  # Sprawdzenie warunku długości wzorca
                length = lps[length - 1]  # Aktualizacja length
            else:
                lps[i] = 0  # Przypisanie 0 do tablicy lps
                i += 1  # Zwiększenie i o 1
    return lps  # Zwrócenie tablicy lps


# Funkcja wyszukująca wzorzec w tekście za pomocą algorytmu Knutha-Morrisa-Pratta
def search_pattern_kmp(text, pattern):
    M = len(pattern)  # Długość wzorca
    N = len(text)  # Długość tekstu
    lps = compute_lps_array(pattern)  # Obliczenie tablicy lps
    j = 0  # Inicjalizacja zmiennej j
    i = 0  # Inicjalizacja zmiennej i
    results = []  # Inicjalizacja listy wyników
    while i < N:  # Pętla while dla indeksu i
        if pattern[j] == text[i]:  # Sprawdzenie warunku porównania znaków
            i += 1  # Zwiększenie i o 1
            j += 1  # Zwiększenie j o 1
        if j == M:  # Sprawdzenie warunku znalezienia wzorca
            if i - j not in results:  # Sprawdzenie, czy indeks nie został już uwzględniony
                results.append(i - j)  # Dodanie indeksu do listy wyników
            j = lps[j - 1]  # Aktualizacja j na podstawie tablicy lps
        elif i < N and pattern[j] != text[i]:  # Sprawdzenie warunku nierówności znaków
            if j != 0:  # Sprawdzenie warunku wartości j
                j = lps[j - 1]  # Aktualizacja j na podstawie tablicy lps
            else:
                i += 1  # Zwiększenie i o 1
    return results  # Zwrócenie listy indeksów, na których znaleziono wzorzec


# Wywołanie programu KMP
if sys.argv[1] == 'KMP':  # Sprawdzenie argumentu wywołania
    with open(sys.argv[2], 'r') as pattern_file:  # Otwarcie pliku z wzorcem do odczytu
        pattern = pattern_file.readline().rstrip()  # Odczyt wzorca z pliku
    filename = sys.argv[3]  # Nazwa pliku podana jako argument wywołania
    with open(filename, 'r') as file:  # Otwarcie pliku do odczytu
        text = file.read()  # Odczyt tekstu z pliku i usunięcie znaków nowej linii
        results_kmp = search_pattern_kmp(text, pattern)  # Wyszukanie wzorca w tekście
        print('Wzorzec "' + pattern + '" znaleziono na indeksach:', results_kmp)  # Wyświetlenie wyników
