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


print(cap_switch("d"))