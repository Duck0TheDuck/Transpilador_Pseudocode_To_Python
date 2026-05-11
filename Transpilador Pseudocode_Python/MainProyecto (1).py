from ScannerProyecto import Scanner

class Main:
    @staticmethod
    def ejecutar():
        # Ejemplo de código fuente de prueba
        codigo = """
inicio
    x = 10.5
    si x > 5
        imprimir "Es mayor"
fin
"""
        scanner = Scanner(codigo)
        try:
            lista_tokens = scanner.scan_tokens()

            print(f"{'LÍNEA':<7} | {'TIPO':<20} | {'VALOR':<15}")
            print("-" * 50)

            for token in lista_tokens:
                # Usamos los nombres de tu Enum TokenType
                print(f"{token.linea:<7} | {token.type.name:<20} | {token.value}")

        except Exception as e:
            print(f"Error durante la ejecución: {e}")


if __name__ == "__main__":
    Main.ejecutar()