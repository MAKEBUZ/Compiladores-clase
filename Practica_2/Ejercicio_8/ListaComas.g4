grammar ListaComas;

lista: NUMERO (',' NUMERO)* ;

NUMERO: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;
