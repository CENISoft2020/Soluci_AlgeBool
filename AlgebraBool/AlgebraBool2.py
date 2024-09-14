import sympy as sp
import re

# Definir las variables booleanas
A, B, C, D, E = sp.symbols('A B C D E')

def preprocess_expression(expr_str):
    """
    Preprocesa la cadena de texto para asegurarse de que sea adecuada para sympy.
    """
    # Reemplaza operadores y añade espacios entre variables
    expr_str = expr_str.replace('*', '&').replace('+', '|').replace('~', 'Not ')
    
    # Reemplaza combinaciones de variables como AB por A & B
    expr_str = re.sub(r'([A-E])([A-E])', r'\1 & \2', expr_str)
    
    # Añadir espacios después de paréntesis para asegurar el formato correcto
    expr_str = re.sub(r'(\))(\S)', r'\1 \2', expr_str)
    expr_str = re.sub(r'(\S)(\()', r'\1 \2', expr_str)
    
    return expr_str

def parse_expression(expr_str):
    """
    Convierte una cadena de texto preprocesada a una expresión booleana usando sympy.
    """
    return sp.sympify(expr_str, evaluate=False)

# Pedir al usuario que introduzca la expresión booleana
expr_str = input("Introduce la expresión booleana (usa '*' para AND, '+' para OR, y '~' para NOT): ")

# Preprocesar la cadena de texto para mejorar la compatibilidad con sympy
preprocessed_expr_str = preprocess_expression(expr_str)

# Convertir la cadena de texto preprocesada en una expresión booleana
expr = parse_expression(preprocessed_expr_str)

# Simplificar la expresión booleana
simplified_expr = sp.simplify_logic(expr)

# Mostrar la expresión simplificada
print(f"Expresión original: {expr}")
print(f"Expresión simplificada: {simplified_expr}")
