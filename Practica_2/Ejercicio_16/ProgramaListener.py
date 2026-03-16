# Generated from Programa.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ProgramaParser import ProgramaParser
else:
    from ProgramaParser import ProgramaParser

# This class defines a complete listener for a parse tree produced by ProgramaParser.
class ProgramaListener(ParseTreeListener):

    # Enter a parse tree produced by ProgramaParser#prog.
    def enterProg(self, ctx:ProgramaParser.ProgContext):
        pass

    # Exit a parse tree produced by ProgramaParser#prog.
    def exitProg(self, ctx:ProgramaParser.ProgContext):
        pass


    # Enter a parse tree produced by ProgramaParser#stat.
    def enterStat(self, ctx:ProgramaParser.StatContext):
        pass

    # Exit a parse tree produced by ProgramaParser#stat.
    def exitStat(self, ctx:ProgramaParser.StatContext):
        pass



del ProgramaParser