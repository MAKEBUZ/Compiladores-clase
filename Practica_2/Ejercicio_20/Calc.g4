grammar Calc;

prog: stat+ ;

stat
    : ID '=' expr
    | 'print' expr
    ;

expr: term (('+'|'-') term)* ;

term: factor (('*'|'/') factor)* ;

factor
    : NUM
    | ID
    | '(' expr ')'
    ;

ID: [a-zA-Z]+ ;
NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;
