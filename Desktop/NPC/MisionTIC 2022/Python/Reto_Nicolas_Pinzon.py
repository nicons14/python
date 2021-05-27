"""
nota1 = input ("ingrese nota 1: ")
nota2 = input ("ingrese nota 2: ")
nota3= input ("ingrese nota 3: ")
nota4 = input ("ingrese nota 3: ")

nota1 = float(nota1)
nota2 = float(nota2)
nota3= float(nota3)
nota4 = float(nota4)

Promedio = (nota1 + nota2 + nota3 + nota4)/4
print("El promedio de la nota es: " + str(Promedio))
"""
"""
def promedio_salarial(Laura: int, Juan: int, Andres: int, Sara: int, Natalia: int) -> str:
    Laura = input (float ("Ingrese el salario: "))
    Juan = input (float ("Ingrese el salario: "))
    Andres = input (float ("Ingrese el salario: "))
    Sara = input (float ("Ingrese el salario: "))
    Natalia = input (float ("Ingrese el salario: "))

    Laura = Laura * 3600
    Sara = Sara * 3600
    Natalia = Natalia * 3600

    promedio = (Laura + Juan + Andres + Sara + Natalia)
    print("El promedio salarial es: " + str(promedio))
    """

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
