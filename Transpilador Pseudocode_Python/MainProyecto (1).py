import json  # <--- 1. AÑADE ESTO AQUÍ
from ScannerProyecto import Scanner
from Sintax_Proyecto import Parser


class Main:
    @staticmethod
    def ejecutar():
        codigo = """
inicio
    funcion sumar(a, b)
        imprimir(a)
        imprimir(b)
fin
"""
        scanner = Scanner(codigo)

        try:
            print("--- TOKENS GENERADOS ---")
            lista_tokens = scanner.scan_tokens()

            for token in lista_tokens:
                print(f"{token.linea:<7} | {token.type.name:<20} | {token.value}")

            print("\n--- EJECUTANDO PARSER ---")
            parser = Parser(lista_tokens)
            arbol_sintactico = parser.parse()

            print("\n--- ÁRBOL SINTÁCTICO (AST) ---")
            # --- 2. CAMBIA LA IMPRESIÓN AQUÍ ---
            # json.dumps formatea el diccionario con sangrías para que parezca un árbol real
            print(json.dumps(arbol_sintactico, indent=4, ensure_ascii=False))

        except SyntaxError as error_sintactico:
            print(f"\n {error_sintactico}")
        except Exception as e:
            print(f"\n Error durante la ejecución: {e}")


if __name__ == "__main__":
    Main.ejecutar()