print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bienvenida a la cuadra pantano.")
print("Tu mision es encontrar el telescopio que Jack Sparrow dejo en el Holandes Errante antes de que este se mudara a Barrios Unidos.")
print("")
input1 = input("Abres la puerta de la casa y dos hombres vestidos de pulpo corren hacia la derecha o la izquierda, ambos tienen algo que parece un telescopio. Escribe izquierda o derecha dependiendo del Pulpo que decidas seguir.\n")

if input1 == ("izquierda"):
    input2 = input('Encontraste que este pulpo nada el rio que esta por el alcantarillado, escribe "nadar" si deseas atravesar el rio, o "esperar" si deseas continuar mirandolo\n')
    if input2 == ("esperar"):
        input3 = input('Mientras esperas, los ladrillos se rompen y derepente un gorro de capitan esta en tu cabeza, el Holandes Errante empieza salir de los ladrillos, puedes ver como las velas del inmenso barco se elevan y ahora te enceuntras frente a 3 puertas, estan muy mohoseadas pero puedes ver los colores "verde, rojo y azul". Que puerta escoges?\n')
        if input3 == ("amarillo"):
            print("Aparece chico guapo pero con muchos residuos marinos, parece que huele a babosa, te dice soy hijo del capitan Barbosa ten tu telescopio, decides casarte con el y desparacitarlo. Has ganado!")
        else:
            print("Muchas babosas salen y te no te comen pero te conviertes en babosa, has perdido!")
    else:
        print("Te mojas tu ropa y tu saco de lana toma un mal olor, no sabes que hacer, pero continuas nadando en un momento el escucha como tu estilo mariposa hace ruido y se voltea, de repente hace una senal con las manos y miras tras ti y el otro pulpo esta ahi, ambos te llevan a las profundidades del rio, has perdido!")

else:
    print("Mientras lo sigues el se voltea y con sus tentaculos te pega en una pared, Game Over!")

    

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

