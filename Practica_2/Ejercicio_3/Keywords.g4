grammar Keywords;

stat: keyword+ ;

keyword: IF | WHILE | PRINT ;

IF: 'if' ;
WHILE: 'while' ;
PRINT: 'print' ;

WS: [ \t\r\n]+ -> skip ;