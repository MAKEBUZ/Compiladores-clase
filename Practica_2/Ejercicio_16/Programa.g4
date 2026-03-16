grammar Programa;

prog: stat+ ;

stat: ID '=' NUM ;

ID: [a-zA-Z]+ ;
NUM: [0-9]+ ;

WS: [ \t\r\n]+ -> skip ;
