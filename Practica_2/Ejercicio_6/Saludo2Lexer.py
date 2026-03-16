# Generated from Saludo2.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,3,35,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,22,8,0,1,1,4,1,25,8,1,11,1,12,
        1,26,1,2,4,2,30,8,2,11,2,12,2,31,1,2,1,2,0,0,3,1,1,3,2,5,3,1,0,2,
        2,0,65,90,97,122,3,0,9,10,13,13,32,32,37,0,1,1,0,0,0,0,3,1,0,0,0,
        0,5,1,0,0,0,1,21,1,0,0,0,3,24,1,0,0,0,5,29,1,0,0,0,7,8,5,104,0,0,
        8,9,5,111,0,0,9,10,5,108,0,0,10,22,5,97,0,0,11,12,5,98,0,0,12,13,
        5,117,0,0,13,14,5,101,0,0,14,15,5,110,0,0,15,16,5,111,0,0,16,17,
        5,115,0,0,17,18,5,100,0,0,18,19,5,105,0,0,19,20,5,97,0,0,20,22,5,
        115,0,0,21,7,1,0,0,0,21,11,1,0,0,0,22,2,1,0,0,0,23,25,7,0,0,0,24,
        23,1,0,0,0,25,26,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,4,1,0,0,
        0,28,30,7,1,0,0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,
        1,0,0,0,32,33,1,0,0,0,33,34,6,2,0,0,34,6,1,0,0,0,4,0,21,26,31,1,
        6,0,0
    ]

class Saludo2Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SALUDOTIPO = 1
    NOMBRE = 2
    WS = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "SALUDOTIPO", "NOMBRE", "WS" ]

    ruleNames = [ "SALUDOTIPO", "NOMBRE", "WS" ]

    grammarFileName = "Saludo2.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


