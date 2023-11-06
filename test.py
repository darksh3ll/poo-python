from time import sleep

# La valeur de départ.
a = 0

# La direction du rebond : 1 pour l'incrément, -1 pour le décrément.
direction = 1

# Boucle 40 fois pour faire rebondir `a` entre 0 et 20 deux fois.
for _ in range(40):
    # Affiche la valeur actuelle de `a`.
    print(a)
    
    # Pause de 1 seconde.
    sleep(1)
    
    # Incrémente ou décrémente `a` selon la direction.
    a += direction
    
    # Inverse la direction si `a` atteint 20 ou 0.
    if a == 10 or a == 0:
        direction *= -1
