n = int(input("Introdusca el Numero: "))
n1 = 0
n2 = 1
count = 0
if n <= 0:
    print("Introduce un numero mayor a 0 ")
elif n <= 1:
    print("La secuencia Fibonacci de", n ,"es:", n, ":")
else:
    print("La secuencia Fibonacci de", n , "es:")
    while count < n:
        print(n1)
        sum = n1 + n2
        n1 = n2
        n2 = sum
        count += 1
    