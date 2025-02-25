
"""
    Videojuego Narrativo de Dragones (para aplicar los conocimientos de POO, pero comenezaremos con Programacion estructurada)
        principales mecanicas (por el momento)
            - Crear tu personaje. (ingresado por el jugador o seleccionado)
                - Nombre
                - Clases ->  Guerrero, Lanza conjuros, Bardo, Picaro, Paladin, Druida (Algo dificil por las especies)
                - Habilidades (seleccionar las habilidades) -> pendiente
                - Seleccionar especie ->    Dragon
                                            Grifo
                                            Hipogrifo
                                            Unicornio
                                            Dragon Marino
                                            Serpirnte Marina
                                            Basilisco
                                            Cocatriz
                                            Quimera
                                            Pegaso
                                            Fenix
                                            Naga
                - Historia (opcional)

            - Enemigos ->   Trolls, Gigantes, Gigantes de hielo, Espectros, Plantas Carnivoras, 
                            Insectos Giagntes, Aves Roc, Leviathan (No se si se escribe asi xD),
                            Hombres Pez, Slimes, Arpia, Golem....
"""

import random as rd

Status = 0
CharName = str
CharClass = str


def Start(Status):
    if (Status == 0):
        CrChar()
    else:
        print("Nombre: ", playerChar1.CharName)
        print("Tipo: ", playerChar1.CharElement)
        print("Clase: ", playerChar1.CharClass)
        print("Habilidad de elemento: ", playerChar1.CharElmAbility)
        print("Vida: ", playerChar1.CharLive, "% ")
        CmpMain()


def CmpMain():
    activeEnemy = rd.choice([enemy1, enemy2, enemy3])
    print("Estas en la plaza central del reino, te encuentras a un(a) ",
          activeEnemy.kind, "...Te ataca...")
    print("que haces? \t1-Luchar \t2-Escapar  \t3-Salir")
    option = int(input())
    if option != 0 and option < 4:
        if option == 1:
            print("Aqui pelearas epicamente contra el/la ", activeEnemy.kind,
                  "pero por ahora usaras tu imaginacion, no es genial?, Yay")
            Btl(activeEnemy)
        if option == 2:
            print("Esta bien tener miedo...(sususra:...Cobarde!!!)")
        if option == 3:
            Exit()
    else:
        print("opcion no valida, felicidades malograste el juego, estas contento?... (¬_¬)")


def GameSvd():
    print("aqui se salvara el juego")


def Btl(activeEnemy):
    # Ataca enemigo, obtenemos nivel de ataque (lo que te bajara de vida) y efectividad (si te da o no)
    lvlAtack = rd.randrange(100)
    # Efectividad, 0 - fallo, 1 - rozo, 2 - golpe suerficial, 3 - golpe no muy efectivo, 4 - golpe directo, 5 - critico
    efective = rd.randrange(5)
    print("Ataque nivel: ", lvlAtack, ", con una efectividad de ", efective)
    if efective == 0:
        print("Fallo")
        separador()
        playerTurn(playerChar1, activeEnemy)
    if efective == 1:
        flvlAtack = lvlAtack-((lvlAtack/100)*80)
        print("Roso, el daño es de", flvlAtack)
        playerChar1.CharLive = playerChar1.CharLive - flvlAtack
        print("tu vida es de ", playerChar1.CharLive, "%")
        separador()
        if playerChar1.CharLive <= 0:
            defeated()
        else:
            playerTurn(playerChar1, activeEnemy)
    if efective == 2:
        flvlAtack = lvlAtack-((lvlAtack/100)*60)
        print("golpe suerficial, el daño es de", flvlAtack)
        playerChar1.CharLive = playerChar1.CharLive - flvlAtack
        print("tu vida es de ", playerChar1.CharLive, "%")
        separador()
        if playerChar1.CharLive <= 0:
            defeated()
        else:
            playerTurn(playerChar1, activeEnemy)
    if efective == 3:
        flvlAtack = lvlAtack-((lvlAtack/100)*40)
        print("golpe no muy efectivo, el daño es de", flvlAtack)
        playerChar1.CharLive = playerChar1.CharLive - flvlAtack
        print("tu vida es de ", playerChar1.CharLive, "%")
        separador()
        if playerChar1.CharLive <= 0:
            defeated()
        else:
            playerTurn(playerChar1, activeEnemy)
    if efective == 4:
        flvlAtack = lvlAtack-((lvlAtack/100)*20)
        print("golpe directo, el daño es de", flvlAtack)
        playerChar1.CharLive = playerChar1.CharLive - flvlAtack
        print("tu vida es de ", playerChar1.CharLive, "%")
        separador()
        if playerChar1.CharLive <= 0:
            defeated()
        else:
            playerTurn(playerChar1, activeEnemy)
    if efective == 5:
        flvlAtack = lvlAtack
        print("critico, el daño es de", flvlAtack)
        playerChar1.CharLive = playerChar1.CharLive - flvlAtack
        print("tu vida es de ", playerChar1.CharLive, "%")
        separador()
        if playerChar1.CharLive <= 0:
            defeated()
        else:
            playerTurn(playerChar1, activeEnemy)

