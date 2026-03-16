# Generated from Operadores.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,5,5,2,0,7,0,1,0,1,0,1,0,0,0,1,0,0,1,1,0,1,4,3,0,2,1,0,0,0,2,
        3,7,0,0,0,3,1,1,0,0,0,0
    ]

class OperadoresParser ( Parser ):

    grammarFileName = "Operadores.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "MAS", "MENOS", "MUL", "DIV", "WS" ]

    RULE_op = 0

    ruleNames =  [ "op" ]

    EOF = Token.EOF
    MAS=1
    MENOS=2
    MUL=3
    DIV=4
    WS=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class OpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAS(self):
            return self.getToken(OperadoresParser.MAS, 0)

        def MENOS(self):
            return self.getToken(OperadoresParser.MENOS, 0)

        def MUL(self):
            return self.getToken(OperadoresParser.MUL, 0)

        def DIV(self):
            return self.getToken(OperadoresParser.DIV, 0)

        def getRuleIndex(self):
            return OperadoresParser.RULE_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp" ):
                listener.enterOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp" ):
                listener.exitOp(self)




    def op(self):

        localctx = OperadoresParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





