from antlr4 import *
from Expr4Lexer import Expr4Lexer
from Expr4Parser import Expr4Parser

# Entrada de prueba
input_stream = InputStream("(3+4)*5")

# Crear lexer
lexer = Expr4Lexer(input_stream)

# Crear stream de tokens
token_stream = CommonTokenStream(lexer)
token_stream.fill()

print("TOKENS:")

for token in token_stream.tokens:
    if token.type != Token.EOF:

        token_name = lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) else None  # ← guard

        if not token_name:                                                                                 # ← cubre None y ''
            token_name = lexer.literalNames[token.type] if token.type < len(lexer.literalNames) else str(token.type)  # ← guard

        print(f"Texto: {token.text}  Tipo: {token_name}")

# Crear parser
parser = Expr4Parser(token_stream)

# Regla inicial
tree = parser.expr()

print("\nÁRBOL SINTÁCTICO:")
print(tree.toStringTree(recog=parser))