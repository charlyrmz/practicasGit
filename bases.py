#Tipos de datos
x = "Hola mundo"
y = 69

print(x)
print(type(x))
print(id(x))
print(y)
print(type(y))
print(id(y))
print("")

print("\n--------------------------------------------------")
lista = [[1], [3, 4], [5, 6, 7]]
otralista = [["Hola mundo", 16], [69, 42, 21], ['3', 11, "nais"]]
print(lista)
print(lista[0][0])
print(lista[1][1])
print(lista[2][0])
print(otralista)
print(otralista[0][0])
print(otralista[1][2])
print(otralista[2][0])
print("")

print("\n--------------------------------------------------")
diccionario = {'nombre': "Paco", 'peso': 65.8, 'soltero': True}
print(diccionario)
print(diccionario['nombre'])
print(diccionario['peso'])
print(diccionario['soltero'])
print("")

#Concatenacion
print("\n--------------------------------------------------")
frutaFav = "mango"
añadido = "con chile"

print("Mi botana favorita es", frutaFav, añadido)

print("\n--------------------------------------------------")
x = 1
y = 2
print(x + y)

x = "1"
y = "2"

print(x + y)
print("")

print("\n--------------------------------------------------")
# cadenas
cadena = "hola, {}{}"
valor = "perro"
otra_cadena = cadena.format(valor, ". Buenos dias")

print(otra_cadena)
print("")

print("\n--------------------------------------------------")
#Booleanos
variable = 10 > 100
print(variable)

if variable:
    print("El resultado es verdadero")

else:
    print("El resultado es falso")

variable = 100 > 10
print(variable)

if variable:
    print("El resultado es verdadero")

else:
    print("El resultado es falso")
print("")

print("\n--------------------------------------------------")
# funciones
def sumar(m, n):
    return m + n

print(sumar(5, 2))
print(sumar(1, 2))
print("")

print("\n--------------------------------------------------")
#funcion tipo switch
def opcion(n):
    if n == 1:
        return "Opcion 1"
    elif n == 2:
        return "Opcion 2"
    elif n == 3:
        return "Opcion 3"
    elif n == 4:
        return "Opcion 4"
    else:
        return "Opcion no valida"

print(opcion(7))
print("")

print("\n--------------------------------------------------")
#while
n = 0
while(n <= 5):
    print("A", n)
    n += 1
print("")

print("\n--------------------------------------------------")
#rango
#range(0,7,2) ::: inicio, fin, paso ::: 1, 2, 3
for x in range(10, 4, -1):
    print(x)

print("\n--------------------------------------------------")
#Entrada de usuario
resultado = input("Escribe un mensaje: ") #Unicamente para valores de tipo str
print("Valor proporcionado: ", resultado)
print("Fin del programa")
print("")

num1 = int(input("Escribe un el primer numero: ")) #Para valores de tipo int
num2 = int(input("Escribe un el segundo numero: "))
resultado = num1 + num2
print("El resultado de la suma es: ", resultado)
print("Fin del programa")