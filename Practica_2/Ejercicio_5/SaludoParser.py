# Generated from Saludo.g4 by ANTLR 4.13.1
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

class SaludoParser ( Parser ):

    grammarFileName = "Saludo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'hola'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "NOMBRE", "WS" ]

    RULE_saludo = 0
    RULE_saludos = 1

    ruleNames =  [ "saludo", "saludos" ]

    EOF = Token.EOF
    T__0=1
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

        def saludos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SaludoParser.SaludosContext)
            else:
                return self.getTypedRuleContext(SaludoParser.SaludosContext,i)


        def getRuleIndex(self):
            return SaludoParser.RULE_saludo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSaludo" ):
                listener.enterSaludo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSaludo" ):
                listener.exitSaludo(self)




    def saludo(self):

        localctx = SaludoParser.SaludoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_saludo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 5 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 4
                self.saludos()
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


    class SaludosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOMBRE(self):
            return self.getToken(SaludoParser.NOMBRE, 0)

        def getRuleIndex(self):
            return SaludoParser.RULE_saludos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSaludos" ):
                listener.enterSaludos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSaludos" ):
                listener.exitSaludos(self)




    def saludos(self):

        localctx = SaludoParser.SaludosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_saludos)
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





