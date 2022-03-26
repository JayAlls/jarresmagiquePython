import random

print("Bienvenue dans le jeu des jarres !")
difficult = int(input("Niveau 1: 4 clés, 1 serpent \n"
                      "Niveau 2: 3 clés, 2 serpents \n"
                      "Niveau 3: 2 clés, 3 serpents \n"
                      "Entre 1, 2 ou 3: "))
keys = 0



while keys != 3:

    snake = ['S'] * difficult

    key = ['K'] * (5 - difficult)

    jars = snake + key

    random.shuffle(jars)

    choice = int(input("Entrez un nombre entre 1 et 5: "))

    if jars[choice - 1] == 'K':
        print("Bravo, tu as trouvé une clé")
        keys += 1
        print(f"Tu as {keys} / 3 clés")
    else:
        print("Aie ! Tu es tombé sur un serpent !")








