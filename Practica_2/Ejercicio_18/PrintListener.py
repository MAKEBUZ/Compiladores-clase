# Generated from Print.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PrintParser import PrintParser
else:
    from PrintParser import PrintParser

# This class defines a complete listener for a parse tree produced by PrintParser.
class PrintListener(ParseTreeListener):

    # Enter a parse tree produced by PrintParser#stat.
    def enterStat(self, ctx:PrintParser.StatContext):
        pass

    # Exit a parse tree produced by PrintParser#stat.
    def exitStat(self, ctx:PrintParser.StatContext):
        pass


    # Enter a parse tree produced by PrintParser#expr.
    def enterExpr(self, ctx:PrintParser.ExprContext):
        pass

    # Exit a parse tree produced by PrintParser#expr.
    def exitExpr(self, ctx:PrintParser.ExprContext):
        pass



del PrintParser