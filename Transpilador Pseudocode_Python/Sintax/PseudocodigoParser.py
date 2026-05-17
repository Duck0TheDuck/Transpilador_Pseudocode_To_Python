# Generated from Pseudocodigo.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,34,169,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,5,0,27,8,0,
        10,0,12,0,30,9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,42,
        8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,
        1,5,1,5,1,5,3,5,62,8,5,1,5,1,5,5,5,66,8,5,10,5,12,5,69,9,5,1,5,1,
        5,1,6,1,6,1,6,5,6,76,8,6,10,6,12,6,79,9,6,1,7,1,7,1,7,3,7,84,8,7,
        1,7,1,7,1,8,1,8,1,8,5,8,91,8,8,10,8,12,8,94,9,8,1,9,1,9,1,9,1,10,
        1,10,1,10,1,10,5,10,103,8,10,10,10,12,10,106,9,10,1,10,1,10,1,10,
        1,10,5,10,112,8,10,10,10,12,10,115,9,10,5,10,117,8,10,10,10,12,10,
        120,9,10,1,10,1,10,5,10,124,8,10,10,10,12,10,127,9,10,3,10,129,8,
        10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,141,8,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,153,8,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,164,8,11,10,
        11,12,11,167,9,11,1,11,0,1,22,12,0,2,4,6,8,10,12,14,16,18,20,22,
        0,3,1,0,25,27,1,0,23,24,2,0,16,19,21,22,183,0,24,1,0,0,0,2,41,1,
        0,0,0,4,43,1,0,0,0,6,48,1,0,0,0,8,53,1,0,0,0,10,57,1,0,0,0,12,72,
        1,0,0,0,14,80,1,0,0,0,16,87,1,0,0,0,18,95,1,0,0,0,20,98,1,0,0,0,
        22,152,1,0,0,0,24,28,5,1,0,0,25,27,3,2,1,0,26,25,1,0,0,0,27,30,1,
        0,0,0,28,26,1,0,0,0,28,29,1,0,0,0,29,31,1,0,0,0,30,28,1,0,0,0,31,
        32,5,2,0,0,32,33,5,0,0,1,33,1,1,0,0,0,34,42,3,4,2,0,35,42,3,6,3,
        0,36,42,3,8,4,0,37,42,3,10,5,0,38,42,3,14,7,0,39,42,3,20,10,0,40,
        42,3,18,9,0,41,34,1,0,0,0,41,35,1,0,0,0,41,36,1,0,0,0,41,37,1,0,
        0,0,41,38,1,0,0,0,41,39,1,0,0,0,41,40,1,0,0,0,42,3,1,0,0,0,43,44,
        5,3,0,0,44,45,5,28,0,0,45,46,3,22,11,0,46,47,5,29,0,0,47,5,1,0,0,
        0,48,49,5,4,0,0,49,50,5,28,0,0,50,51,5,33,0,0,51,52,5,29,0,0,52,
        7,1,0,0,0,53,54,5,33,0,0,54,55,5,20,0,0,55,56,3,22,11,0,56,9,1,0,
        0,0,57,58,5,5,0,0,58,59,5,33,0,0,59,61,5,28,0,0,60,62,3,12,6,0,61,
        60,1,0,0,0,61,62,1,0,0,0,62,63,1,0,0,0,63,67,5,29,0,0,64,66,3,2,
        1,0,65,64,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,70,
        1,0,0,0,69,67,1,0,0,0,70,71,5,6,0,0,71,11,1,0,0,0,72,77,5,33,0,0,
        73,74,5,32,0,0,74,76,5,33,0,0,75,73,1,0,0,0,76,79,1,0,0,0,77,75,
        1,0,0,0,77,78,1,0,0,0,78,13,1,0,0,0,79,77,1,0,0,0,80,81,5,33,0,0,
        81,83,5,28,0,0,82,84,3,16,8,0,83,82,1,0,0,0,83,84,1,0,0,0,84,85,
        1,0,0,0,85,86,5,29,0,0,86,15,1,0,0,0,87,92,3,22,11,0,88,89,5,32,
        0,0,89,91,3,22,11,0,90,88,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,92,
        93,1,0,0,0,93,17,1,0,0,0,94,92,1,0,0,0,95,96,5,7,0,0,96,97,3,22,
        11,0,97,19,1,0,0,0,98,99,5,8,0,0,99,100,3,22,11,0,100,104,5,9,0,
        0,101,103,3,2,1,0,102,101,1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,
        0,104,105,1,0,0,0,105,118,1,0,0,0,106,104,1,0,0,0,107,108,5,10,0,
        0,108,109,3,22,11,0,109,113,5,9,0,0,110,112,3,2,1,0,111,110,1,0,
        0,0,112,115,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,117,1,0,
        0,0,115,113,1,0,0,0,116,107,1,0,0,0,117,120,1,0,0,0,118,116,1,0,
        0,0,118,119,1,0,0,0,119,128,1,0,0,0,120,118,1,0,0,0,121,125,5,11,
        0,0,122,124,3,2,1,0,123,122,1,0,0,0,124,127,1,0,0,0,125,123,1,0,
        0,0,125,126,1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,128,121,1,0,
        0,0,128,129,1,0,0,0,129,130,1,0,0,0,130,131,5,12,0,0,131,21,1,0,
        0,0,132,133,6,11,-1,0,133,134,5,28,0,0,134,135,3,22,11,0,135,136,
        5,29,0,0,136,153,1,0,0,0,137,138,5,33,0,0,138,140,5,28,0,0,139,141,
        3,16,8,0,140,139,1,0,0,0,140,141,1,0,0,0,141,142,1,0,0,0,142,153,
        5,29,0,0,143,144,5,33,0,0,144,145,5,30,0,0,145,146,3,22,11,0,146,
        147,5,31,0,0,147,153,1,0,0,0,148,153,5,33,0,0,149,153,5,15,0,0,150,
        153,5,14,0,0,151,153,5,13,0,0,152,132,1,0,0,0,152,137,1,0,0,0,152,
        143,1,0,0,0,152,148,1,0,0,0,152,149,1,0,0,0,152,150,1,0,0,0,152,
        151,1,0,0,0,153,165,1,0,0,0,154,155,10,10,0,0,155,156,7,0,0,0,156,
        164,3,22,11,11,157,158,10,9,0,0,158,159,7,1,0,0,159,164,3,22,11,
        10,160,161,10,8,0,0,161,162,7,2,0,0,162,164,3,22,11,9,163,154,1,
        0,0,0,163,157,1,0,0,0,163,160,1,0,0,0,164,167,1,0,0,0,165,163,1,
        0,0,0,165,166,1,0,0,0,166,23,1,0,0,0,167,165,1,0,0,0,16,28,41,61,
        67,77,83,92,104,113,118,125,128,140,152,163,165
    ]

