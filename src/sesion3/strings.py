
def principal():
    lenguaje = "python"
    frase = "Hola %s, eres %s y %s" % (lenguaje, "cool", "facil")
    print(frase)
    frase = "Hola {0}, eres {2} y {1}".format(lenguaje, "cool", "facil")
    print(frase)

    print("Python es" + " genial" + " genial" + " genial" + " genial" + " genial")
    print("Python es" + " genial" * 5)
    print(len(frase))
    print(frase.upper())
    print(frase.lower())
    print(frase.capitalize())

    print(frase[0])
    print(frase[-1])
    print(frase[29])
    print(frase[0:4])
    print(frase[4])
    print(frase[5:])


if __name__ == '__main__':
    principal()