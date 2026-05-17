# Generated from Pseudocodigo.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PseudocodigoParser import PseudocodigoParser
else:
    from PseudocodigoParser import PseudocodigoParser

# This class defines a complete generic visitor for a parse tree produced by PseudocodigoParser.

class PseudocodigoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PseudocodigoParser#programa.
    def visitPrograma(self, ctx:PseudocodigoParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#instruccion.
    def visitInstruccion(self, ctx:PseudocodigoParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#imprimir_stat.
    def visitImprimir_stat(self, ctx:PseudocodigoParser.Imprimir_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#leer_stat.
    def visitLeer_stat(self, ctx:PseudocodigoParser.Leer_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#declaracion_var.
    def visitDeclaracion_var(self, ctx:PseudocodigoParser.Declaracion_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#declaracion_funcion.
    def visitDeclaracion_funcion(self, ctx:PseudocodigoParser.Declaracion_funcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#parametros.
    def visitParametros(self, ctx:PseudocodigoParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#llamada_funcion_stat.
    def visitLlamada_funcion_stat(self, ctx:PseudocodigoParser.Llamada_funcion_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#argumentos.
    def visitArgumentos(self, ctx:PseudocodigoParser.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#retornar_stat.
    def visitRetornar_stat(self, ctx:PseudocodigoParser.Retornar_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#si_stat.
    def visitSi_stat(self, ctx:PseudocodigoParser.Si_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#ExprLlamadaFunc.
    def visitExprLlamadaFunc(self, ctx:PseudocodigoParser.ExprLlamadaFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#ExprEntero.
    def visitExprEntero(self, ctx:PseudocodigoParser.ExprEnteroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#ExprSumaResta.
    def visitExprSumaResta(self, ctx:PseudocodigoParser.ExprSumaRestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#ExprRelacional.
    def visitExprRelacional(self, ctx:PseudocodigoParser.ExprRelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#ExprParen.
    def visitExprParen(self, ctx:PseudocodigoParser.ExprParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#ExprFlotante.
    def visitExprFlotante(self, ctx:PseudocodigoParser.ExprFlotanteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#ExprCadena.
    def visitExprCadena(self, ctx:PseudocodigoParser.ExprCadenaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#ExprArreglo.
    def visitExprArreglo(self, ctx:PseudocodigoParser.ExprArregloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#ExprId.
    def visitExprId(self, ctx:PseudocodigoParser.ExprIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PseudocodigoParser#ExprMultDivMod.
    def visitExprMultDivMod(self, ctx:PseudocodigoParser.ExprMultDivModContext):
        return self.visitChildren(ctx)



del PseudocodigoParser