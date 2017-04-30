##Problema: Realice una función en python que calcule y retorne cuantos kilómetros puede recorrer(distancia) con n galones de gasolina (el valor de n es pedido al usuario) y con un rendimiento de k kilómetros por galón (el valor de k es pedido al usuario).

##Entradas: N , K (enteros)

##Salidas: Imprimir cuantos kilómetros puede recorrer el jeep.

##restricciones: no se pueden ingresar numeros negativos, ni un maximo de 13 galones en un jeep

def jeep(kilometros,galones):
    if (galones==1):
        distancia=1*kilometros
        print('la distancia que recorrera es: ',distancia)
    elif (galones>=6 | galones<=13):
        distancia= (1*kilometros+1/3*kilometros+1/5*kilometros)
        print('La distancia que recorrera es: ',distancia)
    elif (galones>=13):
        print('Los galones exceden la capacidad del jeep')
    elif (galones<=0):
        print('No se puede andar debiendo gasolina')
    elif (galones>=2 ):
        distancia=(1*kilometros)+(1/3*kilometros)
        print('la distancia que recorrera es: ',distancia)
    return
a=jeep (int(input('Ingrese el rendimiento de kilómetros por galón:  ')),int(input('ingrese los galones de gasolina: ')))

print("Hola: ", a, abc)