
from functools import reduce

estudiantes = (
    ("Andreina", (9, 8, 10)),
    ("Anay", (6, 7, 5)),
    ("Maryuri", (10, 9, 9)),
    ("Maria", (4, 6, 5))
)

promedio = lambda notas: reduce(lambda a, b: a + b, notas) / len(notas)

calcular_finales = lambda data: tuple(
    map(lambda e: (e[0], promedio(e[1])), data)
)

finales = calcular_finales(estudiantes)

prom_curso = promedio(tuple(map(lambda e: e[1], finales)))

print("Calificaciones finales:", finales)
print("Promedio del curso:", prom_curso)
