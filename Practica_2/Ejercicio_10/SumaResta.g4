grammar SumaResta;

expr: NUM OP NUM ;

OP: '+' | '-' ;
NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;
