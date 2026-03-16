grammar Saludo;

saludo: saludos+ ;
saludos: 'hola' | NOMBRE ;

NOMBRE: [A-Z][a-z]+ ;
WS: [ \t\r\n]+ -> skip ;
