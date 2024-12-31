# *********************************
# Projet NSI : JEU
# Date: 17/01/2023
# Nom: Kabiri
# Prénom: Mohamed Ali
# *********************************


# -------------------------------------------------------------
# -------- FONCTIONS ET PROCEDURES ----------------------------
# -------------------------------------------------------------


from random import *
from time import *

seed()



# Variables GLOBALE (pourront être utilisées à l'intérieur de toutes nos fonctions)

jetons_joueur=['X','O']
grille = []
partie_terminee = False
num_joueur_courant = 1


#***********************************************************************************


def creation_grille_vierge():
    
    ''' Cette fonction va remplir la grille du jeu par des "."
    IN: Rien
    OUT: Rien car on va remplir la variable globale grille, déjà déclarée
    ,→au tout début du programme 

    On fabrique une liste de liste de string (de 1 caractère) modélisant␣
    ,→notre grille de jeu de 6 lignes par 7 colonnes
    [ [".", ".", ".", "." , "." , "." , "."],
    [".", ".", ".", "." , "." , "." , "."],
    ...
    [".", ".", ".", "." , "." , "." , "."] ]

'''

# On déclare que l'on va utiliser la variable globale grille (déjà initialisée)
    global grille
    
    # Pour chaque ligne
    for num_ligne in range(6):
        ligne = []   # on crée un nouveau tableau vide en mémoire                  
        for j in range(7): # On ajoute les sept éléments ".", séparémment.            
            ligne.append(".") 
            
        # On ajoute la nouvelle ligne à la grille
        grille.append(ligne)
    return

# ------ TEST TEMPORAIRE --------
#creation_grille_vierge()
#print(grille)





def affiche_grille() -> None:
    
    ''' Cette fonction affiche la grille de jeu telle que ci-dessous
    IN: Rien
    OUT: Rien
    Affichage souhaitée :
       0 1 2 3 4 5 6
    0 |.|.|.|.|.|.|.|
    1 |.|.|.|.|.|.|.|
    2 |.|.|.|.|.|.|.|
    3 |.|.|.|.|.|.|.|
    4 |.|.|.|X|.|.|.|
    5 |O|X|.|X|O|X|O|
    ---------------
'''
    
    global grille
    
    # Affichage des indices du haut de la grille (0 à 6)
    
    print("   ", end="")
    for i in range(7):
        print(str(i)+" ",end="")
    print("\n  ")
    
    # Affichage des lignes
    
    for i in range(6): 
        print(str(i)+" ",end="")
        for j in range(7): 
            print("|"+ grille[i][j],end="")
        print("|")
        
    # Affichage du trait en bas de la grille    
    print("  ---------------")

# -------- TEST TEMPORAIRE ------------
#
#grille[2][3] = "O"
#grille[5][0] = "X"
#grille[5][1] = "X"






def colonne_pleine(indice_colonne: int) -> bool:
    
    '''
    IN: indice de la colonne à analyser (0 à 6)
    OUT: un booleen (True si la colonne est déjà pleine, False sinon)
'''
    
    global grille
    
    if grille[0][indice_colonne] == "X" or grille[0][indice_colonne] == "O":
        return True
    
    else:
        return False
    
# -------- TEST TEMPORAIRE ------------
#   for i in range(6):
#      grille[i][3] = "X"
#
# affiche_grille()




def joue_jeton(num_joueur: int, indice_colonne: int) -> None:
    
    ''' Place un jeton du joueur numéros num_joueur, dans la colonne␣
    ,indice_colonne.
    IN: num_joueur (int qui vaut 1 ou 2)
    OUT: Rien puisque cette fonction va modifier directement la variable␣
    ,global grille.
    
'''
    
    # On utilise les deux variables globales suivantes
    global grille
    global jetons_joueur
    
    if num_joueur == 1:
        for i in range(5,-1,-1):
            if grille[i][indice_colonne] == ".": # Dans la colonne indice_colonne, en partant, du bas, on cherche la première case vide.
                grille[i][indice_colonne] = jetons_joueur[0]
                return affiche_grille()
            elif grille[i][indice_colonne] == "X" or "O":
                for i in range(5,-1):
                    grille[i-1][indice_colonne] = jetons_joueur[0]
                    return affiche_grille()
            
    elif num_joueur == 2:
        for i in range(5,-1,-1):
            if grille[i][indice_colonne] == ".":
                grille[i][indice_colonne] = jetons_joueur[1]
                return affiche_grille()
            elif grille[i][indice_colonne] == "X" or "O":
                for i in range(5,-1):
                    grille[i-1][indice_colonne] = jetons_joueur[1]
                    return affiche_grille()
                
