grammar Mini;

prog: stat+ ;

stat
    : ID '=' expr
    | 'print' expr
    ;

expr
    : term ('+' term)*   // ← sin ambigüedad
    ;

term
    : NUM
    | ID
    ;

ID : [a-zA-Z]+ ;
NUM: [0-9]+ ;
WS : [ \t\r\n]+ -> skip ;