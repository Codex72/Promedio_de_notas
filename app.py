
print("Notas del Lapso 1")
lapso1 = input()
lapso1 = float(lapso1)

print("Notas del Lapso 2")
lapso2 = input()
lapso2= float(lapso2)

print("Notas del Lapso 3")
lapso3 = input()
lapso3 = float(lapso3)


# Paso numero 2 sumar los 3 lapsos

promedio = lapso1 + lapso2 + lapso3
promedio = promedio / 3
promedio = round(promedio, 1)
promedio = str(promedio)
print("el Promedio Del Estudiante es de " + promedio)
