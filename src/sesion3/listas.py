def principal():
    mylista = [1, 12.4, "hola", "c++", True, [1, 2]]
    print(len(mylista))
    print(mylista[2])
    print(mylista)

    lista2 = mylista
    print(lista2)
    mylista[2] = "chau"
    print(mylista)
    print(lista2)

    hola = "hola mundo"
    lista_hola = list(hola)
    print(lista_hola)
    print(" ".join(lista_hola))

    #hola[2] = "g"
    secuencia = list(range(1, 51,7))
    print(secuencia)

    for num in secuencia:
          print(num ** 3)
    i = 0
    for num in secuencia:
        print(i, num ** 3)
    i = i + 1

    print(list(enumerate(secuencia))) 
    for i, num in enumerate(secuencia):
        print(i, num ** 3)
    
      

if __name__ == '__main__':
    principal()