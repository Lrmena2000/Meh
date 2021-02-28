def check_char (char):
    tipo = type(char)
    codigo = 0
    rango = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if tipo == str:
        tam = len (char)
        char = char.upper()
        if tam >1:
            cont1 = 0 
            ctrl = 0 

            while ctrl == 0:
                for lett in char:
                    cont1 = cont1 +1
                    if codigo == 2 and cont1 == tam +1:
                        ctrl = 1 
                        break
                    if cont1 == tam +1:
                        codigo = 1
                        ctrl = 1
                        break
                    for alph in rango:
                        if lett == alph:
                            codigo = 1
                            break
                        if alph == "Z" and lett != alph:
                            ctrl = 1
                            codigo = 2
                            cont1 = tam
        else:
            for alph in rango:
                        if char == alph:
                            codigo = 0
                            break
                        if alph == "Z" and char != alph:
                            codigo = 2

    else:
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