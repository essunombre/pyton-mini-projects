from errno import EACCES
import random
EASY_MODE = 10
HARD_MODE = 5

def checking(user_input, random_number, turns):
    """Checks answer against guess, Return number of turns remaining"""
    if user_input > random_number :
        print("No, es mayor!")
        return turns - 1
    elif user_input < random_number :
        print("No, es menor!")
        return turns - 1
    else:
        print(f"GANASTE, la respuesta es {random_number}")

def dificulty():
    game_mode = input("Escoge el nivel de dificultad. Escribe 'facil' o 'dificil': ")
    if game_mode == "facil":
        return EASY_MODE
    elif game_mode == "dificil":
        return HARD_MODE
    
def game():
    print("Bienvenido a Adivina el Numero!")
    print("Advina el numero que estoy pensando entre 1 y 100")
    random_number = random.randint(1, 100)
    print(f"Jajajaja el numero es {random_number}")
    turns = dificulty()
    user_input = 0
    while user_input != random_number: 
        print(f"Tienes {turns} intentos para adivinar el numero")
        user_input = int(input("Intenta adivinar: "))
        turns = checking(user_input, random_number, turns)

        if turns == 0:
            print(f"Se acabaron los intentos, perdiste... el numero estaba muy facil. Era {random_number}.")
            return
        elif user_input != random_number:
            print("Intenta nuevamente!")
    
game()