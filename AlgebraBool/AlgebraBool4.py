import sympy as sp

# Definir las variables booleanas
A, B, C, D, E = sp.symbols('A B C D E')

def preprocess_expression(expr_str):
    """
    Preprocesa la expresión booleana para que sea compatible con sympy.
    """
    # Reemplazar operadores booleanos con los correspondientes en sympy
    expr_str = expr_str.replace('*', '&').replace('+', '|')
    
    # Reemplazar 'NOT' por '~' para la compatibilidad con sympy
    expr_str = expr_str.replace('NOT ', '~')

    # Retornar la expresión preprocesada
    return expr_str

def parse_boolean_expression(expr_str):
    """
    Convierte una cadena de texto en una expresión booleana utilizando sympy.
    """
    # Preprocesar la expresión
    expr_str = preprocess_expression(expr_str)
    
    # Evaluar la expresión usando sympy
    try:
        expr = sp.sympify(expr_str, evaluate=False)
        return expr
    except Exception as e:
        raise ValueError(f"Error al analizar la expresión: {e}")

def main():
    # Pedir al usuario que introduzca la expresión booleana
    expr_str = input("Introduce la expresión booleana (usa '*' para AND, '+' para OR, y 'NOT' para NOT): ").strip()
    
    try:
        # Convertir la cadena de texto en una expresión booleana
        expr = parse_boolean_expression(expr_str)

        # Simplificar la expresión booleana
        simplified_expr = sp.simplify_logic(expr)

        # Mostrar la expresión simplificada
        print(f"Expresión original: {expr}")
        print(f"Expresión simplificada: {simplified_expr}")
    except Exception as e:
        print(f"Error al procesar la expresión: {e}")

if __name__ == "__main__":
    main()
