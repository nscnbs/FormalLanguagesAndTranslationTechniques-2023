%option noyywrap
%option nounput
%option noinput

%{
#include "calc_parser.hpp"

int yylex();
%}

BREAK_LINE      \\\n
COMMENT         ^#(.*{BREAK_LINE})*.*$

%%
{COMMENT}                   ;
{BREAK_LINE}                ;
[[:blank:]]+                ;
[0-9]+                      { yylval = atoi(yytext); return NUM; }
\+                          { return ADD; }
\-                          { return SUB; }
\*                          { return MUL; }
\/                          { return DIV; }
\^                          { return POW; }
\(                          { return L_BRA; }
\)                          { return R_BRA; }
\n                          { return EOL; }
.                           { return ERROR; }
%%