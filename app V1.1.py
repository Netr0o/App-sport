def calcul():
    a = int(input("poids (en kg) --> "))
    b = int(input("nombre de rep --> "))

    result1 = a / (1.0278 - 0.0278 * b)
    result2 = 0.9 * result1
    result3 = 0.8 * result1
    result4 = 0.7 * result1
    result5 = 0.6 * result1
    result6 = 0.5 * result1

    return result1, result2, result3, result4, result5, result6

for k in range(10):
    pr_estime, _90_1rm, _80_1rm, _70_1rm,_60_1rm, _50_1rm  = calcul()
    print("PR estimé =", pr_estime)
    print("90% de 1RM =", _90_1rm)
    print("80% de 1RM =", _80_1rm)
    print("70% de 1RM =", _70_1rm)
    print("60% de 1RM =", _60_1rm)
    print("50% de 1RM =", _50_1rm)