from ast import While
from os import path
import os
import pandas as pd
from csv import DictWriter

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
        if libro:
            if path.exists(libro):
                if os.path.splitext(libro)[1] == '.txt':
                    with open(libro,encoding="utf-8") as archivo:
                        print(archivo.read())
                elif os.path.splitext(libro)[1] == '.csv':
                    with open(libro,encoding="utf-8") as archivo:
                        archivo = pd.read_csv(libro)
                        # archivo = pd.read_csv(libro,index_col="id")
                        print(archivo)
                else:
                    print("Solo se puede leer Archivos .txt o .csv")                        
            else:
                print("El archivo no existe")
        else:
            print("Escriba el archivo")

    def listar_libros(self):
        data=pd.read_csv("Libros.csv")
        print(data)
        

    def agregar_libros(self):
        
        codigo=input("ingrese ID: ")
        titulo=input("Ingrese título: ")
        genero=input("Ingrese genero: ")
        isbn=input("Ingrese ISBN: ")
        editorial=input("Ingrese editorial: ")
        autor=input("Ingrese autor: ")
        
        headersCSV = ['id','titulo','genero','isbn','editorial','autor']      

        dict={'id':codigo,'titulo':titulo,'genero':genero,'isbn':isbn,'editorial':editorial,'autor':autor}
        with open('Libros.csv', 'a', newline='',encoding='utf-8-sig') as f_object:
            dictwriter_object = DictWriter(f_object, fieldnames=headersCSV)    
            dictwriter_object.writerow(dict)
            f_object.close()

    def eliminar_libro(self):
        data=pd.read_csv("Libros.csv")
        print(data)
        eliminar_fila_libro = int(input("Escriba el ID del Libro a Eliminar: "))
        id_filas = [id_fila for id_fila,fila in data.iterrows()]
        while eliminar_fila_libro not in id_filas:
            eliminar_fila_libro = int(input("El ID no existe, Escriba el ID a Eliminar: "))
        data.set_index('id',inplace=True) 
        data = data.drop(eliminar_fila_libro) 
        data.to_csv('Libros.csv')
        

if __name__ == '__main__':
    try:
        while True:
            print("""
Opción 1: Leer archivo de disco duro (.txt o csv) que cargue 3 libros.
Opción 2: Listar libros.
Opción 3: Agregar libro.
Opción 4: Eliminar libro.
Opción 5: Buscar libro por ISBN o por título. Se debe sugerir las opciones y listar el resultado.
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
                    break
                except ValueError:
                    print("Debes Escribir un numero Valido")

            libro = Libro()
            if opcion == 1:
                libro.leer_archivo()
            elif opcion ==2:
                libro.listar_libros()
            elif opcion ==3:
                libro.agregar_libros()
            elif opcion ==4:
                libro.eliminar_libro()
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
            else:
                print("La Opcion no existe")

    except KeyboardInterrupt:
        print("Saliendo...")
        exit()

