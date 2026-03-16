# Generated from Saludo.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SaludoParser import SaludoParser
else:
    from SaludoParser import SaludoParser

# This class defines a complete listener for a parse tree produced by SaludoParser.
class SaludoListener(ParseTreeListener):

    # Enter a parse tree produced by SaludoParser#saludo.
    def enterSaludo(self, ctx:SaludoParser.SaludoContext):
        pass

    # Exit a parse tree produced by SaludoParser#saludo.
    def exitSaludo(self, ctx:SaludoParser.SaludoContext):
        pass


    # Enter a parse tree produced by SaludoParser#saludos.
    def enterSaludos(self, ctx:SaludoParser.SaludosContext):
        pass

    # Exit a parse tree produced by SaludoParser#saludos.
    def exitSaludos(self, ctx:SaludoParser.SaludosContext):
        pass



del SaludoParser