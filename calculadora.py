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