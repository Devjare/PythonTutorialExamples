def solicitar_entrada():
    entrada = int(input("""
    Que operacion quieres realizar?
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division\n
    """))

    return entrada


def obtener_operandos() -> (float, float):
    op1 = float(input("Ingresa primer valor: "))
    op2 = float(input("Ingresa segundo valor: "))

    return float(op1), float(op2)


if __name__ == "__main__":

    operacion = solicitar_entrada()

    while True:
        op1, op2 = obtener_operandos()

        if operacion == 1:
            print(f"{op1} + {op2} = {op1 + op2}")
        elif operacion == 2:
            print(f"{op1} - {op2} = {op1 - op2}")
        elif operacion == 3:
            print(f"{op1} * {op2} = {op1 * op2}")
        elif operacion == 4:
            print(f"{op1} / {op2} = {op1 / op2}")
        else:
            print("Operacion invalida!")
            break

        operacion = solicitar_entrada()

