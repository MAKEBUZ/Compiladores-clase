from antlr4 import *
from CalcLexer import CalcLexer
from CalcParser import CalcParser

# Entrada de prueba
input_stream = InputStream("x = 5\ny = 10\nprint x + y\nprint (x + y) * 2")

# Crear lexer
lexer = CalcLexer(input_stream)

# Crear stream de tokens
token_stream = CommonTokenStream(lexer)
token_stream.fill()

print("TOKENS:")

for token in token_stream.tokens:
    if token.type != Token.EOF:

        token_name = lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) else None  # ← guard

        if not token_name:
            token_name = lexer.literalNames[token.type] if token.type < len(lexer.literalNames) else str(token.type)  # ← guard

        print(f"Texto: {token.text}  Tipo: {token_name}")

# Crear parser
parser = CalcParser(token_stream)

# Regla inicial
tree = parser.prog()

print("\nÁRBOL SINTÁCTICO:")
print(tree.toStringTree(recog=parser))