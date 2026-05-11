from TokenType import TokenType


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.posicion = 0
        self.token_actual = self.tokens[self.posicion] if self.tokens else None

    # ==========================================
    # MÉTODOS DE NAVEGACIÓN Y CONTROL DE TOKENS
    # ==========================================
    def avanzar(self):
        """Avanza al siguiente token en la lista."""
        self.posicion += 1
        if self.posicion < len(self.tokens):
            self.token_actual = self.tokens[self.posicion]
        else:
            self.token_actual = None

    def consumir(self, tipo_esperado, mensaje_error):
        """Verifica que el token sea el esperado. Si lo es, avanza. Si no, lanza error."""
        if self.token_actual and self.token_actual.type == tipo_esperado:
            token_consumido = self.token_actual
            self.avanzar()
            return token_consumido
        else:
            linea = self.token_actual.linea if self.token_actual else "EOF"
            valor_actual = self.token_actual.value if self.token_actual else "Fin de archivo"
            raise SyntaxError(f"Error Sintáctico en línea {linea}: {mensaje_error}. Se encontró: '{valor_actual}'")

    # ==========================================
    # REGLAS GRAMATICALES (ÁRBOL SINTÁCTICO)
    # ==========================================
    def parse(self):
        """Punto de entrada principal del Parser."""
        # Limpiamos cualquier indentación o salto suelto antes de empezar
        while self.token_actual and self.token_actual.type in (TokenType.TOKEN_INDENT, TokenType.TOKEN_DEDENT):
            self.avanzar()

        # Todo código de tu lenguaje debe estar dentro de un programa
        return self.programa()

    def programa(self):
        """Regla: inicio <declaraciones> fin"""
        # 1. Esperamos obligatoriamente la palabra 'inicio'
        self.consumir(TokenType.KW_INICIO, "Se esperaba la palabra 'inicio' al principio del programa")

        instrucciones = []

        # 2. Leemos instrucciones mientras no encontremos la palabra 'fin' o se acabe el archivo
        while self.token_actual and self.token_actual.type not in (TokenType.KW_FIN, TokenType.TOKEN_EOF):
            # Ignoramos los tokens de indentación por ahora para no ensuciar el AST
            if self.token_actual.type in (TokenType.TOKEN_INDENT, TokenType.TOKEN_DEDENT):
                self.avanzar()
                continue

            instruccion = self.declaracion()
            if instruccion:
                instrucciones.append(instruccion)

        # 3. Esperamos obligatoriamente la palabra 'fin'
        self.consumir(TokenType.KW_FIN, "Se esperaba la palabra 'fin' para cerrar el programa")

        # Devolvemos el nodo principal (El tronco de nuestro Árbol)
        return {"tipo": "Programa", "cuerpo": instrucciones}

    def declaracion(self):
        """Enruta el análisis dependiendo de la palabra clave que encontremos."""
        if self.token_actual.type == TokenType.KW_IMPRIMIR:
            return self.instruccion_imprimir()

        elif self.token_actual.type == TokenType.KW_LEER:
            return self.instruccion_leer()

        # --- NUEVA REGLA AÑADIDA ---
        elif self.token_actual.type == TokenType.KW_FUNCION:
            return self.declaracion_funcion()

        else:
            linea = self.token_actual.linea
            raise SyntaxError(
                f"Error Sintáctico en línea {linea}: Instrucción no reconocida '{self.token_actual.value}'")

    def instruccion_imprimir(self):
        """Regla: imprimir ( <valor> )"""
        self.avanzar()  # Consumimos 'imprimir'

        self.consumir(TokenType.DEL_PAREN_IZQ, "Falta '(' después de 'imprimir'")

        # Leemos el valor (Cadena, ID de variable, Entero o Flotante)
        if self.token_actual.type in (TokenType.LIT_CADENA, TokenType.ID, TokenType.LIT_ENTERO, TokenType.LIT_FLOTANTE):
            valor = self.token_actual.value
            self.avanzar()
        else:
            raise SyntaxError(
                f"Error Sintáctico en línea {self.token_actual.linea}: Se esperaba un valor para imprimir")

        self.consumir(TokenType.DEL_PAREN_DER, "Falta ')' para cerrar el imprimir")

        return {"tipo": "Imprimir", "valor": valor}

    def instruccion_leer(self):
        """Regla: leer ( <variable> )"""
        self.avanzar()  # Consumimos 'leer'

        self.consumir(TokenType.DEL_PAREN_IZQ, "Falta '(' después de 'leer'")

        # A diferencia de imprimir, 'leer' fuerza a que el contenido sea OBLIGATORIAMENTE un ID (una variable)
        if self.token_actual.type == TokenType.ID:
            nombre_variable = self.token_actual.value
            self.avanzar()
        else:
            raise SyntaxError(
                f"Error Sintáctico en línea {self.token_actual.linea}: 'leer' requiere el nombre de una variable, no un número o texto")

        self.consumir(TokenType.DEL_PAREN_DER, "Falta ')' para cerrar el leer")

        return {"tipo": "Leer", "variable": nombre_variable}

    def declaracion_funcion(self):
        """Regla: funcion <id> ( <parametros> ) <bloque>"""
        self.avanzar()  # Consumimos la palabra 'funcion'

        # 1. Leemos el nombre de la función (debe ser un ID)
        token_nombre = self.consumir(TokenType.ID, "Falta el nombre de la función")
        nombre_func = token_nombre.value

        # 2. Leemos los parámetros entre paréntesis
        self.consumir(TokenType.DEL_PAREN_IZQ, "Falta '(' después del nombre de la función")

        parametros = []
        # Si el token que sigue no es un ')', entonces hay parámetros
        if self.token_actual.type != TokenType.DEL_PAREN_DER:
            # Leemos el primer parámetro
            token_param = self.consumir(TokenType.ID, "Se esperaba el nombre de un parámetro")
            parametros.append(token_param.value)

            # Mientras haya comas, seguimos leyendo parámetros
            while self.token_actual.type == TokenType.DEL_COMA:
                self.avanzar()  # Consumimos la ','
                token_param = self.consumir(TokenType.ID, "Se esperaba otro parámetro después de la coma")
                parametros.append(token_param.value)

        self.consumir(TokenType.DEL_PAREN_DER, "Falta ')' para cerrar los parámetros")

        # 3. Leemos todo el código que está adentro de la función
        cuerpo_funcion = self.bloque()

        return {"tipo": "DeclaracionFuncion", "nombre": nombre_func, "parametros": parametros, "cuerpo": cuerpo_funcion}

    def bloque(self):
        """Agrupa instrucciones que están dentro de un nivel de indentación."""
        instrucciones = []

        # Para que sea un bloque válido, debe empezar con un aumento de sangría (INDENT)
        self.consumir(TokenType.TOKEN_INDENT, "Se esperaba que el código estuviera indentado")

        # Seguimos leyendo instrucciones hasta que la sangría regrese a la normalidad (DEDENT)
        while self.token_actual and self.token_actual.type != TokenType.TOKEN_DEDENT:
            inst = self.declaracion()
            if inst:
                instrucciones.append(inst)

        # Consumimos la reducción de sangría
        self.consumir(TokenType.TOKEN_DEDENT, "Se esperaba el fin del bloque indentado")

        return instrucciones