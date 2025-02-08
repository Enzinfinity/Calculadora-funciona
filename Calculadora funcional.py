
print("Bem vindo a calculadora")

num1 = input ("Coloque o primeiro numero que deseja:")
num2 = input ("Coloque o segundo numero que deseja:")
operation = input("Choose an operation (+, -, *, /): ")




if operation == "+":
    print(f"The result is: {num1 + num2}")
elif operation == "-":
    print(f"The result is: {num1 - num2}")
elif operation == "*":
    print(f"The result is: {num1 * num2}")
elif operation == "/":
    if num2 != 0:
        print(f"The result is: {num1 / num2}")
    else:
        print("Error: Division by zero!")
else:
    print("Invalid operation!")




Continuar = input("Deseja continuar ? (Yes/No)").strip().lower()

if Continuar !="yes":
    



