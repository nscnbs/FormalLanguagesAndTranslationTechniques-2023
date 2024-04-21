import sys

# Implementacja automatu skończonego

class FiniteAutomaton:
    # Funkcja do obliczania funkcji przejścia dla danego wzorca i tekstu
    def compute_transition_function(self, pattern, text):
        m = len(pattern)  # Długość wzorca
        transitions = [{} for _ in range(m + 1)]  # Inicjalizacja tablicy przejść
        for q in range(m + 1):  # Iteracja po stanach automatu
            for a in text:  # Iteracja po znakach tekstu
                k = min(m + 1, q + 1)  # Ustawienie wartości k
                while k > 0 and not (pattern[:q] + a).endswith(pattern[:k]):  # Aktualizacja k dla funkcji przejścia
                    k -= 1
                transitions[q][a] = k  # Zapisanie wyniku do tablicy przejść
            for a in set(text) - set(transitions[q].keys()):  # Dodanie brakujących przejść
                transitions[q][a] = 0
        return transitions  # Zwrócenie tablicy przejść

    # Funkcja wyszukująca wzorzec w tekście za pomocą automatu skończonego
    def search_pattern(self, text, pattern):
        transitions = self.compute_transition_function(pattern, text)  # Obliczenie tablicy przejść
        q = 0  # Inicjalizacja stanu
        results = []  # Inicjalizacja listy wyników
        for i, c in enumerate(text):  # Iteracja po znakach tekstu wraz z indeksem
            q = transitions[q].get(c, 0)  # Aktualizacja stanu zgodnie z tablicą przejść
            print(q)
            if q == len(pattern):  # Sprawdzenie, czy osiągnięto koniec wzorca
                results.append(i - len(pattern) + 1)  # Dodanie indeksu do listy wyników
        return results  # Zwrócenie listy indeksów, na których znaleziono wzorzec

# Wywołanie programu FA
if sys.argv[1] == 'FA':  # Sprawdzenie argumentu wywołania
    fa = FiniteAutomaton()  # Inicjalizacja obiektu automatu skończonego
    with open(sys.argv[2], 'r') as pattern_file:  # Otwarcie pliku z wzorcem do odczytu
        pattern = pattern_file.readline().rstrip()  # Odczyt wzorca z pliku
    filename = sys.argv[3]  # Nazwa pliku podana jako argument wywołania
    with open(filename, 'r') as file:  # Otwarcie pliku do odczytu
        text = file.read().replace('\n', '')  # Odczyt tekstu z pliku
        results = fa.search_pattern(text, pattern)  # Wyszukanie wzorca w tekście
        print("Wzorzec " + pattern + " znaleziono na indeksach:", results)  # Wyświetlenie wyników
