from datetime import date
import math


diaNacimiento = int(input("Día: "))
mesNacimiento = int(input("Mes: "))
anoNacimiento = int(input("Año: "))


fechaNacimiento = date(anoNacimiento, mesNacimiento, diaNacimiento)
edad = date.today() - fechaNacimiento

fisico = (math.sin((2*math.pi*edad.days) / 23))*100
emocional = (math.sin((2*math.pi*edad.days) / 28))*100
intelectual = (math.sin((2*math.pi*edad.days) / 33))*100
intuicional = (math.sin((2*math.pi*edad.days) /38))*100

print("Nivel físico: ", '% .2f' % fisico)
print("Nivel emocional: ", '% .2f' % emocional)
print("Nivel intelectual: ", '% .2f' % intelectual)
print("Nivel intuicional: ", '% .2f' % intuicional)