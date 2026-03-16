grammar ListaNumeros;

lista: NUMERO+ ;

NUMERO: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;
