from ScannerProyecto import Scanner


class Main:
    @staticmethod
    def ejecutar():
        # Ejemplo de código fuente de prueba
        codigo = """
inicio
    imprimir("Iniciando prueba del scanner")
    leer(numero)
    
    funcion calcular_valor(x, y)
        si x >= 10.5
            retornar x * y
        sino_si x == 0
            retornar 0
        sino
            retornar x % 2
            
    resultado = calcular_valor(5, numero)
    
    mientras resultado != 100
        resultado = resultado + 1
        
    lista = [1, 2, 3]
    
    @
    
    imprimir("Fin de la prueba")
fin
"""
        scanner = Scanner(codigo)

        try:
            lista_tokens = scanner.scan_tokens()
            for token in lista_tokens:
                # Usamos los nombres de tu Enum TokenType
                print(f"{token.linea:<7} | {token.type.name:<20} | {token.value}")

        except Exception as e:
            print(f"Error durante la ejecución: {e}")


if __name__ == "__main__":
    Main.ejecutar()