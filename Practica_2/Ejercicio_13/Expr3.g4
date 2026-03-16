grammar Expr3;

expr   : term   (('+'|'-') term)*   ;
term   : factor (('*'|'/') factor)* ;
factor : '-' factor
       | '(' expr ')'
       | NUM
       ;

NUM : [0-9]+ ('.' [0-9]+)? ;
WS  : [ \t\r\n]+ -> skip ;