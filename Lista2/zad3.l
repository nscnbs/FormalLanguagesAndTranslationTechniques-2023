%{
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool docs = false;

%}

%option noyywrap

%%

    /* Single line quotes and pointy brackets <> */
\"[^(\"|\r\n|\n)]*?\"                                      ECHO;
\<[^(\>|\r\n|\n)]*?\>                                      ECHO;

    /* single line docs comments */
[ \t]*\/\/\/(.|\\\r\n|\\\n)*\n                          { if(docs) ECHO; }
[ \t]*\/\/!(.|\\\r\n|\\\n)*\n                           { if(docs) ECHO; }

    /* multiline docs comments */
[ \t]*\/\*\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+\/     { if(docs) ECHO; }
[ \t]*\/\*\!([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+\/     { if(docs) ECHO; }

    /* single and mulitiline normal comments */
[ \t]*"//"(.|\\\r\n|\\\n)*\n                            ;
[ \t]*\/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+\/       ;

.|\n                                                    ECHO;

%%

int main(int argc, char** argv) {
    bool in = false;
    bool out = false;
    if(argc != 3 && argc != 4) {
        printf("Blad: Niepoprawne argumenty, przyklad uzycia: ./zad4.o input.cpp output.cpp [nic v -d]\n");
        return -1;
    } else {
        for(int i = 1; i < argc; i++) {
            if(strcmp(argv[i], "-d") == 0) {
                docs = true;
            } else {
                if (!in) {
                    in = true;
                    yyin = fopen(argv[i], "r");
                } else if (!out) {
                    out = true;
                    yyout = fopen(argv[i], "w");
                }
            }
        }
    }

    yylex();

    if(in) fclose(yyin);
    if(out) fclose(yyout);
    return 0;
}
