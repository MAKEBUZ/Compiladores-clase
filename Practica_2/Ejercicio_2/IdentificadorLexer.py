# Generated from Identificador.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,2,19,6,-1,2,0,7,0,2,1,7,1,1,0,1,0,5,0,8,8,0,10,0,12,0,11,9,0,
        1,1,4,1,14,8,1,11,1,12,1,15,1,1,1,1,0,0,2,1,1,3,2,1,0,3,2,0,65,90,
        97,122,3,0,48,57,65,90,97,122,3,0,9,10,13,13,32,32,20,0,1,1,0,0,
        0,0,3,1,0,0,0,1,5,1,0,0,0,3,13,1,0,0,0,5,9,7,0,0,0,6,8,7,1,0,0,7,
        6,1,0,0,0,8,11,1,0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,2,1,0,0,0,11,
        9,1,0,0,0,12,14,7,2,0,0,13,12,1,0,0,0,14,15,1,0,0,0,15,13,1,0,0,
        0,15,16,1,0,0,0,16,17,1,0,0,0,17,18,6,1,0,0,18,4,1,0,0,0,3,0,9,15,
        1,6,0,0
    ]

class IdentificadorLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    WS = 2

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "ID", "WS" ]

    ruleNames = [ "ID", "WS" ]

    grammarFileName = "Identificador.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


