import math

# Pedir las coordenadas de los dos puntos
x1 = float(input("Ingresa x1: "))
y1 = float(input("Ingresa y1: "))
x2 = float(input("Ingresa x2: "))
y2 = float(input("Ingresa y2: "))

# Calcular las diferencias
dx = x2 - x1
dy = y2 - y1

# Calcular el ángulo en radianes con atan2
angulo_rad = math.atan2(dx, dy)

# Convertir a grados
angulo_deg = math.degrees(angulo_rad)

# Asegurar que el ángulo esté entre 0 y 360
if angulo_deg < 0:
    angulo_deg += 360

# Mostrar el resultado
print(f"El azimut entre los puntos es: {angulo_deg:.2f} grados")