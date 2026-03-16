grammar ExprVar;

expr: expr '+' expr
    | ID
    | NUM
    ;

ID: [a-zA-Z]+ ;
NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;