# ------------ TEST TEMPORAIRE ----------------

#joue_jeton(1, 3) # Joueur 1 joue
#affiche_grille()
#joue_jeton(2, 0) # Joueur 2 joue
#affiche_grille()
#joue_jeton(1, 3) # Joueur 1 joue
#affiche_grille()

        
     
def demander_ou_jouer() -> int:
    
    ''' Doit demander au joueur dans quel indice de colonne il souhaite jouer.
    Si l'indice n'est pas valable (non compris entre 0 et 6), ou bien s'il␣
    ,correspond à une colonne pleine, on lui indique
    que sa saisie est incorrecte et on lui renouvelle la question.
    Si l'utilisateur saisie 'Q' (pour "Quitter"), la partie doit se␣
    →terminer.
    IN: rien
    OUT: Renvoie un indice de colonne (int) valable (colonne non pleine) où␣
    ,→l'on peut jouer.
    
    '''
    
    while True:
        saisie = input("Dans quelle colonne voulez vous jouer (0 à 6 et Q pour quitter)")
    
        if len(saisie)== 1 and (saisie in "0,1,2,3,4,5,6,Q"):
            
            #La saisie est correct (1 seul caractère et il est autorisé)
            if saisie == "Q" :
                exit()
                
            # On vérifie que la colonne n'est pas pleine
            j = int(saisie)
        
            if colonne_pleine(j):
                print("ATTENTION, cette colonne est déjà pleine !")
                
            else:   #Sinon, il y a encore de la place
                    # On renvoie l'indice de la colonne choisie
                return j
    
        else:
            print("SAISIE INCORRECTE")

# ------------ TEST TEMPORAIRE ----------------
'''
colonne = demander_ou_jouer()
joue_jeton(1, colonne) # Joueur 1 joue
affiche_grille()
etc.

'''




def Quatre_jetons_en_ligne(num_joueur: int):
    
    '''
        IN: Numéros du joueur à détecter 1 ou 2
        OUT: booleen (True si 4 jetons alignés trouvés en ligne, False sinon)
    '''
    
    # On déclare les variables globales qui nous seront utiles
    global jetons_joueur
    global grille

    # définition du jeton à trouver
    jeton = jetons_joueur[num_joueur - 1]

    chaine_a_trouver = jeton * 4
    chaine = ""
    for ligne in range(6):
        for i in range(4):
            for colonne in range(4):
                chaine += grille[ligne][colonne + i]
            if chaine == chaine_a_trouver:
                return True
            else:
                chaine = ""

    # Si on arrive ici, c'est qu'aucun alignement de 4 jetons n'a été trouvé en ligne
    return False


# ------------ TEST TEMPORAIRE ----------------
"""
creation_grille_vierge()
joue_jeton(2, 1)
joue_jeton(2, 2)
joue_jeton(2, 3)
joue_jeton(2, 4)
affiche_grille()
print(Quatre_jetons_en_ligne(2))
"""
    


def Quatre_jetons_en_colonne(num_joueur: int):
    '''
        IN: Numéros du joueur à détecter 1 ou 2
        OUT: booleen (True si 4 jetons alignés trouvés en ligne, False sinon)
    '''
    # On déclare les variables globales qui nous seront utiles
    global jetons_joueur
    global grille

    # définition du jeton à trouver
    jeton = jetons_joueur[num_joueur - 1]

    chaine_a_trouver = jeton * 4
    chaine = ""
    for colonne in range(7):
        for i in range(3):
            for ligne in range(4):
                chaine += grille[ligne + i][colonne]
            if chaine == chaine_a_trouver:
                return True
            else:
                chaine = ""

    # Si on arrive ici, c'est qu'aucun alignement de 4 jetons n'a été trouvé en ligne
    return False


# ------------ TEST TEMPORAIRE ----------------
"""
creation_grille_vierge()
joue_jeton(1, 3)
joue_jeton(1, 3)
joue_jeton(1, 3)
joue_jeton(1, 3)
affiche_grille()
print(Quatre_jetons_en_colonne(1))
"""

    
    
    
    
