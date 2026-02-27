# Generated from Calculadora.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CalculadoraParser import CalculadoraParser
else:
    from CalculadoraParser import CalculadoraParser

# This class defines a complete listener for a parse tree produced by CalculadoraParser.
class CalculadoraListener(ParseTreeListener):

    # Enter a parse tree produced by CalculadoraParser#prog.
    def enterProg(self, ctx:CalculadoraParser.ProgContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#prog.
    def exitProg(self, ctx:CalculadoraParser.ProgContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Numero.
    def enterNumero(self, ctx:CalculadoraParser.NumeroContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Numero.
    def exitNumero(self, ctx:CalculadoraParser.NumeroContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#AddSub.
    def enterAddSub(self, ctx:CalculadoraParser.AddSubContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#AddSub.
    def exitAddSub(self, ctx:CalculadoraParser.AddSubContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Parentesis.
    def enterParentesis(self, ctx:CalculadoraParser.ParentesisContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Parentesis.
    def exitParentesis(self, ctx:CalculadoraParser.ParentesisContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#MultDiv.
    def enterMultDiv(self, ctx:CalculadoraParser.MultDivContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#MultDiv.
    def exitMultDiv(self, ctx:CalculadoraParser.MultDivContext):
        pass



del CalculadoraParser