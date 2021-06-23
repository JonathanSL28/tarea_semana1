class Deber:
    def __init__(self):
        pass

    def Oparitmeticos(self):
        num1=float(input("1° valor"))
        num2=float(input("2° valor"))
        suma=num1+num2
        resta=num1-num2
        multi=num1*num2
        div=num1/num2
        print("Suma es:{},Resta es:{}, Multiplicación es:{}, Division es:{}".format(suma,resta,multi,div,mod))

    def Relacionales(self):
        a=float(input("1° valor"))
        b=float(input("2° valor"))
        c=float(input("3° valor"))
        if a<=b:
            print("El 1° valor es menor o igual al 2°")

    def Aritmeticos(self):
        n1=float(input("1° valor"))
        n2=float(input("2° valor"))
        res=(n1/n1+n2)/(n2/n2-n1)
        print("Resultado de la operacion es:",res)

    def Secuencial(self):
        val1=float(input("Ingrese 1 total de la compra"))
        val2=float(input("Ingrese 2 total de la compra"))
        val3=float(input("Ingrese 3 total de la compra"))
        des=(val1+val2+val3)*0.1
        total=val-des
        print("El valor total a pagar ya con descuento es:{}".format(total))

    def Selectiva(self):
        sue=float(input("Ingresar sueldo de un trabajador"))
        if sue <600:
            nsue=sue+sue*0.10
        else:
            nsue=sue
        print("Si sueldo final es de:{}".format(nsue))


    def Compuesta(self):
        n1= float(input("Ingresar numero 1"))
        n2= float(input("Ingresar numero 2"))
        n3= float(input("Ingresar numero 3"))
        if (n1>n2) and (n1>n3):
            tt=n1
        elif n2>n3:
            tt=n2
        else:
            tt=n3
        print("El numero mayor es:{}".format(tt))

    def Forciclo(self):
        n = int(input("Introduce la altura del triángulo (entero positivo): "))
        for i in range(1, n + 1, 2):
            for j in range(i, 0, -2):
                print(j, end=" ")
            print("")

    def Whiciclo(self):
        n1=int(input("Ingresar numero"))
        i=1
        while i<=n:
            print(i)
            i=i+1

    def Anidadofor(self):
        n = int(input("Introduce el número de renglones: "))
        for i in range(n + 1):
            print('*' * i)
        for i in range(n + 1):
            blancos = n - i
            print(" " * blancos + "*" * i)
        for i in range(n + 1):
            blancos = n - i
            print(' ' * blancos + '* ' * i)  # Espacio lado derecho

    def Ciarray(self):
        n = int(input(u"Ingrese el tamaño del arreglo"))
        m = int(input(u"Ingrese el número de múltiplos"))
        A = []
        for i in range(0, n):
            A.append(i * m)
        print(A)

objdeber = Deber()
objdeber.Oparitmeticos()
objdeber.Relacionales()
objdeber.Aritmeticos()
objdeber.Secuencial()
objdeber.Selectiva()
objdeber.Compuesta()
objdeber.Forciclo()
objdeber.Whiciclo()
objdeber.Anidadofor()
objdeber.Ciarray()
