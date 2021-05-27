"""
def nota_estudiante(nota: float):
    aprobo: bool = False
    if nota > 3:
        aprobo = True
    else:
        aprobo = False
    return aprobo


estado_curso = nota_estudiante(float(input("Por favor ingrese la nota del estudiante: ")))

if estado_curso == True:
    print("Aprobó la materia")
else:
    print("Reprobó")
"""
#Condicionales en cascada
"""
nota_minima = 3
nota_estudiante = 4
if nota_estudiante < nota_minima and nota_estudiante > 1:
    print("En el rango de 1 a 2.9")
elif nota_estudiante >= nota_minima and nota_estudiante < 4:
    print("En el rango de 3 a 3.9")
elif nota_estudiante >= 4:
    print("Nota mayor o igual a 4")
"""

def promedio_ventas(dia1,dia2,dia3,dia4):
    promedio= (dia1+dia2+dia3+dia4)/4
    if (promedio < 100):
        return ("se encuentra en un nivel crítico")
    

dia1= 20
dia2= 20
dia3= 20
dia4= 20

print(promedio_ventas(dia1,dia2,dia3,dia4))