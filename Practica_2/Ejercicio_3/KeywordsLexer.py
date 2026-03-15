# Generated from Keywords.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,4,31,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,4,3,26,8,3,11,3,12,
        3,27,1,3,1,3,0,0,4,1,1,3,2,5,3,7,4,1,0,1,3,0,9,10,13,13,32,32,31,
        0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,1,9,1,0,0,0,3,12,
        1,0,0,0,5,18,1,0,0,0,7,25,1,0,0,0,9,10,5,105,0,0,10,11,5,102,0,0,
        11,2,1,0,0,0,12,13,5,119,0,0,13,14,5,104,0,0,14,15,5,105,0,0,15,
        16,5,108,0,0,16,17,5,101,0,0,17,4,1,0,0,0,18,19,5,112,0,0,19,20,
        5,114,0,0,20,21,5,105,0,0,21,22,5,110,0,0,22,23,5,116,0,0,23,6,1,
        0,0,0,24,26,7,0,0,0,25,24,1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,0,27,
        28,1,0,0,0,28,29,1,0,0,0,29,30,6,3,0,0,30,8,1,0,0,0,2,0,27,1,6,0,
        0
    ]

class KeywordsLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    WHILE = 2
    PRINT = 3
    WS = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'while'", "'print'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "WHILE", "PRINT", "WS" ]

    ruleNames = [ "IF", "WHILE", "PRINT", "WS" ]

    grammarFileName = "Keywords.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


