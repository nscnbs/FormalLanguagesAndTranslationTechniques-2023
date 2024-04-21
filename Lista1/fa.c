#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct FiniteAutomaton
{
    char **transitions;
    int startState;
    int finalState;
};

void init(struct FiniteAutomaton *fa, char *pattern)
{
    int i, j;
    int n = strlen(pattern);
    fa->transitions = (char **)malloc((n + 1) * sizeof(char *));
    fa->startState = 0;
    fa->finalState = n;

    for (i = 0; i <= n; i++)
    {
        fa->transitions[i] = (char *)malloc(256 * sizeof(char));
        for (j = 0; j < 256; j++)
        {
            fa->transitions[i][j] = -1;
        }
    }

    for (i = 0; i < n; i++)
    {
        fa->transitions[i + 1][pattern[i]] = i + 1;
    }
}

int find(struct FiniteAutomaton *fa, char *text)
{
    int i;
    int n = strlen(text);
    int state = fa->startState;

    for (i = 0; i < n; i++)
    {
        char currentChar = text[i];
        if (currentChar < 256 && fa->transitions[state][currentChar] != -1)
        {
            state = fa->transitions[state][currentChar];
            if (state == fa->finalState)
            {
                return 1;
            }
        }
    }

    return 0;
}

int main(int argc, char *argv[])
{
    int i; // Deklaracja zmiennej 'i'
    if (argc != 3)
    {
        printf("Wywołanie: FA <wzorzec> <nazwa pliku>\n");
        exit(1);
    }

    char *pattern = argv[1];
    char *filename = argv[2];

    FILE *file = fopen(filename, "r");
    if (!file)
    {
        printf("Błąd przy otwieraniu pliku\n");
        exit(1);
    }

    fseek(file, 0, SEEK_END);
    long file_size = ftell(file);
    rewind(file);
    char *text = (char *)malloc(file_size * sizeof(char));
    fread(text, sizeof(char), file_size, file);
    fclose(file);

    struct FiniteAutomaton fa;
    init(&fa, pattern);

    if (find(&fa, text))
    {
        printf("Wzór został znaleziony w tekście.\n");
    }
    else
    {
        printf("Wzór nie został znaleziony w tekście.\n");
    }

    free(text);
    for (i = 0; i < fa.finalState; i++)
    {
        free(fa.transitions[i]);
    }
    free(fa.transitions);

    return 0;
}
