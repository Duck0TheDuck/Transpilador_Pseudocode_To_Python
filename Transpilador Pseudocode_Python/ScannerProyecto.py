import re
from TokenType import TokenType
from Tokens import Token


class Scanner:
    def __init__(self, source: str):
        self.source = source
        self.tokens = []
        self.linea = 1
        self.columna = 1
        self.posicion = 0
        self.indent_stack = [0]  # Pila para rastrear niveles de espacio

        # Diccionario de Palabras Reservadas (Keywords)
        self.keywords = {
            "si": TokenType.KW_SI, "sino_si": TokenType.KW_SINO_SI, "sino": TokenType.KW_SINO,
            "mientras": TokenType.KW_MIENTRAS, "para": TokenType.KW_PARA, "en": TokenType.KW_EN,
            "funcion": TokenType.KW_FUNCION, "retornar": TokenType.KW_RETORNAR,
            "imprimir": TokenType.KW_IMPRIMIR, "leer": TokenType.KW_LEER,
            "inicio": TokenType.KW_INICIO, "fin": TokenType.KW_FIN
        }

    def scan_tokens(self):
        # Dividimos el código por líneas para manejar la indentación fácilmente
        lineas = self.source.split('\n')

        for num_linea, contenido in enumerate(lineas, 1):
            self.linea = num_linea
            if not contenido.strip():  # Saltar líneas vacías
                continue

            # --- Lógica de Indentación (TOKEN_INDENT / TOKEN_DEDENT) ---
            espacios = len(contenido) - len(contenido.lstrip())
            if espacios > self.indent_stack[-1]:
                self.indent_stack.append(espacios)
                self.tokens.append(Token(TokenType.TOKEN_INDENT, espacios, self.linea, 0, 0))
            elif espacios < self.indent_stack[-1]:
                while espacios < self.indent_stack[-1]:
                    self.indent_stack.pop()
                    self.tokens.append(Token(TokenType.TOKEN_DEDENT, espacios, self.linea, 0, 0))

            # --- Análisis de la línea (Tokens individuales) ---
            self._procesar_linea(contenido.strip())

        # Al final, cerrar todas las indentaciones abiertas y añadir EOF
        while len(self.indent_stack) > 1:
            self.indent_stack.pop()
            self.tokens.append(Token(TokenType.TOKEN_DEDENT, 0, self.linea, 0, 0))

        self.tokens.append(Token(TokenType.TOKEN_EOF, "EOF", self.linea, 0, 0))
        return self.tokens

    def _procesar_linea(self, texto):
        # Aquí usamos expresiones regulares para identificar tus tokens
        patrones = [
            (TokenType.LIT_CADENA, r'"[^"]*"'),
            (TokenType.LIT_FLOTANTE, r'\d+\.\d+'),
            (TokenType.LIT_ENTERO, r'\d+'),
            (TokenType.OP_IGUAL, r'=='),
            (TokenType.OP_DIFERENTE, r'!='),
            (TokenType.OP_MAYOR_IG, r'>='),
            (TokenType.OP_MENOR_IG, r'<='),
            (TokenType.OP_ASIGNACION, r'='),
            (TokenType.OP_MAYOR, r'>'),
            (TokenType.OP_MENOR, r'<'),
            (TokenType.OP_SUMA, r'\+'),
            (TokenType.OP_RESTA, r'-'),
            (TokenType.OP_MULT, r'\*'),
            (TokenType.OP_DIV, r'/'),
            (TokenType.OP_MODULO, r'%'),
            (TokenType.DEL_PAREN_IZQ, r'\('),
            (TokenType.DEL_PAREN_DER, r'\)'),
            (TokenType.DEL_CORCH_IZQ, r'\['),
            (TokenType.DEL_CORCH_DER, r'\]'),
            (TokenType.DEL_COMA, r','),
            # Identificadores: Letra/guion seguido de letras/números
            (TokenType.ID, r'[a-zA-Z_][a-zA-Z0-9_]*')
        ]

        cursor = 0
        while cursor < len(texto):
            if texto[cursor].isspace():
                cursor += 1
                continue

            match_found = False
            for tipo, patron in patrones:
                regex = re.compile(patron)
                match = regex.match(texto, cursor)
                if match:
                    valor = match.group(0)
                    # Si es un ID, checar si es una Palabra Reservada
                    if tipo == TokenType.ID and valor in self.keywords:
                        tipo = self.keywords[valor]

                    # Usar tu clase Token
                    nuevo_token = Token(tipo, valor, self.linea, cursor + 1, cursor)
                    self.tokens.append(nuevo_token)
                    cursor = match.end()
                    match_found = True
                    break

            if not match_found:
                # Se reporta la línea y columna exacta del error
                columna_error = cursor + 1
                simbolo = texto[cursor]
                print(f"Error Léxico: Símbolo desconocido '{simbolo}' en línea {self.linea}, columna {columna_error}")

                # Se añade a la lista de tokens para que el Parser o el sistema lo detecte
                self.tokens.append(Token(TokenType.TOKEN_ERROR, simbolo, self.linea, columna_error, cursor))

                cursor += 1