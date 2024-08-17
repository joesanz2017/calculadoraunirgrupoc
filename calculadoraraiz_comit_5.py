# Esta función suma dos números
def sumar(x, y):
    return x + y

# Esta función resta dos números
def restar(x, y):
    return x - y

# Esta función multiplica dos números
def multiplicar(x, y):
    return x * y

# Esta función divide dos números
def dividir(x, y):
    if y == 0:
        return "Error: No se puede dividir por cero."
    return x / y

# Esta función calcula la raíz cuadrada
def raiz_cuadrada(x):
    if x < 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo."
    return x ** 0.5

print("UNIR GRUPO C")
print("Selecciona una operación.")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Raíz Cuadrada")


while True:
    # Tomar la elección del usuario
    eleccion = input("Ingresa la opción (1/2/3/4/5): ")

    if eleccion in ('1','2','3','4','5'):
        try:
            if eleccion in ('1','2','3','4'):
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))

            if eleccion == '5':
                num1 = float(input("Ingresa el número: "))
            
            
        
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número válido.")
            continue

        if eleccion == '1':
            print(f"{num1} + {num2} = {sumar(num1, num2)}")

        elif eleccion == '2':
            print(f"{num1} - {num2} = {restar(num1, num2)}")

        elif eleccion == '3':
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")

        elif eleccion == '4':
            print(f"{num1} / {num2} = {dividir(num1, num2)}")

        elif eleccion == '5':
            print(f"Raíz cuadrada de {num1} = {raiz_cuadrada(num1)}")

        
    
        # Preguntar si el usuario quiere hacer otro cálculo
        siguiente_calculo = input("¿Deseas hacer otro cálculo? (sí/no): ")
        if siguiente_calculo.lower() != "sí":
            break
    else:
        print("Entrada no válida")
