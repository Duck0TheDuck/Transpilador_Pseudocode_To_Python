# Generated from Pseudocodigo.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PseudocodigoParser import PseudocodigoParser
else:
    from PseudocodigoParser import PseudocodigoParser

# This class defines a complete listener for a parse tree produced by PseudocodigoParser.
class PseudocodigoListener(ParseTreeListener):

    # Enter a parse tree produced by PseudocodigoParser#programa.
    def enterPrograma(self, ctx:PseudocodigoParser.ProgramaContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#programa.
    def exitPrograma(self, ctx:PseudocodigoParser.ProgramaContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#instruccion.
    def enterInstruccion(self, ctx:PseudocodigoParser.InstruccionContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#instruccion.
    def exitInstruccion(self, ctx:PseudocodigoParser.InstruccionContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#imprimir_stat.
    def enterImprimir_stat(self, ctx:PseudocodigoParser.Imprimir_statContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#imprimir_stat.
    def exitImprimir_stat(self, ctx:PseudocodigoParser.Imprimir_statContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#leer_stat.
    def enterLeer_stat(self, ctx:PseudocodigoParser.Leer_statContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#leer_stat.
    def exitLeer_stat(self, ctx:PseudocodigoParser.Leer_statContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#declaracion_var.
    def enterDeclaracion_var(self, ctx:PseudocodigoParser.Declaracion_varContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#declaracion_var.
    def exitDeclaracion_var(self, ctx:PseudocodigoParser.Declaracion_varContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#declaracion_funcion.
    def enterDeclaracion_funcion(self, ctx:PseudocodigoParser.Declaracion_funcionContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#declaracion_funcion.
    def exitDeclaracion_funcion(self, ctx:PseudocodigoParser.Declaracion_funcionContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#parametros.
    def enterParametros(self, ctx:PseudocodigoParser.ParametrosContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#parametros.
    def exitParametros(self, ctx:PseudocodigoParser.ParametrosContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#llamada_funcion_stat.
    def enterLlamada_funcion_stat(self, ctx:PseudocodigoParser.Llamada_funcion_statContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#llamada_funcion_stat.
    def exitLlamada_funcion_stat(self, ctx:PseudocodigoParser.Llamada_funcion_statContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#argumentos.
    def enterArgumentos(self, ctx:PseudocodigoParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#argumentos.
    def exitArgumentos(self, ctx:PseudocodigoParser.ArgumentosContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#retornar_stat.
    def enterRetornar_stat(self, ctx:PseudocodigoParser.Retornar_statContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#retornar_stat.
    def exitRetornar_stat(self, ctx:PseudocodigoParser.Retornar_statContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#si_stat.
    def enterSi_stat(self, ctx:PseudocodigoParser.Si_statContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#si_stat.
    def exitSi_stat(self, ctx:PseudocodigoParser.Si_statContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#ExprLlamadaFunc.
    def enterExprLlamadaFunc(self, ctx:PseudocodigoParser.ExprLlamadaFuncContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#ExprLlamadaFunc.
    def exitExprLlamadaFunc(self, ctx:PseudocodigoParser.ExprLlamadaFuncContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#ExprEntero.
    def enterExprEntero(self, ctx:PseudocodigoParser.ExprEnteroContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#ExprEntero.
    def exitExprEntero(self, ctx:PseudocodigoParser.ExprEnteroContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#ExprSumaResta.
    def enterExprSumaResta(self, ctx:PseudocodigoParser.ExprSumaRestaContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#ExprSumaResta.
    def exitExprSumaResta(self, ctx:PseudocodigoParser.ExprSumaRestaContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#ExprRelacional.
    def enterExprRelacional(self, ctx:PseudocodigoParser.ExprRelacionalContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#ExprRelacional.
    def exitExprRelacional(self, ctx:PseudocodigoParser.ExprRelacionalContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#ExprParen.
    def enterExprParen(self, ctx:PseudocodigoParser.ExprParenContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#ExprParen.
    def exitExprParen(self, ctx:PseudocodigoParser.ExprParenContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#ExprFlotante.
    def enterExprFlotante(self, ctx:PseudocodigoParser.ExprFlotanteContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#ExprFlotante.
    def exitExprFlotante(self, ctx:PseudocodigoParser.ExprFlotanteContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#ExprCadena.
    def enterExprCadena(self, ctx:PseudocodigoParser.ExprCadenaContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#ExprCadena.
    def exitExprCadena(self, ctx:PseudocodigoParser.ExprCadenaContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#ExprArreglo.
    def enterExprArreglo(self, ctx:PseudocodigoParser.ExprArregloContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#ExprArreglo.
    def exitExprArreglo(self, ctx:PseudocodigoParser.ExprArregloContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#ExprId.
    def enterExprId(self, ctx:PseudocodigoParser.ExprIdContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#ExprId.
    def exitExprId(self, ctx:PseudocodigoParser.ExprIdContext):
        pass


    # Enter a parse tree produced by PseudocodigoParser#ExprMultDivMod.
    def enterExprMultDivMod(self, ctx:PseudocodigoParser.ExprMultDivModContext):
        pass

    # Exit a parse tree produced by PseudocodigoParser#ExprMultDivMod.
    def exitExprMultDivMod(self, ctx:PseudocodigoParser.ExprMultDivModContext):
        pass



del PseudocodigoParser