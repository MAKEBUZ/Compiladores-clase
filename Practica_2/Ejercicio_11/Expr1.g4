grammar Expr1;

expr: expr1+;

expr1: EXPR | NUM ;

EXPR: '+';
NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;
