from ast import While
from os import path
import json

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
                with open(libro,encoding="utf-8") as archivo:
                    print(archivo.read())
            else:
                print("El archivo no existe")
        else:
            print("Escriba el archivo")


    def listar_libros(self):
        with open("prueba.json",encoding="utf-8") as archivo:
            datos_libros = json.load(archivo)

            for i in datos_libros:
                diccionario_libro = datos_libros[i]
                nombre_libro_id =diccionario_libro["id"]
                nombre_libro_titulo = diccionario_libro["titulo"]
                nombre_libro_genero =diccionario_libro["genero"] 
                nombre_libro_isbn =diccionario_libro["isbn"] 
                nombre_libro_editorial =diccionario_libro["editorial"] 
                nombre_libro_autor =diccionario_libro["autor"] 
                print(f"\n-El Libro llamano {nombre_libro_titulo}, su genero es {nombre_libro_genero}, su codigo de isbn es {nombre_libro_isbn}, la editorial es {nombre_libro_editorial} y el autor es {nombre_libro_autor}\n")






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
            opcion = int(input("Digite la Opcion: "))

            libro = Libro()
            if opcion == 1:
                libro.leer_archivo()
            elif opcion ==2:
                pass

            elif opcion ==3:
                pass

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

