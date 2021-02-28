import funcion


def test_check_char2():
    letra = "aa"
    resultado = funcion.check_char(letra)
    assert resultado == 1


def test_check_char3():
    letra = ",1"
    resultado = funcion.check_char(letra)
    assert resultado == 2


def test_check_char4():
    letra = 47
    resultado = funcion.check_char(letra)
    assert resultado == 3
