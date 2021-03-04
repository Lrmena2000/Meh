import funcion  # Se debe llamar el codigo creado para correr el pytest


def test_cap_switch():
    letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
              "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
              "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
              "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    res = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
           "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for i in range(51):
        resultado = funcion.cap_switch(letras[i])
        assert resultado == res[i]


'''
test_cap_switch hace una prueba para cada letra mayuscula y minuscula
valida de la lista letras y compara el resultado con los
elementos de la lista res, que corresponden
a las respuestas esperables de la operacion cap_switch.
'''


def test_check_char1():
    letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
              "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
              "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
              "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for i in range(51):
        resultado = funcion.check_char(letras[i])
        assert resultado == 0


'''
test_check_char1 se encarga de probar la  función check_char introduciendo
cada caracter dentro del rango A-Z, tanto mayúscula como minúscula
y revisa que retorne como resultado el codigo 0
'''


def test_check_char2():
    letra = "aA"
    resultado = funcion.check_char(letra)
    assert resultado == 1


'''
test_check_char2 se encarga de probar la  función check_char introduciendo
dos caracteres dentro del rango A-Z, tanto mayúscula como minúscula
y revisa que esta retorne como resultado el codigo 1
    '''


def test_check_char3():
    letra = ",1"
    resultado = funcion.check_char(letra)
    assert resultado == 2


'''
test_check_char3 se encarga de probar la  función check_char introduciendo
dos caracteres fuera del rango A-Z, y revisa que esta
retorne como resultado el codigo 2
'''


def test_check_char4():
    letra = 47
    resultado = funcion.check_char(letra)
    assert resultado == 3


'''
test_check_char4 se encarga de probar la  función check_char introduciendo
dos caracteres que no son del tipo string, y revisa que esta
retorne como resultado el codigo 3
'''
