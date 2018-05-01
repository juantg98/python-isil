#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0


import sys
import re

"""
Baby Names
==========

Defina la funcion extract_names() de abajo y modique main()
para que la invoque.

Asi es como los archivos html lucen babyxxxx.html

...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Hitos sugeridos para el desarrollo incremental::
 -Extraer el año e imprimirlo.
 -Extraer los nombres y rangos(ranks) e imprimirlos.
 -Obtener los nombres dentro de diccionarios e imprimirlos.
 -Armar la lista [año, "nombre rango(rank)", ...]
 -Corregir main() para usar la lista que retorne la funcion extract_names.
"""


def extract_names(filename):
    """
    Dado un nombre de archivo, devuelve una lista que comienza con
    el año como cadena seguido de las cadenas de "nombres rango" en orden
    alfabético.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    names = []

 
    f = open(filename, 'rU')
    text = f.read()

    year_match = re.search(r'Popularity\sin\s(\d\d\d\d)', text)
    if not year_match:
  
        sys.stderr.write('Couldn\'t find the year!\r\n')
         sys.exit(1)
     year = year_match.group(1)
     names.append(year)

    tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', text)

      for rank_tuple in tuples:
        (rank, boyname, girlname) = rank_tuple 
         if boyname not in names_to_rank:
            names_to_rank[boyname] = rank
         if girlname not in names_to_rank:
            names_to_rank[girlname] = rank
    sorted_names = sorted(names_to_rank.keys())
    for name in sorted_names:
       names.append(name + " " + names_to_rank[name])      

     return names


def main():
    # Se pasa una serie de archivos omitimos el argumento argv[0]
    # el cual nos trae el nombre del archivo.
    args = sys.argv[1:]

    if not args:
        print 'usage: [--generaresumen] archivo [archivo ...]'
        sys.exit(1)

    # Observe que el flag generaresumen.
    summary = False
    if args[0] == '--generaresumen':
        summary = True
        del args[0]

    for filename in args:
       names = extract_names(filename)

       text = '\n'.join(names)

       if summary:
      outf = open(filename + '.resumen', 'w')
      outf.write(text + '\n')
      outf.close()

      else:
      print text

    
    # Por cada archivo pasado como parametro imprimir el resultado.
    # En caso se pase el flag generaresumen, guardar en un archivo
    # con el mismo nombre pero la extension .resumen

    # Ejemplo:
    # $ python babynames.py baby1990.html baby1992.html
    # $ python babynames.py --generaresumen baby1990.html baby1992.html

if __name__ == '__main__':
    main()
