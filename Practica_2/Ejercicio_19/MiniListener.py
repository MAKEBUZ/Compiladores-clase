# Generated from Mini.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniParser import MiniParser
else:
    from MiniParser import MiniParser

# This class defines a complete listener for a parse tree produced by MiniParser.
class MiniListener(ParseTreeListener):

    # Enter a parse tree produced by MiniParser#prog.
    def enterProg(self, ctx:MiniParser.ProgContext):
        pass

    # Exit a parse tree produced by MiniParser#prog.
    def exitProg(self, ctx:MiniParser.ProgContext):
        pass


    # Enter a parse tree produced by MiniParser#stat.
    def enterStat(self, ctx:MiniParser.StatContext):
        pass

    # Exit a parse tree produced by MiniParser#stat.
    def exitStat(self, ctx:MiniParser.StatContext):
        pass


    # Enter a parse tree produced by MiniParser#expr.
    def enterExpr(self, ctx:MiniParser.ExprContext):
        pass

    # Exit a parse tree produced by MiniParser#expr.
    def exitExpr(self, ctx:MiniParser.ExprContext):
        pass



del MiniParser