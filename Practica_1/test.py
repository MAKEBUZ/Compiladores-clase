from antlr4 import *
from CalculadoraLexer import CalculadoraLexer
from CalculadoraParser import CalculadoraParser

input_stream = InputStream("3+4*2")

lexer = CalculadoraLexer(input_stream)
token_stream = CommonTokenStream(lexer)
token_stream.fill()

print("TOKENS:")

for token in token_stream.tokens:
    if token.type != Token.EOF:
        token_name = CalculadoraParser.symbolicNames[token.type]
        print(f"Texto: {token.text:>3}  Tipo: {token_name}")

parser = CalculadoraParser(token_stream)
tree = parser.prog()

print("\nÁRBOL:")
print(tree.toStringTree(recog=parser))