# Importer le dictionnaire de phrases
from dictionary import phrases

langue = 'fr'  # Choisissez la langue (fr, en, es, it)

# Fonctions
def par_defaut():
    # Afficher le message de bienvenue
    print(phrases['bienvenue'][langue])

def regles():
    print(phrases['regles'][langue])
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    #print("Les positions de ce tableau 3 x 3 sont les mêmes que celles du côté droit de votre clavier.\n")
    print(phrases['conclusion_regles'][langue])

def jouer():
    while True:
        user_input = input(phrases['pret_a_jouer'][langue]).lower()
        if user_input.startswith('o') or user_input.startswith('y') or user_input.startswith('s'):
            return True
        elif user_input.startswith('n'):
            return False
        else:
            print(phrases['entree_invalide'][langue])
def noms():
    # Saisir les noms des joueurs
    p1_name = input("\nEntrez↩ le NOM du joueur 1 : ").capitalize()
    p2_name = input("Entrez↩ le NOM du joueur 2 : ").capitalize()
    return (p1_name, p2_name)

def choix():
    # Saisir le choix des joueurs
    p1_choice = " "
    p2_choice = " "
    
    # Boucle while : si la valeur entrée n'est pas X ou O
    while p1_choice != "X" or p1_choice != "O":           
        # Corps de la boucle while commence
        p1_choice = input(f"\n{p1_name}, Veux-tu être ❌ ou ⭕ ? : ")[0].upper()
        # L'entrée ci-dessus a [0].upper() à la fin,
        # Donc même si l'utilisateur entre x, X, xxxx ou XXX, l'entrée sera toujours prise comme X.
        # Ainsi, en augmentant la fenêtre d'entrée utilisateur.

        if p1_choice == "X" or p1_choice == "O":
            # si la valeur entrée est X ou O, mettre fin à la boucle.
            break
        print("ENTRÉE INVALIDE🚫 ! Veuillez réessayer !") 
        # si la valeur entrée n'est pas X ou O, redémarrer la boucle while.
        # Le corps de la boucle while commence
        
    # Attribution de la valeur à p2 et puis affichage des valeurs
    if p1_choice == "X":
        p2_choice = "O"
    elif p1_choice == "O":
        p2_choice = "X"    
    return (p1_choice, p2_choice)

def premier_joueur():
    # Cette fonction décidera de manière aléatoire qui jouera en premier
    import random
    return random.choice((0, 1))

def afficher_tableau(board, avail):
    print("    " + " {} | {} | {} ".format(board[1], board[2], board[3]) + "            " + " {} | {} | {} ".format(avail[1], avail[2], avail[3]))
    print("    " + "-----------" + "            " + "-----------")
    print("    " + " {} | {} | {} ".format(board[4], board[5], board[6]) + "            " + " {} | {} | {} ".format(avail[4], avail[5], avail[6]))
    print("    " + "-----------" + "            " + "-----------")
    print("    " + " {} | {} | {} ".format(board[7], board[8], board[9]) + "            " + " {} | {} | {} ".format(avail[7], avail[8], avail[9]))

def choix_joueur(board, name, choice):
    while True:
        try:
            position = int(input(f"\n{name} ({choice}), Choisissez votre prochaine position : (1-9) : "))

            if 1 <= position <= 9 and verifier_espace(board, position):
                break
            else:
                print("ENTRÉE INVALIDE🚫 ! Veuillez entrer une position valide et non occupée (1-9).")
        except ValueError:
            print("ENTRÉE INVALIDE🚫 ! Veuillez entrer un entier valide.")

    return position

#####################################

