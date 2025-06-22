def sumar(a: float, b: float) -> float:
    """Suma dos números."""
    return a + b

def restar(a: float, b: float) -> float:
    """Resta el segundo número del primero."""
    return a - b

def multiplicar(a: float, b: float) -> float:
    """Multiplica dos números."""
    return a * b

def dividir(a: float, b: float) -> float:
    """Divide el primer número entre el segundo."""
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

if __name__ == "__main__":
    print(sumar(2, 3))        # 5
    print(restar(5, 1))       # 4
    print(multiplicar(4, 2))  # 8
    print(dividir(10, 2))     # 5.0

def potencia(a: float, b: float) -> float:
    """Calcula a elevado a b."""
    return a ** b

def elevar_al_cubo(a: float) -> float:
    """Eleva un número al cubo."""
    return a ** 3
