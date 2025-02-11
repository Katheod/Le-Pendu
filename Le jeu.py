import random
from Mots import mots

def mot_valide(mots):
    mot = random.choice(mots)
    while "-" in mot or " " in mot:
        mot = random.choice(mots)

    return mot.upper()

def Le_pendu():
    mot = mot_valide(mots)
    lettres_mot = set(mot)
    lettres_essayées = set()
    joueur_essai = input("Essais une lettre : ").upper()
    if joueur_essai.isalpha() and joueur_essai not in lettres_essayées:
        lettres_essayées.add(joueur_essai)
        if joueur_essai in lettres_mot:
            lettres_essayées.remove(joueur_essai)
    
    elif joueur_essai in lettres_essayées:
        print("Tu as déjà essayé cette lettre. Essaie une autre.")

    else:
        print("Caractère invalide")