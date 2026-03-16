grammar Expr4;

expr: term (('+'|'-') term)* ;

term: factor (('*'|'/') factor)* ;

factor
    : NUM
    | '(' expr ')'
    ;

NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;