def playerTurn(playerLive,activeEnemy):
    if playerLive.CharLive >= 0 :
        action = int(input("Tu turno: \n\t1- Atacar \n\t2- Huir \n\t3- Usar Item \n\t"))
        print(action)
        if action == 1 :
            atack = int(input("\n\t1- Magia \n\t2- Fisico \n\t"))
            if atack == 1 :
                spell = int(input("\n\t1- Destello cegador \n\t2- Paralizante \n\t"))
                if spell == 1 :
                    spell2= PlayerChar.CharElmAbility
                    lvlAtack = rd.randrange(100)+(spell2/2)
                    print("Tu Nivel de ataque es de : ", lvlAtack)
                    efective = rd.randrange(5)
                    if efective <= 0:
                        print("Fallo")
                        separador()
                        Btl(activeEnemy)
                    if efective == 1:
                        flvlAtack = lvlAtack - ((lvlAtack / 100) * 80)
                        print("Roso, el daño es de", flvlAtack)
                        Enemy.live = Enemy.live - flvlAtack
                        print("La vida del enemigo es de ", Enemy.live, "%")
                        separador()
                        if Enemy.live <= 0:
                            victory()
                        else:
                            Btl(activeEnemy)
                    if efective == 2:
                        flvlAtack = lvlAtack - ((lvlAtack / 100) * 60)
                        print("golpe suerficial, el daño es de", flvlAtack)
                        Enemy.live = Enemy.live - flvlAtack
                        print("La vida del enemigo es de ", Enemy.live, "%")
                        separador()
                        if Enemy.live <= 0:
                            victory()
                        else:
                            Btl(activeEnemy)
                    if efective == 3:
                        flvlAtack = lvlAtack - ((lvlAtack / 100) * 40)
                        print("golpe no muy efectivo, el daño es de", flvlAtack)
                        Enemy.live = Enemy.live - flvlAtack
                        print("La vida del enemigo es de ", Enemy.live, "%")
                        separador()
                        if Enemy.live <= 0:
                            victory()
                        else:
                            Btl(activeEnemy)
                    if efective == 4:
                        flvlAtack = lvlAtack - ((lvlAtack / 100) * 20)
                        print("golpe directo, el daño es de", flvlAtack)
                        Enemy.live = Enemy.live - flvlAtack
                        print("La vida del enemigo es de ", Enemy.live, "%")
                        separador()
                        if Enemy.live <= 0:
                            victory()
                        else:
                            Btl(activeEnemy)
                    if efective == 5:
                        flvlAtack = lvlAtack
                        print("critico, el daño es de", flvlAtack)
                        Enemy.live = Enemy.live - flvlAtack
                        print("La vida del enemigo es de ", Enemy.live, "%")
                        separador()
                        if Enemy.live <= 0:
                            victory()
                        else:
                            Btl(activeEnemy)
                elif spell == 2:
                    print("aun en desarrollo!!!!")
                    exit()
            elif atack == 2:
                print("Aun en desarrollo!!!")
                exit()
        elif action == 2 :
            print("aun en desarrollo!!!")
            exit()
        elif action == 3 :
            print("aun en desarrollo!!!")
            exit()
    else:
        print("Game over...")

def victory():
    print("Has ganado que no es Genial!!!!!")
    input("La historia continuara...Gracias por jugar!!!")

def defeated():
    status = 0
    playerChar1.CharLive = 100
    select = input("Deseas jugar denuevo?:  Y/N")
    if select == "Y" or select == "y":
        Start(status)
    elif select == "N" or select == "n":
        Exit()
    else:
        print("Selecion invalida!!!")

def charClassFunc(value):
    if value == 1:
        return "Guerrero"
    elif value == 2:
        return "Lanzaconjuros"
    elif value == 3:
        return "Bardo"
    elif value == 4:
        return  "Picaro"
    elif value == 5:
        return "Paladin"
    elif value == 6:
        return "Druida"

def separador():
    print("\n--------------------------------------------------------\n")

class Enemy:
    kind = rd.choice(["Troll", "Gigante", "Gigante de hielo", "Espectro", "Planta Carnivora",
                     "Insecto Giagnte", "Ave Roc", "Leviathan", "Hombre Pez", "Slime", "Arpia", "Golem"])
    level = rd.randrange(10)
    live = 100
    elemnAb = rd.choice([25, 50, 75, 100])


class PlayerChar:
    CharName = CharName
    CharLive = 100
    CharClass = CharClass
    CharElement = rd.choice(["Fire", "Water", "Earth", "Wind"])
    CharElmAbility = rd.choice([25, 50, 75, 100])


def CrChar():

    CharName = input("\nCual sera el nombre de tu personaje: \n\t-> ")

    # vamos a verificar si es un numero lo que el usuario ingreso:
    its_number = True
    # aqui recorremos cada caracter (char) dentro de la cadena (str)
    for char in CharName:
        # si no es (if not) una letra minuscula o mayuscula
        if not (('a' <= char <= 'z') or ('A' <= char <= 'Z')):
            its_number = False
            break
    if not its_number:
        print("Ingrese un nombre que este formado solo por letras: \t")
        CrChar()  # volvemos a llamar a nuestra funcion para reintentar
    else:
        charClass = int(input("Cual sera tu clase: \n\t1- Guerrero\n\t2- Lanzaconjuros\n\t3- Bardo\n\t4- Picaro\n\t5- Paladin\n\t6- Druida\n\t(Despues habra mas clases)"))
        CharClass = charClassFunc(charClass)
        print("Bienvenido ", CharName)
        playerChar1.CharName = CharName
        playerChar1.CharClass = CharClass
        status = 1
        Start(status)


def Exit():
    GameSvd()
    input("Hasta Luego...Gracias por jugar!!!")


playerChar1 = PlayerChar()  #Instanciamos un jugador
enemy1 = Enemy()            #Instanciamos 3 enemigos, de los cuales enfrentaremos uno a uno conforme avance la historia
enemy2 = Enemy()
enemy3 = Enemy()

Start(Status)
