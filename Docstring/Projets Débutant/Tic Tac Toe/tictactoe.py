

def printBorad(P):    
    print ("| "+P[0]+" | "+P[1]+" | "+P[2]+" | \n" \
    "----*---*---*\n" \
    "| "+P[3]+" | "+P[4]+" | "+P[5]+" | \n" \
        "----*---*---*\n" \
    "| "+P[6]+" | "+P[7]+" | "+P[8]+" | \n" \
    )

def jouer(P,roundPlay):

    if roundPlay == 10:
        print("partie terminée Score Nule")
        return 1

    if roundPlay % 2 == 1:
        joueur = "Joueur 1"
        sign = "X"
    else :
        joueur = "Joueur 2"
        sign = "O"
        
    choice = int(input(f"{joueur} choisir une case: "))
    if P[choice-1].isdigit() :
        P[choice-1] = sign
        if win(P,sign) == 1 :
            print(f"le {joueur} a gagné")
            printBorad(P)
            return 1
        else :
            roundPlay += 1
            print("La partie continue")
            printBorad(P)
            jouer(P,roundPlay)

    else :
        print("Cette case a deja été choisit")
        jouer(P,roundPlay)
            
   
def win(P,player):
    if P[0] == player and P[1] == player and P[2] == player :        
        return 1
    if P[3] == player and P[4] == player and P[5] == player :        
        return 1
    if P[6] == player and P[7] == player and P[8] == player :        
        return 1
    if P[0] == player and P[3] == player and P[6] == player :        
        return 1
    if P[1] == player and P[4] == player and P[7] == player :        
        return 1
    if P[2] == player and P[5] == player and P[8] == player :        
        return 1
    if P[0] == player and P[4] == player and P[8] == player :        
        return 1
    if P[2] == player and P[4] == player and P[6] == player :
        print(f"Player {player} won the game")         
        return 1
    return 0