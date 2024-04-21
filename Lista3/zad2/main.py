from ply import lex, yacc

import c_lexer as c_lexer
import c_parser


def main():
    l = lex.lex(module=c_lexer)
    p = yacc.yacc(module=c_parser)
    while True:
        user_input = ""
        while True:
            try:
                user_input += input()
            except EOFError:
                return
            user_input += '\n'
            if not user_input.endswith('\\\n'):
                break
        p.parse(user_input, lexer=l)

        
main()