def Quatre_jetons_en_diagonal(num_joueur: int):
    
    '''
        IN: Numéros du joueur à détecter 1 ou 2.
        OUT: booleen (True si 4 jetons alignés trouvés en diagonale, False sinon)
    '''
    global grille
    global jetons_joueur

    jeton = jetons_joueur[num_joueur - 1]

    chaine_a_trouver = jeton * 4
    chaine = ""
    trouve = False
    
    # ------------------------------------------------------
    # PARTIE 1 : Recherche sur les diagonales descendantes vers la droite:
    ''' 
    # On définit la liste des coordonnées des points de départ possible pour les diagonales descendantes vers la droite.
        0   1   2   3   4   5   6
    0   X   X   X   X           
    1   X   X   X   X          
    2   X   X   X   X        
    3                            
    4                      
    5  ___________________________                     

    '''
    
    for i in range(4):
        for j in range(3):
            chaine += grille[j][i]
            chaine += grille[j+1][i+1]
            chaine += grille[j+2][i+2]
            chaine += grille[j+3][i+3]
            if chaine == chaine_a_trouver:
                trouve = True
                break
            else:
                chaine = ""
        if trouve:
            break

    # Si un alignement en diagonale a été trouvé
    if trouve:
        # Une diagonale complète trouvée
        print("VICTOIRE EN DIAGONALE DE " + jeton)
        return True

    # ----------------- FIN PARTIE 1 -----------------------
    # ------------------------------------------------------
    # PARTIE 2 : Recherche sur les diagonales descendantes vers la gauche:
    ''' 
    # On définit la liste des coordonnées des points de départ possible pour les diagonales descendantes vers la gauche.
        0   1   2   3   4   5   6
    0               X   X   X   X
    1               X   X   X   X 
    2               X   X   X   X
    3                            
    4                      
    5  ___________________________                     

    '''

    for i in range(4):
        for j in range(3):
            chaine += grille[j][i+3]
            chaine += grille[j+1][i+2]
            chaine += grille[j+2][i+1]
            chaine += grille[j+3][i]
            if chaine == chaine_a_trouver:
                trouve = True
                break
            else:
                chaine = ""
        if trouve:
            break

    # Si un alignement en diagonale a été trouvé
    if trouve:
        # Une diagonale complète trouvée
        print("VICTOIRE EN DIAGONALE DE " + jeton)
        return True

    # ----------------- FIN PARTIE 2 -----------------

    # Si on arrive ici, aucune diagonale n'a été trouvée, on renvoie False
    return False


# ----------- TEST TEMPORAIRE -------------
"""
creation_grille_vierge()

#test dans la partie de droite
grille[5][6] = "O"
grille[4][5] = "O"
grille[3][4] = "O"
grille[2][3] = "O"

#test dans la partie de gauche
grille[5][0] = "O"
grille[4][1] = "O"
grille[3][2] = "O"
grille[2][3] = "O"

affiche_grille()
print(Quatre_jetons_diagonal(2))
affiche_grille()
"""




def Recherche_si_victoire(num_joueur) -> bool:
    '''
        IN: num_joueur (1 ou 2)
        OUT: un booléen (True si le joueur indiqué a gagné, False sinon)
    '''

    if Quatre_jetons_en_diagonal(num_joueur) or Quatre_jetons_en_colonne(num_joueur) or Quatre_jetons_en_ligne(num_joueur):
        return True
    else:
        return False

# ----------- TEST TEMPORAIRE -------------
"""
creation_grille_vierge()

Test 1 :
grille[5][6] = "O"
grille[4][5] = "O"
grille[3][4] = "O"
grille[2][3] = "O"

Ou un autre test :

joue_jeton(2, 1)
joue_jeton(2, 1)
joue_jeton(2, 1)
joue_jeton(2, 1)
affiche_grille()
print(Recherche_si_victoire(2))
"""





def grille_pleine():
    global grille
    for i in range(6):
        if "." in grille[i]:
            return False
    return True








# --------------------------------------
# -------- PROGRAMME PRINCIPAL ---------
# --------------------------------------

creation_grille_vierge()   
affiche_grille()           


# Tant que la partie n'est pas terminée, un joueur joue.
while partie_terminee == False:

    if num_joueur_courant == 1:
        colonne = demander_ou_jouer()
        joue_jeton(num_joueur_courant, colonne)

    else:
        print("L'ordinateur joue...")
        sleep(0.5)
        joue_jeton(num_joueur_courant, randint(0,7))
        

    if Recherche_si_victoire(num_joueur_courant):
        print("Joueur", num_joueur_courant, "a gagné !")
        break

    if grille_pleine():
        print("Grille remplie, partie terminée")
        break

    # On change le numéros du joueur courant
    if num_joueur_courant == 1:
        num_joueur_courant = 2
    else:
        num_joueur_courant = 1

# FIN DU WHILE

# On est sorti de la boucle donc:
print("FIN DE PARTIE")