from dataclasses import dataclass
from typing import Any
from TokenType import TokenType


@dataclass
class Token:
    type: TokenType
    value: Any
    linea: int
    columna: int
    posicion: int

    def __str__(self):
        return f"Token(type={self.type}, value={self.value}, linea={self.linea}, columna={self.columna}, posicion={self.posicion})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.type == other.type

    def is_type(self, token_type: TokenType) -> bool:
        return self.type == token_type

    # Palabras Reservadad/Keywords
    def is_KW_SI(self) -> bool: return self.is_type(TokenType.KW_SI)

    def is_KW_SINO_SI(self) -> bool: return self.is_type(TokenType.KW_SINO_SI)

    def is_KW_SINO(self) -> bool: return self.is_type(TokenType.KW_SINO)

    def is_KW_MIENTRAS(self) -> bool: return self.is_type(TokenType.KW_MIENTRAS)

    def is_KW_PARA(self) -> bool: return self.is_type(TokenType.KW_PARA)

    def is_KW_EN(self) -> bool: return self.is_type(TokenType.KW_EN)

    def is_KW_FUNCION(self) -> bool: return self.is_type(TokenType.KW_FUNCION)

    def is_KW_RETORNAR(self) -> bool: return self.is_type(TokenType.KW_RETORNAR)

    def is_KW_IMPRIMIR(self) -> bool: return self.is_type(TokenType.KW_IMPRIMIR)

    def is_KW_LEER(self) -> bool: return self.is_type(TokenType.KW_LEER)

    def is_KW_INICIO(self) -> bool: return self.is_type(TokenType.KW_INICIO)

    def is_KW_FIN(self) -> bool: return self.is_type(TokenType.KW_FIN)

    # Operadores Aritméticos
    def is_OP_SUMA(self) -> bool: return self.is_type(TokenType.OP_SUMA)

    def is_OP_RESTA(self) -> bool: return self.is_type(TokenType.OP_RESTA)

    def is_OP_MULT(self) -> bool: return self.is_type(TokenType.OP_MULT)

    def is_OP_DIV(self) -> bool: return self.is_type(TokenType.OP_DIV)

    def is_OP_MODULO(self) -> bool: return self.is_type(TokenType.OP_MODULO)

    # Operadores Relacionales
    def is_OP_IGUAL(self) -> bool: return self.is_type(TokenType.OP_IGUAL)

    def is_OP_DIFERENTE(self) -> bool: return self.is_type(TokenType.OP_DIFERENTE)

    def is_OP_MAYOR(self) -> bool: return self.is_type(TokenType.OP_MAYOR)

    def is_OP_MENOR(self) -> bool: return self.is_type(TokenType.OP_MENOR)

    def is_OP_MAYOR_IG(self) -> bool: return self.is_type(TokenType.OP_MAYOR_IG)

    def is_OP_MENOR_IG(self) -> bool: return self.is_type(TokenType.OP_MENOR_IG)

    # Operadores Lógicos y Asignación
    def is_OP_Y(self) -> bool: return self.is_type(TokenType.OP_Y)

    def is_OP_O(self) -> bool: return self.is_type(TokenType.OP_O)

    def is_OP_NO(self) -> bool: return self.is_type(TokenType.OP_NO)

    def is_OP_ASIGNACION(self) -> bool: return self.is_type(TokenType.OP_ASIGNACION)

    # --- Tipos de Datos (Literales) ---
    def is_LIT_ENTERO(self) -> bool: return self.is_type(TokenType.LIT_ENTERO)

    def is_LIT_FLOTANTE(self) -> bool: return self.is_type(TokenType.LIT_FLOTANTE)

    def is_LIT_CADENA(self) -> bool: return self.is_type(TokenType.LIT_CADENA)

    def is_LIT_VERDADERO(self) -> bool: return self.is_type(TokenType.LIT_VERDADERO)

    def is_LIT_FALSO(self) -> bool: return self.is_type(TokenType.LIT_FALSO)

    # Identificadores
    def is_ID(self) -> bool: return self.is_type(TokenType.ID)

    # Delimitadores
    def is_DEL_PAREN_IZQ(self) -> bool: return self.is_type(TokenType.DEL_PAREN_IZQ)

    def is_DEL_PAREN_DER(self) -> bool: return self.is_type(TokenType.DEL_PAREN_DER)

    def is_DEL_CORCH_IZQ(self) -> bool: return self.is_type(TokenType.DEL_CORCH_IZQ)

    def is_DEL_CORCH_DER(self) -> bool: return self.is_type(TokenType.DEL_CORCH_DER)

    def is_DEL_COMA(self) -> bool: return self.is_type(TokenType.DEL_COMA)

    # Tokens Especiales de Control
    def is_TOKEN_INDENT(self) -> bool: return self.is_type(TokenType.TOKEN_INDENT)

    def is_TOKEN_DEDENT(self) -> bool: return self.is_type(TokenType.TOKEN_DEDENT)

    def is_TOKEN_EOF(self) -> bool: return self.is_type(TokenType.TOKEN_EOF)

    def is_TOKEN_ERROR(self) -> bool: return self.is_type(TokenType.TOKEN_ERROR)

    #Funciones de Clasificación

    def is_paReservada(self) -> bool:
        return self.type in [
            TokenType.KW_SI, TokenType.KW_SINO_SI, TokenType.KW_SINO,
            TokenType.KW_MIENTRAS, TokenType.KW_PARA, TokenType.KW_EN,
            TokenType.KW_FUNCION, TokenType.KW_RETORNAR, TokenType.KW_IMPRIMIR,
            TokenType.KW_LEER, TokenType.KW_INICIO, TokenType.KW_FIN
        ]

    def is_opAritmetico(self) -> bool:
        return self.type in [
            TokenType.OP_SUMA, TokenType.OP_RESTA, TokenType.OP_MULT,
            TokenType.OP_DIV, TokenType.OP_MODULO
        ]

    def is_opRelacional(self) -> bool:
        return self.type in [
            TokenType.OP_IGUAL, TokenType.OP_DIFERENTE, TokenType.OP_MAYOR,
            TokenType.OP_MENOR, TokenType.OP_MAYOR_IG, TokenType.OP_MENOR_IG
        ]

    def is_opLogico(self) -> bool:
        return self.type in [
            TokenType.OP_Y, TokenType.OP_O, TokenType.OP_NO
        ]

    def is_Operator(self) -> bool:
        return (self.is_opAritmetico() or
                self.is_opRelacional() or
                self.is_opLogico() or
                self.type == TokenType.OP_ASIGNACION)

    def is_delimitador(self) -> bool:
        return self.type in [
            TokenType.DEL_PAREN_IZQ, TokenType.DEL_PAREN_DER,
            TokenType.DEL_CORCH_IZQ, TokenType.DEL_CORCH_DER,
            TokenType.DEL_COMA
        ]

    def is_tipoDato(self) -> bool:
        return self.type in [
            TokenType.LIT_ENTERO, TokenType.LIT_FLOTANTE, TokenType.LIT_CADENA,
            TokenType.LIT_VERDADERO, TokenType.LIT_FALSO
        ]

    def is_especial(self) -> bool:
        return self.type in [
            TokenType.TOKEN_INDENT, TokenType.TOKEN_DEDENT,
            TokenType.TOKEN_EOF, TokenType.TOKEN_ERROR
        ]

    # Utilidades de coincidencia
    def has_value(self, expected_value: Any) -> bool:
        return self.value == expected_value

    def match(self, token_type: TokenType, value: Any = None) -> bool:
        if value is None:
            return self.is_type(token_type)
        return self.has_value(value) and self.is_type(token_type)

