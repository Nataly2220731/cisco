str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)

ch1 = "@"
ch2 = ' ' # espacio
ch3 = "["
ch4 = "{"

print(ord(ch1))
print(ord(ch2))
print(ord(ch3))
print(ord(ch4))

print(chr(64))
print(chr(124))
print(chr(48))

alpha = "abcdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[::2])
print(alpha[::3])
print(alpha[1::2])

alpfabeto = "abcdefghijklmnopqrstuvwxyz"

print("f" in alpfabeto)
print("F" in alpfabeto)
print("l" in alpfabeto)
print("ghi" in alpfabeto)
print("Xyz" in alpfabeto)

alfabeto = "bcdefghijklmnopqrstuvwxy"

alfabeto = "a" + alfabeto
alfabeto = alfabeto + "z"

print(alfabeto)

# Demonstrando min() - Ejemplo 1
print(min("aAbByYzZ"))

t= [0, 1, 2]
print(min(t))

# Demonstrando max() - Ejemplo 1
print(max("aAbByYzZ"))

# Demonstrando max() - Ejemplo 2 y 3
t = 'Los Caballeros Que Dicen"¡Ní!"'
print('[' + max(t) + ']')

t= [0, 1, 2]
print(max(t))

# Demostrando del metodo replace ()
print("www.netacad.com".replace ("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

# Demostracion del método swapcase ()
print ("Yo sé que no sé nada.".swapcase())

print ()

# Demostracion del método title()
print("Yo sé que no sé nada. Parte 1.".title
      ())

print ()

# Demostracion del método upper ()
print ("Yo sé que no sé nada. Parte 2.".upper
       ())

# Demostracion del método sort()
secondGreek = ['omega', 'alfa', 'pi', 'gama']
print (secondGreek)

secondGreek.sort()
print (secondGreek)

# Demostracion del método the isalnum()
print('lambda 30'.isalnum())
print ('lambda'.isalnum())
print ('30'.isalnum())
print ('@'.isalnum())
print ('lambda_30'.isalnum())
print (''.isalnum())


# Ejemplo 1: Demostracion del método isaph a()
print("Moooo".isalpha())
print('Mu40'.isalpha())

# Ejemplo 2: Demostracion del método isdig it()

print('2018'.isdigit())
print("Año2019".isdigit())