# Fonctions pour ajouter l'IA au jeu
def IA(board, name, choice):
    possibilities = [x for x, letter in enumerate(board) if letter == " " and x != 0]

    for let in ["O", "X"]:
        for i in possibilities:
            boardCopy = board[:]
            boardCopy[i] = let
            if verifier_victoire(boardCopy, let):
                return i

    coins_ouverts = [x for x in possibilities if x in [1, 3, 7, 9]]
    bords_ouverts = [x for x in possibilities if x in [2, 4, 6, 8]]

    mouvements_preferes = coins_ouverts + [5] + bords_ouverts

    for position in mouvements_preferes:
        if position in possibilities:
            return position

    # Si aucune des stratégies ci-dessus n'est applicable, choisissez une position au hasard
    return choisir_aleatoire(possibilities)

def choisir_aleatoire(board):
    import random
    ln = len(board)
    r = random.randrange(0,ln)
    return board[r]

def placer_marque(board, avail, choice, position):
    # Pour marquer/remplacer la position dans la liste du tableau
    board[position] = choice
    avail[position] = " "

def verifier_espace(board, position):
    # Pour vérifier si la position donnée est vide ou occupée
    return board[position] == " "

def verifier_tableau_plein(board):
    # Pour vérifier si le tableau est plein, alors le jeu est une égalité
    for i in range(1, 10):
        if verifier_espace(board, i):
            return False
    return True

def verifier_victoire(board, choice):
    # Liste des combinaisons gagnantes (rangées, colonnes, diagonales)
    combinaisons_gagnantes = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Horizontale
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Verticale
        [1, 5, 9], [3, 5, 7]              # Diagonale
    ]

    # Vérifier si l'une des combinaisons gagnantes correspond aux choix du joueur
    for combinaison in combinaisons_gagnantes:
        if all(board[position] == choice for position in combinaison):
            return True

    return False


def retarder(mode):
    if mode == 2:
        import time
        time.sleep(2)

def rejouer():
    # Si les joueurs veulent rejouer ?
    while True:
        user_input = input("\nVoulez-vous rejouer ? 🔁 Entrez [O]ui ou [N]on : ").lower()
        if user_input.startswith('o') or user_input.startswith('y') or user_input.startswith('s'):
            return True
        elif user_input.startswith('n'):
            return False
        else:
            print("ENTRÉE INVALIDE🚫 ! Veuillez entrer [O]ui ou [N]on.")

# Début du programme principal
input("Appuyez sur ENTER↩ pour commencer▶")
par_defaut()
regles()

#####################################

while True:
    
    # Création du tableau comme une liste à remplacer avec l'entrée utilisateur
    theBoard = [" "]*10
    
    # Création des options disponibles sur le tableau
    disponible = [str(num) for num in range(0, 10)] # une Compréhension de Liste
    # disponible ➡ "0 1 2 3 4 5 6 7 8 9"
    
    print("\n0️⃣➡ 👱 🆚 🤖")
    print("1️⃣➡ 👱 🆚 👱‍♀️")
    print("2️⃣➡ 🤖 🆚 🤖")
    try:
        mode = int(input("\nSélectionnez↩ une option 0, 1 ou 2 : "))

        if mode not in [0, 1, 2]:
            raise ValueError("Choix invalide ! Veuillez entrer 0, 1 ou 2.")
    except ValueError as e:
        print(f"Erreur : {e}")
        continue
    
    # Mode pour 👱 🆚 🤖
    if mode == 0:  
        p1_name = input("\nEntrez↩ le NOM du joueur qui va affronter l'ordinateur : ").capitalize()
        p2_name = "🤖"
        # Demande de choix et affichage des choix➡ X ou O
        p1_choice, p2_choice = choix()
        print(f"\n👱{p1_name} : {p1_choice}")
        print(f"{p2_name} : {p2_choice}")

    # Mode pour 👱 🆚 👱‍♀️
    elif mode == 1:
        # Demander les noms
        p1_name, p2_name = noms()
        # Demande de choix et affichage des choix➡ X ou O
        p1_choice, p2_choice = choix()
        print(f"\n👱{p1_name} : {p1_choice}")
        print(f"👱‍♀️{p2_name} : {p2_choice}")
        
    # Mode pour 🤖 🆚 🤖
    else:
        p1_name = "🤖1️⃣"
        p2_name = "🤖2️⃣"
        p1_choice, p2_choice = "X", "O"
        print(f"\n{p1_name} : {p1_choice}")
        print(f"\n{p2_name} : {p2_choice}")
   
    # Affichage aléatoire de qui commencera
    if premier_joueur():
        turn = p2_name
    else:
        turn = p1_name
    print(f"\n{turn} commencera en premier !☝️")
    
    #  L'utilisateur, s'il est prêt à jouer, la sortie sera True ou False
    if(mode == 2):
        ent = input("\nCela va être rapide ! Appuyez sur Enter↩ pour que la bataille commence !\n")
        play_game = 1
    else:
        play_game = jouer()   
    
    while play_game:
        
