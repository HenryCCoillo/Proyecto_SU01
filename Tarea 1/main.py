from ast import While
from os import path
import json
from csv import DictWriter
import csv
import pandas as pd

class Libro:
    def __init__(self,id:str = None ,titulo:str = None,genero:str= None,isbn= None,editorial= None,autor= None) -> None:
        self.__id = id
        self.__titulo = titulo
        self.__genero = genero
        self.__isbn = isbn
        self.__editorial = editorial
        self.__autor = autor

    def __del__(self):
        return None

    def leer_archivo(self):
        libro = input("Escriba el archivo : ")
        while libro not in ("Libros"):
            libro = input("Escriba el archivo nuevamente: ")
        if libro == "Libros":
            with open('D:\\BootCamp\\Proyecto_Silabuz\\Proyecto_SU01\\Tarea 1\\'+libro+'.csv',encoding='utf-8-sig') as f:
                archivo = csv.reader(f)
                datos =[]
                for i in archivo:
                    datos.append(i)
                print(datos)


    def listar_libros(self):
        data=pd.read_csv("D:\\BootCamp\\Proyecto_Silabuz\\Proyecto_SU01\\Tarea 1\\Libros.csv")
        data2=data[['titulo','genero','isbn','editorial','autor']]
        data3=data2.to_string(index=False)
        print(data3)
        
    
    def agregar_libros(self):
        
        codigo=input("ingrese ID: ")
        titulo=input("Ingrese título: ")
        genero=input("Ingrese genero: ")
        isbn=input("Ingrese ISBN: ")
        editorial=input("Ingrese editorial: ")
        autor=input("Ingrese autor: ")
        
        headersCSV = ['id','titulo','genero','isbn','editorial','autor']      

        dict={'id':codigo,'titulo':titulo,'genero':genero,'isbn':isbn,'editorial':editorial,'autor':autor}
        with open('D:\\BootCamp\\Proyecto_Silabuz\\Proyecto_SU01\\Tarea 1\\Libros.csv', 'a', newline='',encoding='utf-8-sig') as f_object:
    
            dictwriter_object = DictWriter(f_object, fieldnames=headersCSV)
    
            dictwriter_object.writerow(dict)
            
   
            f_object.close()



if __name__ == '__main__':
    try:
        while True:
            print("""
Opción 1: Leer archivo de disco duro (.txt o csv) que cargue 3 libros.
Opción 2: Listar libros.
Opción 3: Agregar libro.
Opción 4: Eliminar libro.
Opción 5: Buscar libro por título. Se debe sugerir las opciones y listar el resultado.
Opción 6: Ordenar libros por título.
Opción 7: Buscar libros por autor, editorial o género. Se deben sugerir las opciones y listar los resultados.
Opción 8: Buscar libros por número de autores. Se debe ingresar un número por ejemplo 2 (hace referencia a dos autores) y se deben listar todos los libros 
que contengan 2 autores.
Opción 9: Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores).
Opción 10: Guardar libros en archivo de disco duro (.txt o csv).
Opción 11: Salir del Programa.
            """)

            while True:
                try:
                    opcion = int(input("Digite la Opcion: "))
                except ValueError:
                    print("Debes Escribir un numero Valido")
                    continue
                
                if opcion:
                    break

            libro = Libro()
            if opcion == 1:
                libro.leer_archivo()
            elif opcion == 2:
                libro.listar_libros()

            elif opcion == 3:
                libro.agregar_libros()

            elif opcion ==4:
                pass

            elif opcion ==5:
                pass

            elif opcion ==6:
                pass

            elif opcion ==7:
                pass

            elif opcion ==8:
                pass
                

            elif opcion ==9:
                pass

            elif opcion ==10:
                pass

            elif opcion == 11:
                del libro
                break

    except KeyboardInterrupt:
        print("Saliendo...")
        exit()



