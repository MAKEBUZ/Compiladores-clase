# Generated from Saludo2.g4 by ANTLR 4.13.1
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
        4,1,3,12,2,0,7,0,2,1,7,1,1,0,4,0,6,8,0,11,0,12,0,7,1,1,1,1,1,1,0,
        0,2,0,2,0,1,1,0,1,2,10,0,5,1,0,0,0,2,9,1,0,0,0,4,6,3,2,1,0,5,4,1,
        0,0,0,6,7,1,0,0,0,7,5,1,0,0,0,7,8,1,0,0,0,8,1,1,0,0,0,9,10,7,0,0,
        0,10,3,1,0,0,0,1,7
    ]

class Saludo2Parser ( Parser ):

    grammarFileName = "Saludo2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "SALUDOTIPO", "NOMBRE", "WS" ]

    RULE_saludo = 0
    RULE_saludo2 = 1

    ruleNames =  [ "saludo", "saludo2" ]

    EOF = Token.EOF
    SALUDOTIPO=1
    NOMBRE=2
    WS=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SaludoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def saludo2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Saludo2Parser.Saludo2Context)
            else:
                return self.getTypedRuleContext(Saludo2Parser.Saludo2Context,i)


        def getRuleIndex(self):
            return Saludo2Parser.RULE_saludo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSaludo" ):
                listener.enterSaludo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSaludo" ):
                listener.exitSaludo(self)




    def saludo(self):

        localctx = Saludo2Parser.SaludoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_saludo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 5 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 4
                self.saludo2()
                self.state = 7 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==2):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Saludo2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SALUDOTIPO(self):
            return self.getToken(Saludo2Parser.SALUDOTIPO, 0)

        def NOMBRE(self):
            return self.getToken(Saludo2Parser.NOMBRE, 0)

        def getRuleIndex(self):
            return Saludo2Parser.RULE_saludo2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSaludo2" ):
                listener.enterSaludo2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSaludo2" ):
                listener.exitSaludo2(self)




    def saludo2(self):

        localctx = Saludo2Parser.Saludo2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_saludo2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
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





