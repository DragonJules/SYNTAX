import random

essais = 0
prix = random.randint(1,1000)

userinput = 0

while not userinput == prix:
    userinput = int(input("Entrer un prix entre 1 et 1000\n>>> "))

    if userinput < prix:
        print("C'est plus")
    elif userinput > prix:
        print("C'est moins")
    
    essais = essais + 1
    


print("Bravo c'etait",str(prix),"Trouvé en",str(essais),"essais")