grammar Pseudocodigo;

// ==========================================
// REGLAS SINTÁCTICAS (PARSER) - Minúsculas
// ==========================================

programa : KW_INICIO instruccion* KW_FIN EOF ;

instruccion : imprimir_stat
            | leer_stat
            | declaracion_var
            | declaracion_funcion
            | llamada_funcion_stat
            | si_stat
            | retornar_stat ;

imprimir_stat : KW_IMPRIMIR DEL_PAREN_IZQ expresion DEL_PAREN_DER ;
leer_stat     : KW_LEER DEL_PAREN_IZQ ID DEL_PAREN_DER ;

declaracion_var : ID OP_ASIGNACION expresion ;

declaracion_funcion  : KW_FUNCION ID DEL_PAREN_IZQ parametros? DEL_PAREN_DER instruccion* KW_FIN_FUNCION ;
parametros           : ID (DEL_COMA ID)* ;
llamada_funcion_stat : ID DEL_PAREN_IZQ argumentos? DEL_PAREN_DER ;
argumentos           : expresion (DEL_COMA expresion)* ;
retornar_stat        : KW_RETORNAR expresion ;

si_stat : KW_SI expresion KW_ENTONCES instruccion*
          (KW_SINO_SI expresion KW_ENTONCES instruccion*)*
          (KW_SINO instruccion*)?
          KW_FIN_SI ;

// Jerarquía de operaciones matemáticas y lógicas (usando TUS tokens)
expresion : expresion (OP_MULT | OP_DIV | OP_MODULO) expresion                     # ExprMultDivMod
          | expresion (OP_SUMA | OP_RESTA) expresion                               # ExprSumaResta
          | expresion (OP_MAYOR_IG | OP_MENOR_IG | OP_MAYOR | OP_MENOR | OP_IGUAL | OP_DIFERENTE) expresion # ExprRelacional
          | DEL_PAREN_IZQ expresion DEL_PAREN_DER                                  # ExprParen
          | ID DEL_PAREN_IZQ argumentos? DEL_PAREN_DER                             # ExprLlamadaFunc
          | ID DEL_CORCH_IZQ expresion DEL_CORCH_DER                               # ExprArreglo // Agregado para usar tus corchetes
          | ID                                                                     # ExprId
          | LIT_ENTERO                                                             # ExprEntero
          | LIT_FLOTANTE                                                           # ExprFlotante
          | LIT_CADENA                                                             # ExprCadena
          ;

// ==========================================
// REGLAS LÉXICAS (LEXER/TOKENS) - Mayúsculas
// ==========================================

// 1. PALABRAS RESERVADAS (Deben ir antes del ID)
KW_INICIO      : 'inicio' ;
KW_FIN         : 'fin' ;
KW_IMPRIMIR    : 'imprimir' ;
KW_LEER        : 'leer' ;
KW_FUNCION     : 'funcion' ;
KW_FIN_FUNCION : 'fin_funcion' ;
KW_RETORNAR    : 'retornar' ;
KW_SI          : 'si' ;
KW_ENTONCES    : 'entonces' ;
KW_SINO_SI     : 'sino_si' ;
KW_SINO        : 'sino' ;
KW_FIN_SI      : 'fin_si' ;

// 2. LA LISTA EXACTA DE TUS TOKENS
LIT_CADENA     : '"' ~["]* '"' ;
LIT_FLOTANTE   : [0-9]+ '.' [0-9]+ ;
LIT_ENTERO     : [0-9]+ ;

OP_IGUAL       : '==' ;
OP_DIFERENTE   : '!=' ;
OP_MAYOR_IG    : '>=' ;
OP_MENOR_IG    : '<=' ;
OP_ASIGNACION  : '=' ;
OP_MAYOR       : '>' ;
OP_MENOR       : '<' ;

OP_SUMA        : '+' ;
OP_RESTA       : '-' ;
OP_MULT        : '*' ;
OP_DIV         : '/' ;
OP_MODULO      : '%' ;

DEL_PAREN_IZQ  : '(' ;
DEL_PAREN_DER  : ')' ;
DEL_CORCH_IZQ  : '[' ;
DEL_CORCH_DER  : ']' ;
DEL_COMA       : ',' ;

ID             : [a-zA-Z_][a-zA-Z0-9_]* ;

// 3. IGNORAR ESPACIOS
WS             : [ \t\r\n]+ -> skip ;