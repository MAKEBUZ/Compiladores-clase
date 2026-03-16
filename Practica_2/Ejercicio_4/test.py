from antlr4 import *
from OperadoresLexer import OperadoresLexer
from OperadoresParser import OperadoresParser

# Entrada de prueba
input_stream = InputStream("+")

# Crear lexer
lexer = OperadoresLexer(input_stream)

# Crear stream de tokens
token_stream = CommonTokenStream(lexer)
token_stream.fill()

print("TOKENS:")

for token in token_stream.tokens:
    if token.type != Token.EOF:

        token_name = lexer.symbolicNames[token.type]

        if token_name is None:
            token_name = lexer.literalNames[token.type]

        print(f"Texto: {token.text}  Tipo: {token_name}")

# Crear parser
parser = OperadoresParser(token_stream)

# Regla inicial
tree = parser.op()

print("\nÁRBOL SINTÁCTICO:")
print(tree.toStringTree(recog=parser))
