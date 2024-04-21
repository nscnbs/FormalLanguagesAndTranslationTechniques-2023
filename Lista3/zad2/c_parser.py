from c_lexer import tokens
from g_field import GaloisField

GF_ORDER = 1234577
gf = GaloisField(GF_ORDER)
exp_gf = GaloisField(GF_ORDER - 1)

tokens = tokens[:-3]

rpn = []
errorMessage = ''

precedence = (
    ('left', 'ADD', 'SUB'),
    ('left', 'MUL', 'DIV'),
    ('right', 'NEG'),
    ('right', 'POW')
)

def p_line_expression(p):
    'line : expression EOL'
    global rpn, errorMessage
    if errorMessage != '':
        print(''.join(rpn))
        print(errorMessage)
    else:
        print(''.join(rpn))
        print(f'Result: {p[1]}')

    rpn = []
    errorMessage = ''

def p_line_error(p):
    'line : error EOL'
    global rpn, errorMessage
    if errorMessage != '':
        print(errorMessage)

    rpn = []
    errorMessage = ''

def p_line_eol(p):
    'line : EOL'
    pass

def p_expression_num(p):
    'expression : NUM'
    global rpn, gf
    num = gf.convert_to_field_element(int(p[1]))
    rpn.append(f'{num} ')
    p[0] = p[1] = num

def p_expression_parent(p):
    'expression : L_BRA expression R_BRA'
    p[0] = p[2]

def p_expression_add(p):
    'expression : expression ADD expression'
    global rpn, gf
    rpn.append('+ ')
    p[0] = gf.add(p[1], p[3])

def p_expression_sub(p):
    'expression : expression SUB expression'
    global rpn, gf
    rpn.append('- ')
    p[0] = gf.subtract(p[1], p[3])

def p_expression_mul(p):
    'expression : expression MUL expression'
    global rpn, gf
    rpn.append('* ')
    p[0] = gf.multiply(p[1], p[3])

def p_expression_div(p):
    'expression : expression DIV expression'
    global rpn, errorMessage, gf
    rpn.append('/ ')
    result = gf.divide(p[1], p[3])
    if result is None:
        errorMessage = f'ERROR: {p[3]} is not invertible in GF({GF_ORDER})'
        raise SyntaxError
    else:
        p[0] = result

def p_expression_neg(p):
    'expression : SUB expression %prec NEG'
    global rpn, gf
    rpn = rpn[:-1]
    rpn.append(str(gf.opposite(p[2])) + ' ')
    p[0] = gf.opposite(p[2])

def p_expression_pow(p):
    'expression : expression POW exponent'
    global rpn, gf
    rpn.append('^ ')
    p[0] = gf.power(p[1], p[3])

def p_exponent_num(p):
    'exponent : NUM'
    global rpn, exp_gf
    num = exp_gf.convert_to_field_element(int(p[1]))
    rpn.append(f'{num} ')
    p[0] = p[1] = num

def p_exponent_parent(p):
    'exponent : L_BRA exponent R_BRA'
    p[0] = p[2]

def p_exponent_add(p):
    'exponent : exponent ADD exponent'
    global rpn, exp_gf
    rpn.append('+ ')
    p[0] = exp_gf.add(p[1], p[3])

def p_exponent_sub(p):
    'exponent : exponent SUB exponent'
    global rpn, exp_gf
    rpn.append('- ')
    p[0] = exp_gf.subtract(p[1], p[3])

def p_exponent_mul(p):
    'exponent : exponent MUL exponent'
    global rpn, exp_gf
    rpn.append('* ')
    p[0] = exp_gf.multiply(p[1], p[3])

def p_exponent_div(p):
    'exponent : exponent DIV exponent'
    global rpn, errorMessage, exp_gf
    rpn.append('/ ')
    result = exp_gf.divide(p[1], p[3])
    if result is None:
        errorMessage = f'ERROR: {p[3]} is not invertible in GF({GF_ORDER-1})'
        raise SyntaxError
    else:
        p[0] = result

def p_exponent_neg(p):
    'exponent : SUB exponent %prec NEG'
    global rpn, exp_gf
    rpn = rpn[:-1]
    rpn.append(str(exp_gf.opposite(p[2])) + ' ')
    p[0] = exp_gf.opposite(p[2])

def p_error(p):
    global rpn, errorMessage
    print('ERROR: Invalid syntax')
    rpn = []
    errorMessage = ''