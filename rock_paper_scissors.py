import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
selection_computer = random.randint(0,2)
user_selection = int(input("Piedra, Papel, o Tijera! Selecciona 0 para Piedra, 1 para Papel, 2 para Tijera\n"))
print("Has escogido:")
if user_selection == 0:
  print(rock)
elif user_selection == 1:
  print(paper)
elif user_selection == 2:
  print(scissors)

  

print("Yo he escogido!")  
print(selection_computer)
if selection_computer == 0:
  print(rock)
elif selection_computer == 1:
  print(paper)
elif selection_computer == 2:
  print(scissors)

if selection_computer == 0:
  if user_selection == 0:
    print("Empate! :o")
  if user_selection == 1:
    print("Me ganaste!")
  if user_selection == 2:
    print("Gane!")
    
elif selection_computer == 1:
  if user_selection == 0:
    print("Gane")
  if user_selection == 1:
    print("Empate")
  if user_selection ==2:
    print("Me Ganaste")

elif selection_computer == 2:
  if user_selection == 0:
    print("Me ganaste")
  if user_selection == 1:
    print("Gane")
  if user_selection ==2:
    print:("Empate")





