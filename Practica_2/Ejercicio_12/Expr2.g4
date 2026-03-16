grammar Expr2;

expr: expr2+;

expr2: EXPR2 | NUM ;

EXPR2: '+' | '*';
NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;
