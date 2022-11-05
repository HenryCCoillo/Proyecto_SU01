from ast import While
from os import path
import os
import pandas as pd
from csv import DictWriter

class Libro:
    def __init__(self,id:int = None ,titulo:str = None,genero:str= None,isbn= None,editorial= None,autor= None) -> None:
        self.__id = id
        self.__titulo = titulo
        self.__genero = genero
        self.__isbn = isbn
        self.__editorial = editorial
        self.__autor = autor

    def __del__(self):
        return None

    def leer_archivo(self):
        libro = input("Escriba el archivo a leer: ")
        if libro:
            if path.exists(libro):
                if os.path.splitext(libro)[1] == '.txt':
                    with open(libro,encoding="utf-8") as data:
                        print(data.read())
                elif os.path.splitext(libro)[1] == '.csv':
                    with open(libro,encoding="utf-8") as data:
                        data = pd.read_csv(libro,index_col="id",encoding='utf-8')
                        print(data)
                else:
                    print("Solo se puede leer Archivos .txt o .csv")                        
            else:
                print("El archivo no existe")
        else:
            print("El Input esta Vacio")

    def listar_libros(self):
        data=pd.read_csv("Libros.csv",index_col="id",encoding='utf-8')
        return data
        
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

        data = self.listar_libros()
        print(data)

        id_filas = [id_fila for id_fila,fila in data.iterrows()]
        
        eliminar_fila_libro = int(input("Escriba el ID del Libro a Eliminar: "))

        while eliminar_fila_libro not in id_filas:
            eliminar_fila_libro = int(input("El ID no existe, Escriba el ID a Eliminar: "))

        data = data.drop(eliminar_fila_libro) 
        data.to_csv('Libros.csv')

    def buscar_libro_isbn_titulo(self):
        data = self.listar_libros()
        print(data)
        buscar = input("""Buscar libro por: ISBN o Título: """).lower()
        if buscar == "isbn":
            lista_isbn = list(set(data["isbn"]))
            buscar_isbn = input("Escriba el ISBN a buscar: ")
            while buscar_isbn not in lista_isbn:
                buscar_isbn = input("El ISBN no se encuentra, Escriba otro ISBN a buscar: ")

            isbn = data[data["isbn"] == buscar_isbn]
            print(isbn)
            
        elif buscar == "titulo" or buscar == "título":
            lista_titulo = list(set(data["titulo"]))
            buscar_titulo = input("Escriba el Título a buscar: ")
            while buscar_titulo not in lista_titulo:
                buscar_titulo = input("El Título no se encuentra, Escriba otro Título a buscar: ")

            titulo = data[data["titulo"] == buscar_titulo]
            print(titulo)
        else:
            print("No existe esa Categoria")

    def ordenar_libro(self):
        data=pd.read_csv('Libros.csv',index_col="id",encoding='utf-8')
        data = data.sort_values(by=['titulo'], ascending=[True])        
        print(data)

    def bucar_libro_autor_editorial_genero(self):
        data = self.listar_libros()
        print(data)
        buscar = input("""Buscar libro por: autor, editorial o género: """).lower()
        if buscar == "autor":
            lista_autor = list(set(data["autor"]))
            
            buscar_autor = input("Escriba el autor a buscar: ")
            while buscar_autor not in lista_autor:
                buscar_autor = input("El autor no se encuentra, Escriba otro autor a buscar: ")

            # data[data["autor"].str.contains("Ciro Alegría")]
            autor = data[data["autor"] == buscar_autor]
            print(autor)

        elif buscar == "editorial":
            lista_editorial = list(set(data["editorial"]))
            buscar_editorial = input("Escriba la editorial a buscar: ")
            while buscar_editorial not in lista_editorial:
                buscar_editorial = input("La editorial no se encuentra, Escriba otra editorial a buscar: ")
            editorial = data[data["editorial"] == buscar_editorial]
            print(editorial)

        elif buscar == "género" or buscar == "genero":
            lista_genero = list(set(data["genero"]))
            buscar_genero = input("Escriba el genero a buscar: ")
            while buscar_genero not in lista_genero:
                buscar_genero = input("El genero no se encuentra, Escriba otra genero a buscar: ")
            genero = data[data["genero"] == buscar_genero]
            print(genero)

        else:
            print("No existe esa categoria")


    def editar_libro_titulo_genero_isbn_editorial_autor(self):
            
            data = self.listar_libros()
            print(data)
            
            id_filas = [id_fila for id_fila,fila in data.iterrows()]
    
            editar_libro_id = int(input("Escribe el ID del Libro a editar: "))

            while editar_libro_id not in id_filas:
                editar_libro_id = int(input("El ID no existe, Escriba el ID a Eliminar: "))

            print(data.iloc[editar_libro_id-1:editar_libro_id])

            print("¿Que campo desea cambiar?")
            print("1) Título")
            print("2) Género")
            print("3) ISBN")
            print("4) Editorial")
            print("5) Autor")

            editar_libro_columna = int(input("Digite un numero: "))

            while editar_libro_columna not in (1,2,3,4,5):
                editar_libro_columna = int(input("Numero Incorrecto, solo puede digitar 1, 2, 3, 4 o 5: "))

            if editar_libro_columna == 1:
                editar_libro_columna = "titulo"

            elif editar_libro_columna == 2:
                editar_libro_columna = "genero"

            elif editar_libro_columna == 3:
                editar_libro_columna = "isbn"

            elif editar_libro_columna == 4:
                editar_libro_columna = "editorial"
            else:
                editar_libro_columna = "autor"

            editar_libro_valor = input("Escribe la valor a reemplazar: ").title()

            data.loc[editar_libro_id,editar_libro_columna] = editar_libro_valor

            # print(data.iloc[editar_libro_id-1:editar_libro_id])
            print(data)
            
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
                data = libro.listar_libros()
                print(data)

            elif opcion ==3:
                libro.agregar_libros()

            elif opcion ==4:
                libro.eliminar_libro()

            elif opcion ==5:
                libro.buscar_libro_isbn_titulo()

            elif opcion ==6:
                libro.ordenar_libro()

            elif opcion ==7:
                libro.bucar_libro_autor_editorial_genero()

            elif opcion ==8:
                pass
            elif opcion ==9:
                libro.editar_libro_titulo_genero_isbn_editorial_autor()
                # data = libro.listar_libros()
                # print(data)
                
                # id_filas = [id_fila for id_fila,fila in data.iterrows()]
        
                # editar_libro_id = int(input("Escribe el ID del Libro a editar: "))

                
                # while editar_libro_id not in id_filas:
                #     editar_libro_id = int(input("El ID no existe, Escriba el ID a Eliminar: "))

                # print(data.iloc[editar_libro_id-1:editar_libro_id])

                # editar_libro_columna = input("Escribe la columna a cambir titulo, genero, ISBN, editorial o autor: ")

                # editar_libro_valor = input("Escribe la palabra a reemplazar: ")

                # data.loc[editar_libro_id,editar_libro_columna] = editar_libro_valor

                # print(data.iloc[editar_libro_id-1:editar_libro_id])
                
                # data.to_csv('Libros.csv')


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

libro = Libro()
libro.leer_archivo()