grammar Operadores;

op: MAS | MENOS | MUL | DIV ;

MAS: '+' ;
MENOS: '-' ;
MUL: '*' ;
DIV: '/' ;

WS: [ \t\r\n]+ -> skip ;
