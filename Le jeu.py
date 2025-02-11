import random
# from Mots import mots

mots = ["banane"]
def choisir_le_mot():
    return random.choice(mots)

def deviner_le_mots(x):
    tentative = str(input("Je pense que le mot est : ").lower())
    if tentative == x:
        print(f"Bravo! le mot caché était bien {x}!")
    else:
        print(f"Désolé, le mot caché n'est pas {tentative}.")
        game()


def Test_avec_lettre(x):
    lettre = str(input("Quelle lettre veux-tu essayer ? ").lower())
    réponse = ["_"] *len(x)
    for c in range(len(list(x))):
        if x[c] == lettre:
            réponse[c] = lettre

    réponse_str = "".join(réponse) 
    
    if réponse_str == x:
        print(f"Bravo! Tu as trouvé la lettre manquante! Le mot était {x}")
    else:
        print("Tu as ça {réponse}")
    
def game():
    mot = choisir_le_mot()
    while True:
        Décision = str(input("Veux-tu essayer deviner le mot (m) ou tester une lettre (l) ? ").lower())
        if Décision == "m":
            deviner_le_mots(mot)
        elif Décision == "l":
            Test_avec_lettre(mot)
        else:
            print(f"Veuillez choisir la lettre m pour deviner un mot ou l pour tenter une lettre")     


game()
    
