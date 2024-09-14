import sympy as sp

# Definir las variables booleanas
A, B, C = sp.symbols('A B C')

# Definir las reglas y leyes del álgebra booleana
def apply_boolean_rules(expr):
    # Leyes de identidad
    expr = sp.simplify_logic(expr)
    expr = expr.subs(A * 1, A).subs(A + 0, A)  # A * 1 = A, A + 0 = A
    expr = expr.subs(A * 0, 0).subs(A + 1, 1)  # A * 0 = 0, A + 1 = 1

    # Ley de idempotencia
    expr = expr.subs(A * A, A).subs(A + A, A)  # A * A = A, A + A = A

    # Ley de complementación
    expr = expr.subs(A * sp.Not(A), 0).subs(A + sp.Not(A), 1)  # A * ¬A = 0, A + ¬A = 1

    # Ley de involución
    expr = expr.subs(sp.Not(sp.Not(A)), A)  # ¬(¬A) = A

    # Ley de conmutación
    expr = expr.subs(A * B, B * A).subs(A + B, B + A)  # A * B = B * A, A + B = B + A

    # Ley de asociatividad
    expr = sp.simplify_logic(expr)

    # Ley de distributividad
    expr = expr.subs(A * (B + C), (A * B) + (A * C))  # A * (B + C) = (A * B) + (A * C)
    expr = expr.subs(A + (B * C), (A + B) * (A + C))  # A + (B * C) = (A + B) * (A + C)

    # Ley de absorción
    expr = expr.subs(A + (A * B), A).subs(A * (A + B), A)  # A + (A * B) = A, A * (A + B) = A

    # Ley de De Morgan
    expr = expr.subs(sp.Not(A * B), sp.Not(A) + sp.Not(B)).subs(sp.Not(A + B), sp.Not(A) * sp.Not(B))  # ¬(A * B) = ¬A + ¬B, ¬(A + B) = ¬A * ¬B

    return sp.simplify_logic(expr)

# Definir las expresiones booleanas usando suma (OR) y multiplicación (AND)
expr1 = A * (B + C)  # Ejemplo de expresión 1: A * (B + C)
expr2 = (A * B) + (A * C)  # Ejemplo de expresión 2: (A * B) + (A * C)

# Aplicar las reglas booleanas a ambas expresiones
simplified_expr1 = apply_boolean_rules(expr1)
simplified_expr2 = apply_boolean_rules(expr2)

# Verificar si las dos expresiones son equivalentes
if simplified_expr1 == simplified_expr2:
    print("Las expresiones son equivalentes.")
else:
    print("Las expresiones no son equivalentes.")

# Opcional: Imprimir las expresiones simplificadas
print(f"Expresión 1 simplificada: {simplified_expr1}")
print(f"Expresión 2 simplificada: {simplified_expr2}")
