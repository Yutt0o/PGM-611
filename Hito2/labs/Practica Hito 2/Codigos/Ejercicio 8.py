n1 = input("Introdusca un Valor entre A, B")
rs = input("Introdusca la funcion suma (+)")
n2 = input("Introdusca un Valor entre A, B")

if n1 == "A":
    a1 = 2
elif n1 == "B":
    a1 = 6
if n2 == "A":
    b2 = 2
elif n2 == "B":
    b2 = 6

if rs == "+":
    print(n1, rs, n2, '=')
    if a1 == b2:
        if a1 == 2:  
            print('Resp A')
        else:
            print('Resp B')
    else:
        sum = a1 + b2
        if sum == 8:
            print('Resp F')