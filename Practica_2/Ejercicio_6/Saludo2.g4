grammar Saludo2;

saludo: saludo2+ ;

saludo2: SALUDOTIPO | NOMBRE ;

SALUDOTIPO: 'hola' | 'buenosdias';
NOMBRE: [a-zA-Z]+ ;
WS: [ \t\r\n]+ -> skip ;
