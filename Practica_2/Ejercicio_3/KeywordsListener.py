# Generated from Keywords.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .KeywordsParser import KeywordsParser
else:
    from KeywordsParser import KeywordsParser

# This class defines a complete listener for a parse tree produced by KeywordsParser.
class KeywordsListener(ParseTreeListener):

    # Enter a parse tree produced by KeywordsParser#stat.
    def enterStat(self, ctx:KeywordsParser.StatContext):
        pass

    # Exit a parse tree produced by KeywordsParser#stat.
    def exitStat(self, ctx:KeywordsParser.StatContext):
        pass


    # Enter a parse tree produced by KeywordsParser#keyword.
    def enterKeyword(self, ctx:KeywordsParser.KeywordContext):
        pass

    # Exit a parse tree produced by KeywordsParser#keyword.
    def exitKeyword(self, ctx:KeywordsParser.KeywordContext):
        pass



del KeywordsParser