def principal():
  # NUMERO 1:
    numero = list(range(1,5,1))
    print(numero)
    suma=0
    for nume in numero:
        print(nume**2)
    for num in numero:
        suma=suma+(num**2)

    print("La suma de cuadrados es: ",  suma)
    # NUMERO 2:
    texto = "Juan Tuya Garcia"
    print(texto)
    contador=0
    for letra in texto:
        if(letra=='a'):
            contador+=1

    print(contador)
if __name__=='__main__':
    principal()