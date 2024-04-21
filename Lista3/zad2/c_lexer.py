tokens = (
    'NUM', 'ADD', 'SUB', 'MUL', 'DIV', 'POW', 
    'L_BRA', 'R_BRA', 'EOL', 
    'ERROR', 'COMMENT', 'BREAK_LINE'
)

t_NUM     = r'\d+'
t_ADD     = r'\+'
t_SUB     = r'[-]'
t_MUL     = r'\*'
t_DIV     = r'[/]'
t_POW     = r'\^'
t_L_BRA   = r'\('
t_R_BRA   = r'\)'
t_EOL     = r'\n'
t_ERROR   = r'.'

t_ignore = ' \t'
t_ignore_COMMENT = r'^\#(.*\\\n)*.*$'
t_ignore_BREAK_LINE = r'\\\n'

def t_error(_):
    pass
