# from logo import calc_logo
# print (calc_logo)
#Calculator Functions
# Sum
from turtle import Turtle


def add(num1, num2):
  return num1 + num2
# Substraction
def substract(num1, num2):
  return num1 - num2
# Multiplication
def multiply(num1, num2):
  return num1 * num2
# Division
def divide(num1, num2):
  return num1 / num2

symbols = {
  "+":add,
  "-":substract,
  "*":multiply,
  "/":divide
}

#print(type(symbols))
#print(symbols)
def calculator():
  num1 = float(input("Cual es el primer numero? "))
  for key in symbols:
    #print(symbols[key])
    print(key)
  continue_using = True
  while continue_using:
    operation_symbol = input("Seleccione un operador: ")
    num2 = float(input("Cual es el siguiente numero? "))
    #para que este funcione debo tener las otras como string en el dictionary, los value
    # if operation_symbol == "+":
    #   result = add(num1, num2)
    # elif operation_symbol == "-":
    #   result = substract(num1, num2)
    # elif operation_symbol == "*":
    #   result = multiply(num1, num2)
    # elif operation_symbol == "/":
    #   result = divide(num1, num2)
    calculation_function = symbols[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer} es el resultado final Perrito")

    if input(f"Escribe 'si' si deseas continuar con {answer} o escriba 'no' para continuar con un nuevo numero. ") == "si":
      num1 = answer
    else:
      continue_using = False
      calculator()

calculator()