class PseudocodigoParser ( Parser ):

    grammarFileName = "Pseudocodigo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'inicio'", "'fin'", "'imprimir'", "'leer'", 
                     "'funcion'", "'fin_funcion'", "'retornar'", "'si'", 
                     "'entonces'", "'sino_si'", "'sino'", "'fin_si'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'=='", "'!='", "'>='", "'<='", 
                     "'='", "'>'", "'<'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "KW_INICIO", "KW_FIN", "KW_IMPRIMIR", 
                      "KW_LEER", "KW_FUNCION", "KW_FIN_FUNCION", "KW_RETORNAR", 
                      "KW_SI", "KW_ENTONCES", "KW_SINO_SI", "KW_SINO", "KW_FIN_SI", 
                      "LIT_CADENA", "LIT_FLOTANTE", "LIT_ENTERO", "OP_IGUAL", 
                      "OP_DIFERENTE", "OP_MAYOR_IG", "OP_MENOR_IG", "OP_ASIGNACION", 
                      "OP_MAYOR", "OP_MENOR", "OP_SUMA", "OP_RESTA", "OP_MULT", 
                      "OP_DIV", "OP_MODULO", "DEL_PAREN_IZQ", "DEL_PAREN_DER", 
                      "DEL_CORCH_IZQ", "DEL_CORCH_DER", "DEL_COMA", "ID", 
                      "WS" ]

    RULE_programa = 0
    RULE_instruccion = 1
    RULE_imprimir_stat = 2
    RULE_leer_stat = 3
    RULE_declaracion_var = 4
    RULE_declaracion_funcion = 5
    RULE_parametros = 6
    RULE_llamada_funcion_stat = 7
    RULE_argumentos = 8
    RULE_retornar_stat = 9
    RULE_si_stat = 10
    RULE_expresion = 11

    ruleNames =  [ "programa", "instruccion", "imprimir_stat", "leer_stat", 
                   "declaracion_var", "declaracion_funcion", "parametros", 
                   "llamada_funcion_stat", "argumentos", "retornar_stat", 
                   "si_stat", "expresion" ]

    EOF = Token.EOF
    KW_INICIO=1
    KW_FIN=2
    KW_IMPRIMIR=3
    KW_LEER=4
    KW_FUNCION=5
    KW_FIN_FUNCION=6
    KW_RETORNAR=7
    KW_SI=8
    KW_ENTONCES=9
    KW_SINO_SI=10
    KW_SINO=11
    KW_FIN_SI=12
    LIT_CADENA=13
    LIT_FLOTANTE=14
    LIT_ENTERO=15
    OP_IGUAL=16
    OP_DIFERENTE=17
    OP_MAYOR_IG=18
    OP_MENOR_IG=19
    OP_ASIGNACION=20
    OP_MAYOR=21
    OP_MENOR=22
    OP_SUMA=23
    OP_RESTA=24
    OP_MULT=25
    OP_DIV=26
    OP_MODULO=27
    DEL_PAREN_IZQ=28
    DEL_PAREN_DER=29
    DEL_CORCH_IZQ=30
    DEL_CORCH_DER=31
    DEL_COMA=32
    ID=33
    WS=34

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_INICIO(self):
            return self.getToken(PseudocodigoParser.KW_INICIO, 0)

        def KW_FIN(self):
            return self.getToken(PseudocodigoParser.KW_FIN, 0)

        def EOF(self):
            return self.getToken(PseudocodigoParser.EOF, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudocodigoParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(PseudocodigoParser.InstruccionContext,i)


        def getRuleIndex(self):
            return PseudocodigoParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = PseudocodigoParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(PseudocodigoParser.KW_INICIO)
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8589935032) != 0):
                self.state = 25
                self.instruccion()
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 31
            self.match(PseudocodigoParser.KW_FIN)
            self.state = 32
            self.match(PseudocodigoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def imprimir_stat(self):
            return self.getTypedRuleContext(PseudocodigoParser.Imprimir_statContext,0)


        def leer_stat(self):
            return self.getTypedRuleContext(PseudocodigoParser.Leer_statContext,0)


        def declaracion_var(self):
            return self.getTypedRuleContext(PseudocodigoParser.Declaracion_varContext,0)


        def declaracion_funcion(self):
            return self.getTypedRuleContext(PseudocodigoParser.Declaracion_funcionContext,0)


        def llamada_funcion_stat(self):
            return self.getTypedRuleContext(PseudocodigoParser.Llamada_funcion_statContext,0)


        def si_stat(self):
            return self.getTypedRuleContext(PseudocodigoParser.Si_statContext,0)


        def retornar_stat(self):
            return self.getTypedRuleContext(PseudocodigoParser.Retornar_statContext,0)


        def getRuleIndex(self):
            return PseudocodigoParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = PseudocodigoParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruccion)
        try:
            self.state = 41
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.imprimir_stat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.leer_stat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 36
                self.declaracion_var()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 37
                self.declaracion_funcion()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 38
                self.llamada_funcion_stat()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 39
                self.si_stat()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 40
                self.retornar_stat()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Imprimir_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_IMPRIMIR(self):
            return self.getToken(PseudocodigoParser.KW_IMPRIMIR, 0)

        def DEL_PAREN_IZQ(self):
            return self.getToken(PseudocodigoParser.DEL_PAREN_IZQ, 0)

        def expresion(self):
            return self.getTypedRuleContext(PseudocodigoParser.ExpresionContext,0)


        def DEL_PAREN_DER(self):
            return self.getToken(PseudocodigoParser.DEL_PAREN_DER, 0)

        def getRuleIndex(self):
            return PseudocodigoParser.RULE_imprimir_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImprimir_stat" ):
                listener.enterImprimir_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImprimir_stat" ):
                listener.exitImprimir_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImprimir_stat" ):
                return visitor.visitImprimir_stat(self)
            else:
                return visitor.visitChildren(self)




    def imprimir_stat(self):

        localctx = PseudocodigoParser.Imprimir_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_imprimir_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(PseudocodigoParser.KW_IMPRIMIR)
            self.state = 44
            self.match(PseudocodigoParser.DEL_PAREN_IZQ)
            self.state = 45
            self.expresion(0)
            self.state = 46
            self.match(PseudocodigoParser.DEL_PAREN_DER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Leer_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_LEER(self):
            return self.getToken(PseudocodigoParser.KW_LEER, 0)

        def DEL_PAREN_IZQ(self):
            return self.getToken(PseudocodigoParser.DEL_PAREN_IZQ, 0)

        def ID(self):
            return self.getToken(PseudocodigoParser.ID, 0)

        def DEL_PAREN_DER(self):
            return self.getToken(PseudocodigoParser.DEL_PAREN_DER, 0)

        def getRuleIndex(self):
            return PseudocodigoParser.RULE_leer_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeer_stat" ):
                listener.enterLeer_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeer_stat" ):
                listener.exitLeer_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeer_stat" ):
                return visitor.visitLeer_stat(self)
            else:
                return visitor.visitChildren(self)




    def leer_stat(self):

        localctx = PseudocodigoParser.Leer_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_leer_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(PseudocodigoParser.KW_LEER)
            self.state = 49
            self.match(PseudocodigoParser.DEL_PAREN_IZQ)
            self.state = 50
            self.match(PseudocodigoParser.ID)
            self.state = 51
            self.match(PseudocodigoParser.DEL_PAREN_DER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracion_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PseudocodigoParser.ID, 0)

        def OP_ASIGNACION(self):
            return self.getToken(PseudocodigoParser.OP_ASIGNACION, 0)

        def expresion(self):
            return self.getTypedRuleContext(PseudocodigoParser.ExpresionContext,0)


        def getRuleIndex(self):
            return PseudocodigoParser.RULE_declaracion_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion_var" ):
                listener.enterDeclaracion_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion_var" ):
                listener.exitDeclaracion_var(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion_var" ):
                return visitor.visitDeclaracion_var(self)
            else:
                return visitor.visitChildren(self)




    def declaracion_var(self):

        localctx = PseudocodigoParser.Declaracion_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaracion_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(PseudocodigoParser.ID)
            self.state = 54
            self.match(PseudocodigoParser.OP_ASIGNACION)
            self.state = 55
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracion_funcionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FUNCION(self):
            return self.getToken(PseudocodigoParser.KW_FUNCION, 0)

        def ID(self):
            return self.getToken(PseudocodigoParser.ID, 0)

        def DEL_PAREN_IZQ(self):
            return self.getToken(PseudocodigoParser.DEL_PAREN_IZQ, 0)

        def DEL_PAREN_DER(self):
            return self.getToken(PseudocodigoParser.DEL_PAREN_DER, 0)

        def KW_FIN_FUNCION(self):
            return self.getToken(PseudocodigoParser.KW_FIN_FUNCION, 0)

        def parametros(self):
            return self.getTypedRuleContext(PseudocodigoParser.ParametrosContext,0)


        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudocodigoParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(PseudocodigoParser.InstruccionContext,i)


        def getRuleIndex(self):
            return PseudocodigoParser.RULE_declaracion_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion_funcion" ):
                listener.enterDeclaracion_funcion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion_funcion" ):
                listener.exitDeclaracion_funcion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion_funcion" ):
                return visitor.visitDeclaracion_funcion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion_funcion(self):

        localctx = PseudocodigoParser.Declaracion_funcionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declaracion_funcion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(PseudocodigoParser.KW_FUNCION)
            self.state = 58
            self.match(PseudocodigoParser.ID)
            self.state = 59
            self.match(PseudocodigoParser.DEL_PAREN_IZQ)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 60
                self.parametros()


            self.state = 63
            self.match(PseudocodigoParser.DEL_PAREN_DER)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8589935032) != 0):
                self.state = 64
                self.instruccion()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self.match(PseudocodigoParser.KW_FIN_FUNCION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PseudocodigoParser.ID)
            else:
                return self.getToken(PseudocodigoParser.ID, i)

        def DEL_COMA(self, i:int=None):
            if i is None:
                return self.getTokens(PseudocodigoParser.DEL_COMA)
            else:
                return self.getToken(PseudocodigoParser.DEL_COMA, i)

        def getRuleIndex(self):
            return PseudocodigoParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametros" ):
                return visitor.visitParametros(self)
            else:
                return visitor.visitChildren(self)




    def parametros(self):

        localctx = PseudocodigoParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(PseudocodigoParser.ID)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 73
                self.match(PseudocodigoParser.DEL_COMA)
                self.state = 74
                self.match(PseudocodigoParser.ID)
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Llamada_funcion_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PseudocodigoParser.ID, 0)

        def DEL_PAREN_IZQ(self):
            return self.getToken(PseudocodigoParser.DEL_PAREN_IZQ, 0)

        def DEL_PAREN_DER(self):
            return self.getToken(PseudocodigoParser.DEL_PAREN_DER, 0)

        def argumentos(self):
            return self.getTypedRuleContext(PseudocodigoParser.ArgumentosContext,0)


        def getRuleIndex(self):
            return PseudocodigoParser.RULE_llamada_funcion_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamada_funcion_stat" ):
                listener.enterLlamada_funcion_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamada_funcion_stat" ):
                listener.exitLlamada_funcion_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamada_funcion_stat" ):
                return visitor.visitLlamada_funcion_stat(self)
            else:
                return visitor.visitChildren(self)




    def llamada_funcion_stat(self):

        localctx = PseudocodigoParser.Llamada_funcion_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_llamada_funcion_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(PseudocodigoParser.ID)
            self.state = 81
            self.match(PseudocodigoParser.DEL_PAREN_IZQ)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8858427392) != 0):
                self.state = 82
                self.argumentos()


            self.state = 85
            self.match(PseudocodigoParser.DEL_PAREN_DER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudocodigoParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(PseudocodigoParser.ExpresionContext,i)


        def DEL_COMA(self, i:int=None):
            if i is None:
                return self.getTokens(PseudocodigoParser.DEL_COMA)
            else:
                return self.getToken(PseudocodigoParser.DEL_COMA, i)

        def getRuleIndex(self):
            return PseudocodigoParser.RULE_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos" ):
                listener.enterArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos" ):
                listener.exitArgumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentos" ):
                return visitor.visitArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def argumentos(self):

        localctx = PseudocodigoParser.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_argumentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.expresion(0)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 88
                self.match(PseudocodigoParser.DEL_COMA)
                self.state = 89
                self.expresion(0)
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Retornar_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_RETORNAR(self):
            return self.getToken(PseudocodigoParser.KW_RETORNAR, 0)

        def expresion(self):
            return self.getTypedRuleContext(PseudocodigoParser.ExpresionContext,0)


        def getRuleIndex(self):
            return PseudocodigoParser.RULE_retornar_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRetornar_stat" ):
                listener.enterRetornar_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRetornar_stat" ):
                listener.exitRetornar_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetornar_stat" ):
                return visitor.visitRetornar_stat(self)
            else:
                return visitor.visitChildren(self)




    def retornar_stat(self):

        localctx = PseudocodigoParser.Retornar_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_retornar_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(PseudocodigoParser.KW_RETORNAR)
            self.state = 96
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Si_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_SI(self):
            return self.getToken(PseudocodigoParser.KW_SI, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudocodigoParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(PseudocodigoParser.ExpresionContext,i)


        def KW_ENTONCES(self, i:int=None):
            if i is None:
                return self.getTokens(PseudocodigoParser.KW_ENTONCES)
            else:
                return self.getToken(PseudocodigoParser.KW_ENTONCES, i)

        def KW_FIN_SI(self):
            return self.getToken(PseudocodigoParser.KW_FIN_SI, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudocodigoParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(PseudocodigoParser.InstruccionContext,i)


        def KW_SINO_SI(self, i:int=None):
            if i is None:
                return self.getTokens(PseudocodigoParser.KW_SINO_SI)
            else:
                return self.getToken(PseudocodigoParser.KW_SINO_SI, i)

        def KW_SINO(self):
            return self.getToken(PseudocodigoParser.KW_SINO, 0)

        def getRuleIndex(self):
            return PseudocodigoParser.RULE_si_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSi_stat" ):
                listener.enterSi_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSi_stat" ):
                listener.exitSi_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSi_stat" ):
                return visitor.visitSi_stat(self)
            else:
                return visitor.visitChildren(self)




    def si_stat(self):

        localctx = PseudocodigoParser.Si_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_si_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(PseudocodigoParser.KW_SI)
            self.state = 99
            self.expresion(0)
            self.state = 100
            self.match(PseudocodigoParser.KW_ENTONCES)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8589935032) != 0):
                self.state = 101
                self.instruccion()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 107
                self.match(PseudocodigoParser.KW_SINO_SI)
                self.state = 108
                self.expresion(0)
                self.state = 109
                self.match(PseudocodigoParser.KW_ENTONCES)
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8589935032) != 0):
                    self.state = 110
                    self.instruccion()
                    self.state = 115
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 121
                self.match(PseudocodigoParser.KW_SINO)
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8589935032) != 0):
                    self.state = 122
                    self.instruccion()
                    self.state = 127
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 130
            self.match(PseudocodigoParser.KW_FIN_SI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PseudocodigoParser.RULE_expresion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExprLlamadaFuncContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PseudocodigoParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(PseudocodigoParser.ID, 0)
        def DEL_PAREN_IZQ(self):
            return self.getToken(PseudocodigoParser.DEL_PAREN_IZQ, 0)
        def DEL_PAREN_DER(self):
            return self.getToken(PseudocodigoParser.DEL_PAREN_DER, 0)
        def argumentos(self):
            return self.getTypedRuleContext(PseudocodigoParser.ArgumentosContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprLlamadaFunc" ):
                listener.enterExprLlamadaFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprLlamadaFunc" ):
                listener.exitExprLlamadaFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLlamadaFunc" ):
                return visitor.visitExprLlamadaFunc(self)
            else:
                return visitor.visitChildren(self)


    class ExprEnteroContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PseudocodigoParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LIT_ENTERO(self):
            return self.getToken(PseudocodigoParser.LIT_ENTERO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprEntero" ):
                listener.enterExprEntero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprEntero" ):
                listener.exitExprEntero(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprEntero" ):
                return visitor.visitExprEntero(self)
            else:
                return visitor.visitChildren(self)


    class ExprSumaRestaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PseudocodigoParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudocodigoParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(PseudocodigoParser.ExpresionContext,i)

        def OP_SUMA(self):
            return self.getToken(PseudocodigoParser.OP_SUMA, 0)
        def OP_RESTA(self):
            return self.getToken(PseudocodigoParser.OP_RESTA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprSumaResta" ):
                listener.enterExprSumaResta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprSumaResta" ):
                listener.exitExprSumaResta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprSumaResta" ):
                return visitor.visitExprSumaResta(self)
            else:
                return visitor.visitChildren(self)


    class ExprRelacionalContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PseudocodigoParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudocodigoParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(PseudocodigoParser.ExpresionContext,i)

        def OP_MAYOR_IG(self):
            return self.getToken(PseudocodigoParser.OP_MAYOR_IG, 0)
        def OP_MENOR_IG(self):
            return self.getToken(PseudocodigoParser.OP_MENOR_IG, 0)
        def OP_MAYOR(self):
            return self.getToken(PseudocodigoParser.OP_MAYOR, 0)
        def OP_MENOR(self):
            return self.getToken(PseudocodigoParser.OP_MENOR, 0)
        def OP_IGUAL(self):
            return self.getToken(PseudocodigoParser.OP_IGUAL, 0)
        def OP_DIFERENTE(self):
            return self.getToken(PseudocodigoParser.OP_DIFERENTE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprRelacional" ):
                listener.enterExprRelacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprRelacional" ):
                listener.exitExprRelacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprRelacional" ):
                return visitor.visitExprRelacional(self)
            else:
                return visitor.visitChildren(self)


    class ExprParenContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PseudocodigoParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DEL_PAREN_IZQ(self):
            return self.getToken(PseudocodigoParser.DEL_PAREN_IZQ, 0)
        def expresion(self):
            return self.getTypedRuleContext(PseudocodigoParser.ExpresionContext,0)

        def DEL_PAREN_DER(self):
            return self.getToken(PseudocodigoParser.DEL_PAREN_DER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprParen" ):
                listener.enterExprParen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprParen" ):
                listener.exitExprParen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprParen" ):
                return visitor.visitExprParen(self)
            else:
                return visitor.visitChildren(self)


    class ExprFlotanteContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PseudocodigoParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LIT_FLOTANTE(self):
            return self.getToken(PseudocodigoParser.LIT_FLOTANTE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprFlotante" ):
                listener.enterExprFlotante(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprFlotante" ):
                listener.exitExprFlotante(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprFlotante" ):
                return visitor.visitExprFlotante(self)
            else:
                return visitor.visitChildren(self)


    class ExprCadenaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PseudocodigoParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LIT_CADENA(self):
            return self.getToken(PseudocodigoParser.LIT_CADENA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprCadena" ):
                listener.enterExprCadena(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprCadena" ):
                listener.exitExprCadena(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprCadena" ):
                return visitor.visitExprCadena(self)
            else:
                return visitor.visitChildren(self)


    class ExprArregloContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PseudocodigoParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(PseudocodigoParser.ID, 0)
        def DEL_CORCH_IZQ(self):
            return self.getToken(PseudocodigoParser.DEL_CORCH_IZQ, 0)
        def expresion(self):
            return self.getTypedRuleContext(PseudocodigoParser.ExpresionContext,0)

        def DEL_CORCH_DER(self):
            return self.getToken(PseudocodigoParser.DEL_CORCH_DER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprArreglo" ):
                listener.enterExprArreglo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprArreglo" ):
                listener.exitExprArreglo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprArreglo" ):
                return visitor.visitExprArreglo(self)
            else:
                return visitor.visitChildren(self)


    class ExprIdContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PseudocodigoParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(PseudocodigoParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprId" ):
                listener.enterExprId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprId" ):
                listener.exitExprId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprId" ):
                return visitor.visitExprId(self)
            else:
                return visitor.visitChildren(self)


    class ExprMultDivModContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PseudocodigoParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PseudocodigoParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(PseudocodigoParser.ExpresionContext,i)

        def OP_MULT(self):
            return self.getToken(PseudocodigoParser.OP_MULT, 0)
        def OP_DIV(self):
            return self.getToken(PseudocodigoParser.OP_DIV, 0)
        def OP_MODULO(self):
            return self.getToken(PseudocodigoParser.OP_MODULO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprMultDivMod" ):
                listener.enterExprMultDivMod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprMultDivMod" ):
                listener.exitExprMultDivMod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprMultDivMod" ):
                return visitor.visitExprMultDivMod(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PseudocodigoParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = PseudocodigoParser.ExprParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 133
                self.match(PseudocodigoParser.DEL_PAREN_IZQ)
                self.state = 134
                self.expresion(0)
                self.state = 135
                self.match(PseudocodigoParser.DEL_PAREN_DER)
                pass

            elif la_ == 2:
                localctx = PseudocodigoParser.ExprLlamadaFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 137
                self.match(PseudocodigoParser.ID)
                self.state = 138
                self.match(PseudocodigoParser.DEL_PAREN_IZQ)
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8858427392) != 0):
                    self.state = 139
                    self.argumentos()


                self.state = 142
                self.match(PseudocodigoParser.DEL_PAREN_DER)
                pass

            elif la_ == 3:
                localctx = PseudocodigoParser.ExprArregloContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 143
                self.match(PseudocodigoParser.ID)
                self.state = 144
                self.match(PseudocodigoParser.DEL_CORCH_IZQ)
                self.state = 145
                self.expresion(0)
                self.state = 146
                self.match(PseudocodigoParser.DEL_CORCH_DER)
                pass

            elif la_ == 4:
                localctx = PseudocodigoParser.ExprIdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 148
                self.match(PseudocodigoParser.ID)
                pass

            elif la_ == 5:
                localctx = PseudocodigoParser.ExprEnteroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 149
                self.match(PseudocodigoParser.LIT_ENTERO)
                pass

            elif la_ == 6:
                localctx = PseudocodigoParser.ExprFlotanteContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 150
                self.match(PseudocodigoParser.LIT_FLOTANTE)
                pass

            elif la_ == 7:
                localctx = PseudocodigoParser.ExprCadenaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 151
                self.match(PseudocodigoParser.LIT_CADENA)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 165
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 163
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = PseudocodigoParser.ExprMultDivModContext(self, PseudocodigoParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 154
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 155
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 234881024) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 156
                        self.expresion(11)
                        pass

                    elif la_ == 2:
                        localctx = PseudocodigoParser.ExprSumaRestaContext(self, PseudocodigoParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 157
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 158
                        _la = self._input.LA(1)
                        if not(_la==23 or _la==24):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 159
                        self.expresion(10)
                        pass

                    elif la_ == 3:
                        localctx = PseudocodigoParser.ExprRelacionalContext(self, PseudocodigoParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 160
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 161
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7274496) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 162
                        self.expresion(9)
                        pass

             
                self.state = 167
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         




