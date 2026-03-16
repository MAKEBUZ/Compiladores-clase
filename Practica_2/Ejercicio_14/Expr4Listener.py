# Generated from Expr4.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Expr4Parser import Expr4Parser
else:
    from Expr4Parser import Expr4Parser

# This class defines a complete listener for a parse tree produced by Expr4Parser.
class Expr4Listener(ParseTreeListener):

    # Enter a parse tree produced by Expr4Parser#expr.
    def enterExpr(self, ctx:Expr4Parser.ExprContext):
        pass

    # Exit a parse tree produced by Expr4Parser#expr.
    def exitExpr(self, ctx:Expr4Parser.ExprContext):
        pass


    # Enter a parse tree produced by Expr4Parser#term.
    def enterTerm(self, ctx:Expr4Parser.TermContext):
        pass

    # Exit a parse tree produced by Expr4Parser#term.
    def exitTerm(self, ctx:Expr4Parser.TermContext):
        pass


    # Enter a parse tree produced by Expr4Parser#factor.
    def enterFactor(self, ctx:Expr4Parser.FactorContext):
        pass

    # Exit a parse tree produced by Expr4Parser#factor.
    def exitFactor(self, ctx:Expr4Parser.FactorContext):
        pass



del Expr4Parser