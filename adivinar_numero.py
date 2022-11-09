import random
def dificulty():
    game_mode = input("Escoge el nivel de dificultad. Escribe 'facil' o 'dificil': ")
    if game_mode == "facil":
        mode = 10
        return mode
    elif game_mode == "dificil":
        mode = 5
        return mode

def checking(answer):
    if random_number > answer :
        print("No, es mayor!")
    elif random_number < answer :
        print("No, es menor!")
    else:
        print("GANASTE, la respuesta es {answer}")

def prueba(mode):
    attempts = mode
    for attempt in range(1,attempts + 1):
        print(f"Tienes {attempts } intentos para adivinar el numero")
        user_input = int(input("Intenta adivinar: "))
        attempts -= 1
        checking(user_input)

def game(mode):
    attempts_left = True
    attempts = mode
    while attempts_left:
        for attempt in range(1,attempts + 1):
            print(f"Tienes {attempts } intentos para adivinar el numero")
            user_input = int(input("Intenta adivinar: "))
            if random_number == user_input:
                print(f"Lo encontraste, el numero es {random_number}!")
                attempts_left = False
                break
            elif random_number > user_input :
                print("No, es mayor!")
            elif random_number <user_input :
                print("No, es menor!")
            attempts -= 1
        if attempts < 1:
            attempts_left = False
            print(f"Se acabaron los intentos, perdiste... el numero estaba muy facil. Era {random_number}.")
        

random_number = random.randint(1, 100)
print("Bienvenido a Adivina el Numero!")
print("Advina el numero que estoy pensando entre 1 y 100")
print(f"Jajajaja el numero es {random_number}")
user_selection = dificulty()
game(user_selection)