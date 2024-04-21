%{
    #include <stdio.h>
%}

%x TAG  /* Definicja stanu TAG (dla tagow XML) */
%x COM  /* Definicja stanu COM (dla komentarzy) */
%x STR  /* Definicja stanu STR (dla ciagow znakow) */

%%
    /* Obsługa tagów */
"<"                {ECHO; BEGIN(TAG);} /* Zaczyna analizę tagu, przechodzi do stanu TAG */
<TAG>{
    \".*\"|.|\n	    ECHO;  /* ECHO - wypisuje zgodnie z regula, kiedy jestesmy w stanie TAG */
    .> {ECHO; BEGIN(0);}  /* Zakonczenie tagu - przechodzi z powrotem do domyslnego stanu */
}

    /* Obsługa komentarzy */
"<!--"          BEGIN(COM); /* Zaczyna analize komentarza, przechodzi do stanu COM */
<COM>{
.|\n            ;  /* Ignoruje zawartosc komentarza */
"-->"           BEGIN(0);  /* Zakonczenie komentarza - przechodzi z powrotem do domyslnego stanu */
}
    /* Niepoprawny komentarz - pozostawia go nienaruszony */
"<!--".*"--".*"-->" {ECHO;}

%%

int yywrap() {
    return 1;  /* Funkcja zamykająca analizator leksykalny */
}
int main() {
    yyout = fopen("result2.xml", "w");
    yylex();
    return 0;
}
