import random
# from Mots import mots

mots = ["banane"]
def choisir_le_mot():
    random.choice(mots)

def deviner_le_mots(x):
    tentative = str(input("Je pense que le mot est : ").lower())
    if tentative == x:
        print(f"Bravo! le mot caché était bien {x}!")
    else:
        print(f"Désolé, le mot caché n'est pas {tentative}.")
    
def game():
    mot = choisir_le_mot()

game()
    
