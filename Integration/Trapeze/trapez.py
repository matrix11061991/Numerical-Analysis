def trapeze(f, a, b, n):
    # Étape 1 : déterminer l'espacement entre les points de la grille
    h = (b-a)/n

    # Étape 2 : calculer la valeur de l'intégrale en utilisant la méthode des trapèzes
    resultat = 0.5*(f(a) + f(b))
    for i in range(1, n):
        resultat += f(a + i*h)
    resultat *= h

    return resultat

