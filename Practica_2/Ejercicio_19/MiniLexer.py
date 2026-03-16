# Generated from Mini.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,6,40,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,4,3,25,8,3,11,3,12,3,26,
        1,4,4,4,30,8,4,11,4,12,4,31,1,5,4,5,35,8,5,11,5,12,5,36,1,5,1,5,
        0,0,6,1,1,3,2,5,3,7,4,9,5,11,6,1,0,3,2,0,65,90,97,122,1,0,48,57,
        3,0,9,10,13,13,32,32,42,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,
        1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,1,13,1,0,0,0,3,15,1,0,0,0,5,21,
        1,0,0,0,7,24,1,0,0,0,9,29,1,0,0,0,11,34,1,0,0,0,13,14,5,61,0,0,14,
        2,1,0,0,0,15,16,5,112,0,0,16,17,5,114,0,0,17,18,5,105,0,0,18,19,
        5,110,0,0,19,20,5,116,0,0,20,4,1,0,0,0,21,22,5,43,0,0,22,6,1,0,0,
        0,23,25,7,0,0,0,24,23,1,0,0,0,25,26,1,0,0,0,26,24,1,0,0,0,26,27,
        1,0,0,0,27,8,1,0,0,0,28,30,7,1,0,0,29,28,1,0,0,0,30,31,1,0,0,0,31,
        29,1,0,0,0,31,32,1,0,0,0,32,10,1,0,0,0,33,35,7,2,0,0,34,33,1,0,0,
        0,35,36,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,38,1,0,0,0,38,39,
        6,5,0,0,39,12,1,0,0,0,4,0,26,31,36,1,6,0,0
    ]

class MiniLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    ID = 4
    NUM = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'print'", "'+'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "NUM", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "ID", "NUM", "WS" ]

    grammarFileName = "Mini.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


