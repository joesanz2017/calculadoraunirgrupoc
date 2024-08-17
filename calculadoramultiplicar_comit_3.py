# Esta función suma dos números
def sumar(x, y):
    return x + y

# Esta función resta dos números
def restar(x, y):
    return x - y

# Esta función multiplica dos números
def multiplicar(x, y):
    return x * y

print("UNIR GRUPO C")
print("Selecciona una operación.")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")


while True:
    # Tomar la elección del usuario
    eleccion = input("Ingresa la opción (1/2/3): ")

    if eleccion in ('1','2','3'):
        try:
            if eleccion in ('1','2','3'):
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            
            
        
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número válido.")
            continue

        if eleccion == '1':
            print(f"{num1} + {num2} = {sumar(num1, num2)}")

        elif eleccion == '2':
            print(f"{num1} - {num2} = {restar(num1, num2)}")

        elif eleccion == '3':
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")

        
    
        # Preguntar si el usuario quiere hacer otro cálculo
        siguiente_calculo = input("¿Deseas hacer otro cálculo? (sí/no): ")
        if siguiente_calculo.lower() != "sí":
            break
    else:
        print("Entrada no válida")
