def calcul():
    a = float(input("poids  --> "))
    b = float(input("nombre de rep --> "))

    result1 = a / (1.0278 - 0.0278 * b)
    result1a = round(result1, 1)
    
    result2 = 0.9 * result1
    result2a = round(result2, 1)
    
    result3 = 0.8 * result1
    result3a = round(result3, 1)
    
    result4 = 0.7 * result1
    result4a = round(result4, 1)
    
    result5 = 0.6 * result1
    result5a = round(result5, 1)
    
    result6 = 0.5 * result1
    result6a = round(result6, 1)


    return result1a, result2a, result3a, result4a, result5a, result6a

#percentage = 

for k in range(10):
    pr_estime, _90_1rm, _80_1rm, _70_1rm,_60_1rm, _50_1rm  = calcul()
    print("PR estimé =", pr_estime)
    print("90% de 1RM =", _90_1rm, " --> 4 rep" )
    print("80% de 1RM =", _80_1rm, " --> 8 rep")
    print("70% de 1RM =", _70_1rm, " --> 11 rep")
    print("60% de 1RM =", _60_1rm, " --> 15 rep")
    print("50% de 1RM =", _50_1rm, " --> 19 rep")
    