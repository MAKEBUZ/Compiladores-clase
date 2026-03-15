# Generated from Numeros.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .NumerosParser import NumerosParser
else:
    from NumerosParser import NumerosParser

# This class defines a complete listener for a parse tree produced by NumerosParser.
class NumerosListener(ParseTreeListener):

    # Enter a parse tree produced by NumerosParser#numero.
    def enterNumero(self, ctx:NumerosParser.NumeroContext):
        pass

    # Exit a parse tree produced by NumerosParser#numero.
    def exitNumero(self, ctx:NumerosParser.NumeroContext):
        pass



del NumerosParser