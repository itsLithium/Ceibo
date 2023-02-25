class Token(object):
    INTEGER_TYPE = 'entero'
    REAL_TYPE = 'real'
    INTEGER = 'INTEGER_CONST'
    REAL = 'REAL_CONST'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    MUL = 'MUL'
    INTEGER_DIV = 'INTEGER_DIV'
    FLOAT_DIV = 'FLOAT_DIV'
    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN'
    ID = 'ID'
    ASSIGN = 'ASSIGN'
    BEGIN = 'comenzar'
    END = 'fin'
    SEMI = 'SEMI'
    DOT = 'DOT'
    PROGRAM = 'programa'
    PROCESSES = 'procesos'
    VAR = 'variables'
    COLON = 'COLON'
    COMMA = 'COMMA'
    EOF = 'EOF'

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        """String representation of the class instance."""
        return 'Token({type}, {value})'.format(type=self.type, value=repr(self.value))

    def __repr__(self):
        return self.__str__()


RESERVED_KEYWORDS = {
    'PROGRAMA': Token('programa', 'programa'),
    'VARIABLES': Token('variables', 'variables'),
    'PROCESOS': Token('procesos', 'procesos'),
    'DIV': Token('INTEGER_DIV', 'DIV'),
    'ENTERO': Token('entero', 'entero'),
    'REAL': Token('real', 'real'),
    'COMENZAR': Token('comenzar', 'comenzar'),
    'FIN': Token('fin', 'fin'),
}
