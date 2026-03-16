from antlr4 import *
from Expr3Lexer import Expr3Lexer
from Expr3Parser import Expr3Parser

input_stream = InputStream("3+4*5")

lexer = Expr3Lexer(input_stream)
token_stream = CommonTokenStream(lexer)
token_stream.fill()

print("TOKENS:")

for token in token_stream.tokens:
    if token.type != Token.EOF:

        sym  = lexer.symbolicNames[token.type]  if token.type < len(lexer.symbolicNames)  else None
        lit  = lexer.literalNames[token.type]   if token.type < len(lexer.literalNames)   else None

        token_name = (sym if sym and sym != '<INVALID>' else None) or \
                     (lit if lit and lit != '<INVALID>' else None) or \
                     str(token.type)

        print(f"Texto: {token.text!r:<6}  Tipo: {token_name}")

parser = Expr3Parser(token_stream)
tree = parser.expr()

print("\nÁRBOL SINTÁCTICO:")
print(tree.toStringTree(recog=parser))

