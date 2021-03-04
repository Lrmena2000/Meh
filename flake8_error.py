def is40(numA, numB):
    addition = numA + numB
    if (addition == 40):
        return 1
    else:
        return 0


firstNum = 20
secondNum = 20
if(is40(firstNum, secondNum) == 1):
    print("¡Es 40!")
else:
    print("No es 40")
