def calcul(poids, rep):
    result1 = poids / (1.0278 - 0.0278 * rep)
    result1a = round(result1, 1)

    pourcentages = [0.9, 0.8, 0.7, 0.6, 0.5]
    resultats = [round(p * result1, 1) for p in pourcentages]

    return result1a, *resultats

poids = float(input("Poids (en kg) --> "))
rep = float(input("Nombre de rep --> "))

# Calculer une seule fois en dehors de la boucle
pr_estime, _90_1rm, _80_1rm, _70_1rm, _60_1rm, _50_1rm = calcul(poids, rep)

# Afficher les résultats une seule fois
print("PR estimé =", pr_estime)
print("90% de 1RM =", _90_1rm, " --> 4 rep")
print("80% de 1RM =", _80_1rm, " --> 8 rep")
print("70% de 1RM =", _70_1rm, " --> 11 rep")
print("60% de 1RM =", _60_1rm, " --> 15 rep")
print("50% de 1RM =", _50_1rm, " --> 19 rep")