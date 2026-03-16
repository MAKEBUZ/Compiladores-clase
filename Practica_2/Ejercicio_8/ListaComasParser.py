# Generated from ListaComas.g4 by ANTLR 4.13.1
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
        4,1,3,11,2,0,7,0,1,0,1,0,1,0,5,0,6,8,0,10,0,12,0,9,9,0,1,0,0,0,1,
        0,0,0,10,0,2,1,0,0,0,2,7,5,2,0,0,3,4,5,1,0,0,4,6,5,2,0,0,5,3,1,0,
        0,0,6,9,1,0,0,0,7,5,1,0,0,0,7,8,1,0,0,0,8,1,1,0,0,0,9,7,1,0,0,0,
        1,7
    ]

class ListaComasParser ( Parser ):

    grammarFileName = "ListaComas.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "NUMERO", "WS" ]

    RULE_lista = 0

    ruleNames =  [ "lista" ]

    EOF = Token.EOF
    T__0=1
    NUMERO=2
    WS=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ListaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self, i:int=None):
            if i is None:
                return self.getTokens(ListaComasParser.NUMERO)
            else:
                return self.getToken(ListaComasParser.NUMERO, i)

        def getRuleIndex(self):
            return ListaComasParser.RULE_lista

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista" ):
                listener.enterLista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista" ):
                listener.exitLista(self)




    def lista(self):

        localctx = ListaComasParser.ListaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_lista)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(ListaComasParser.NUMERO)
            self.state = 7
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 3
                self.match(ListaComasParser.T__0)
                self.state = 4
                self.match(ListaComasParser.NUMERO)
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





