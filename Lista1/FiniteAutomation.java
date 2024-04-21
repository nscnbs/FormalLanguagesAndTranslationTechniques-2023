import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class FiniteAutomation {
    // Funkcja do obliczania funkcji przejścia dla danego wzorca
    public Map<Integer, Map<Character, Integer>> computeTransitionFunction(String pattern, String text) {
        int m = pattern.length();  // Długość wzorca
        Map<Integer, Map<Character, Integer>> transitions = new HashMap<>();  // Inicjalizacja pustego słownika dla przechowywania przejść
        for (int q = 0; q <= m; q++) {  // Iteracja po stanie automatu od 0 do długości wzorca
            transitions.put(q, new HashMap<>());  // Inicjalizacja pustego słownika dla danego stanu
            for (int i = 0; i < text.length(); i++) {  // Iteracja po znakach tekstu
                char a = text.charAt(i);
                int k = Math.min(m, q + 1);  // Inicjalizacja zmiennej k na podstawie stanu i długości wzorca
                String subPatternQ = pattern.substring(0, q) + a;  // Konstrukcja podciągu wzorca dla danego stanu i znaku
                while (k > 0 && !subPatternQ.endsWith(pattern.substring(0, k))) {  // Aktualizacja k w zależności od podciągu
                    k--;  // Dekrementacja k
                    subPatternQ = pattern.substring(0, q) + a;  // Aktualizacja podciągu wzorca
                }
                Map<Character, Integer> transitionMap = transitions.get(q);
                transitionMap.put(a, k);  // Przypisanie k do danego przejścia w słowniku
                transitions.put(q, transitionMap);
            }
        }
        return transitions;  // Zwrócenie słownika z tablicą przejść
    }

    // Funkcja wyszukująca wzorzec w tekście za pomocą automatu skończonego
    public List<Integer> searchPattern(String text, String pattern, Map<Integer, Map<Character, Integer>> transitions) {
        int q = 0;  // Inicjalizacja stanu automatu
        List<Integer> results = new ArrayList<>();  // Inicjalizacja pustej listy wyników
        for (int i = 0; i < text.length(); i++) {  // Iteracja po indeksach tekstu
            char c = text.charAt(i);  // Przypisanie aktualnego znaku do zmiennej c
            if (!transitions.containsKey(q) || !transitions.get(q).containsKey(c)) {  // Sprawdzenie czy istnieje przejście dla stanu i znaku
                q = 0;  // Zresetowanie stanu do 0
            } else {
                q = transitions.get(q).get(c);  // Aktualizacja stanu na podstawie przejścia
            }
            if (q == pattern.length()) {  // Sprawdzenie, czy osiągnięto koniec wzorca
                results.add(i - pattern.length() + 1);  // Dodanie indeksu do listy wyników
            }
        }
        return results;  // Zwrócenie listy indeksów, na których znaleziono wzorzec
    }

    // Funkcja do odczytu danych z pliku
    public String readFile(String filename) {
        StringBuilder content = new StringBuilder();
        try {
            BufferedReader reader = new BufferedReader(new FileReader(filename));
            String line;
            while ((line = reader.readLine()) != null) {
                content.append(line);
            }
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return content.toString();
    }

    public static void main(String[] args) {
        if (args.length < 3) {  // Sprawdzenie czy podano odpowiednią liczbę argumentów
            System.out.println("Użycie: java FiniteAutomation <plik_wzorca> <plik_tekstu>");  // Wyświetlenie instrukcji użycia
        } else {
            FiniteAutomation fa = new FiniteAutomation();  // Inicjalizacja obiektu klasy FiniteAutomation
            String pattern = fa.readFile(args[1]);  // Odczyt wzorca z pliku
		String text = fa.readFile(args[2]);  // Odczyt tekstu z pliku
            Map<Integer, Map<Character, Integer>> transitions = fa.computeTransitionFunction(pattern, text);  // Obliczenie tablicy przejść dla danego wzorca i tekstu
            List<Integer> results = fa.searchPattern(text, pattern, transitions);  // Wyszukanie wzorca w tekście
            System.out.print("Wzorzec \"" + pattern + "\" znaleziono na indeksach: " + results);  // Wyświetlenie wyników
        }
    }
}
