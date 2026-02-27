grammar Calculadora;

prog: expresion EOF ;
// Regla principal
expresion : expresion ('*'|'/') expresion   # MultDiv
          | expresion ('+'|'-') expresion   # AddSub  
          | '(' expresion ')'               # Parentesis
          | NUMBER                          # Numero
          ;

// Tokens
NUMBER : [0-9]+ ('.' [0-9]+)? ;
WS : [ \t\r\n]+ -> skip ;