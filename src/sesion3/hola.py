# Para ejecutar este programa escrbir la terminacion
#python hola.py Isil

#Importamos los modulos que necesitamos usar.
#sys es uno muy estandar.
import sys

#Juntamos todo nuestro codigo en la funcion principal
def principal():
    #Los argumentos escritos em la linea de comandos
    # sys.argv[1], sys.argv[2] ...
    print('Hola', sys.argv[1])
    #sys.argv[0] es el nombre del script que estamos usando
    print('Soy el modulo', sys.argv[0])

#Para llamar a nuestra funcion principal para iniciar el
#programa usamos lo siguiente.
if __name__ == '__main__':
    principal()