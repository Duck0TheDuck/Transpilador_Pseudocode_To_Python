from enum import Enum, auto

class TokenType(Enum):

        # Palabras Reservadas
        KW_SI = auto()
        KW_SINO_SI = auto()
        KW_SINO = auto()
        KW_MIENTRAS = auto()
        KW_PARA = auto()
        KW_EN = auto()
        KW_FUNCION = auto()
        KW_RETORNAR = auto()
        KW_IMPRIMIR = auto()
        KW_LEER = auto()
        KW_INICIO = auto()
        KW_FIN = auto()

        # Operadores Aritméticos
        OP_SUMA = auto()
        OP_RESTA = auto()
        OP_MULT = auto()
        OP_DIV = auto()
        OP_MODULO = auto()

        # Operadores Relacionales
        OP_IGUAL = auto()
        OP_DIFERENTE = auto()
        OP_MAYOR = auto()
        OP_MENOR = auto()
        OP_MAYOR_IG = auto()
        OP_MENOR_IG = auto()

        # Operadores Lógicos y Asignación
        OP_Y = auto()
        OP_O = auto()
        OP_NO = auto()
        OP_ASIGNACION = auto()

        # Tipo de dato
        LIT_ENTERO = auto()
        LIT_FLOTANTE = auto()
        LIT_CADENA = auto()
        LIT_VERDADERO = auto()
        LIT_FALSO = auto()
        # Identificadores
        ID = auto()
        # Delimitadores
        DEL_PAREN_IZQ = auto()
        DEL_PAREN_DER = auto()
        DEL_CORCH_IZQ = auto()
        DEL_CORCH_DER = auto()
        DEL_COMA = auto()

        # Tokens Especiales de Control
        TOKEN_INDENT = auto()
        TOKEN_DEDENT = auto()
        TOKEN_EOF = auto()
        TOKEN_ERROR = auto()