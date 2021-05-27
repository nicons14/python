def promedio_salarial(Laura: int, Juan: int, Andres: int, Sara: int, Natalia: int):
    Laura = Laura * 3600
    Juan = Juan
    Andres = Andres
    Sara = Sara * 3600
    Natalia = Natalia * 3600
    promedio_salarial = (Laura + Juan + Andres + Sara + Natalia)/5
    Resultado="El promedio salarial es: " + str(promedio_salarial) + " pesos colombiamos"
    
    return Resultado

#promedio_salarial (1050, 180000, 2750000, 2100, 3500)
print(promedio_salarial(1050,1800000,2750000,2100,3500))
