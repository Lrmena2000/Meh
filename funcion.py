def check_char (char):
    '''Los valores de codigo representan:
    codigo = 0: Se recibió un único caracter entre A-Z
    codigo = 1: Se recibió más de un caracter en el rango A-Z
    codigo = 2: Se recibió uno o más caracteres fuera del rango A-Z
    codigo = 3: Se recibió uno o más caracateres que no son del tipo string
    '''
    tipo = type(char) #Para determinar el tipo de variable que es char
    codigo = 0 #Variable que establece el codigo de error, según el contenido de la variable char
    rango = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Cadena de caracteres que se utilizaran para saber si el dato ingresado se encuentra dentro del rango A-Z 
    if tipo == str: #Si la variable es de tipo string, se procede a realizar otras comprobaciones
        tam = len (char) #Para medir la cantidad de caracteres de la palabra
        char = char.upper() #Para hacer todas las letras mayusculas y evitar problemas relacionados con ello
        if tam >1: #Si el tamaño es mayor a 1 caracter, se procede a indetificar si está dentro del rango A-Z
            cont1 = 0 #Variable que lleva el conteo de los caracteres
            ctrl = 0 #Variable que controla cuando se sale del bucle while
            while ctrl == 0: #Bucle while
                for lett in char: #Ciclo que revisa cada caracter y lo compara con los que se encuentran en la cadena de rango
                    cont1 = cont1 +1 #Cada vez que se inicia el ciclo, se suma 1 al conteo
                    if codigo == 2: #Si codigo tiene un valor de 2, char tiene caracteres fuera del rango A-Z, no es necesario revisar más y se sale del bucle while 
                        ctrl = 1 
                        break
                    if cont1 == tam +1: #Si el contador es más grande que el tamaño de la palabra, entonces todos los caracteres están dentro del rango A-Z y se sale del bucle while
                        codigo = 1
                        ctrl = 1
                        break
                    for alph in rango: #Ciclo en el que se comprueba si cada caracter está dentro del rango A-Z
                        if lett == alph:
                            codigo = 1
                            break
                        if alph == "Z" and lett != alph: #Si ya se llegó a Z y el caracter no coincide, se asigna un valor de 2 a codigo
                            codigo = 2
        else: #Si el tamaño de char es de 1 solo caracter se procede a comprobar si está dentro del rango A-Z
            for alph in rango:
                        if char == alph: #Si el caracter está dentro del rango, se asigna un valor de 0 a codigo
                            codigo = 0
                            break
                        if alph == "Z" and char != alph: #Si el caracter llegó a Z y no coincide, entonces se asigna un valor de 2 a codigo
                            codigo = 2

    else: #Si char no es del tipo string, entonces se asigna directamente un valor de 3 a codigo
        codigo = 3
    return codigo


def cap_switch(char_in):
    verificar = check_char(char_in)
    if (verificar == 0):
        if char_in.isupper():
            char_in = char_in.lower() 
        elif char_in.islower():
            char_in = char_in.upper()
        return char_in
    else:
        return verificar


def test_cap_switch():
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    res = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in range(51):
        resultado = cap_switch(letras[i])
        print(resultado, res[i])
        if resultado == res[i]:
            print("yes")
        else:
            print("no")
test_cap_switch()