#####################################
        # Joueur_1
        if turn == p1_name:
            
            # Affichage du tableau
            afficher_tableau(theBoard, disponible)

            # Position de l'entrée
            if mode != 2:
                position = choix_joueur(theBoard, p1_name, p1_choice)
            else:
                position = IA(theBoard, p1_name, p1_choice)
                print(f"\n{p1_name} ({p1_choice}) a choisi la position : {position}\n")
            
            # Remplacer le " " à la *position* par *p1_choice* dans la liste *theBoard*
            placer_marque(theBoard, disponible, p1_choice, position)
            
            # Vérifier si le Joueur_1 a gagné après l'entrée actuelle
            if verifier_victoire(theBoard, p1_choice):
                afficher_tableau(theBoard, disponible)
                print("\n************************************************")
                if(mode >= 0):
                    print(f"\nFÉLICITATIONS {p1_name} ! Vous avez remporté la partie ! \n")
                play_game = False
                
            else:
                # Vérifier si le tableau est plein, si oui, la partie est nulle
                if verifier_tableau_plein(theBoard):
                    afficher_tableau(theBoard, disponible)
                    print("******************")
                    print("\nLa partie est nulle  !\n")
                    print("******************")
                    break
                # Si aucune des stratégies ci-dessus n'est applicable, prochain tour du Joueur_2      
                else:
                    turn = p2_name        
#####################################
        # Joueur_2            
        elif turn == p2_name:
            
            # Affichage du plateau
            afficher_tableau(theBoard, disponible)

            # Position de l'entrée
            if(mode == 1):
                position = choix_joueur(theBoard, p2_name, p2_choice)
            else:
                position = IA(theBoard, p2_name, p2_choice)
                print(f"\n{p2_name} ({p2_choice}) a choisi la position : {position}\n")
            
            # Remplacement de " " à la *position* par *p2_choice* dans la liste *theBoard*
            placer_marque(theBoard, disponible, p2_choice, position)
            
            # Vérification si le Joueur_2 a gagné après l'entrée actuelle
            if verifier_victoire(theBoard, p2_choice):
                afficher_tableau(theBoard, disponible)
                print("\n************************************************")
                if(mode):
                    print(f"\nFÉLICITATIONS {p2_name} ! Vous avez gagné la partie ! \n")
                else:
                    print("\nL'ordinateur a remporté la partie ! \n")
                print("************************************************")
                play_game = False
                
            else:
                # Vérification si le plateau est plein, si oui, la partie est nulle
                if verifier_tableau_plein(theBoard):
                    afficher_tableau(theBoard, disponible)
                    print("******************")
                    print("\nLa partie est nulle ! 😑\n")
                    print("******************")
                    break
                # Si aucune des situations ci-dessus n'est possible, prochain tour du Joueur_2      
                else:
                    turn = p1_name        
                    
    # Si les utilisateurs veulent rejouer à la partie?                
    if rejouer():
        # si Oui
        continue
    else:
        # si Non
        break        

# Message de fin
print("\n\n\t\t\t**FIN**")  

