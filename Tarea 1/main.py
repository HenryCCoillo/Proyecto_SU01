from os import path
import os
import pandas as pd
from csv import DictWriter


class Libro:
    def __init__(self, id: int = None, titulo: str = None, genero: str = None, isbn=None, editorial=None,
                 autor=None) -> None:
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
                    with open(libro, encoding="utf-8") as data:
                        print(data.read())
                elif os.path.splitext(libro)[1] == '.csv':
                    with open(libro, encoding="utf-8") as data:
                        data = pd.read_csv(libro, index_col="id", encoding='utf-8')
                        print(data)
                else:
                    print("Solo se puede leer Archivos .txt o .csv")
            else:
                print("El archivo no existe")
        else:
            print("El Input esta Vacio")

    def listar_libros(self):
        data = pd.read_csv("Libros.csv", index_col="id", encoding='utf-8')
        return data

    def agregar_libros(self):

        codigo = input("ingrese ID: ")
        titulo = input("Ingrese título: ")
        genero = input("Ingrese genero: ")
        isbn = input("Ingrese ISBN: ")
        editorial = input("Ingrese editorial: ")
        autor = input("Ingrese autor: ")

        headersCSV = ['id', 'titulo', 'genero', 'isbn', 'editorial', 'autor']

        dict = {'id': codigo, 'titulo': titulo, 'genero': genero, 'isbn': isbn, 'editorial': editorial, 'autor': autor}
        with open('Libros.csv', 'a', newline='', encoding='utf-8-sig') as f_object:
            dictwriter_object = DictWriter(f_object, fieldnames=headersCSV)
            dictwriter_object.writerow(dict)
            f_object.close()

    def eliminar_libro(self):

        data = self.listar_libros()
        print(data)

        id_filas = [id_fila for id_fila, fila in data.iterrows()]  # Extrae todos los ID en un Array
        eliminar_fila_libro = int(input("Escriba el ID del Libro a Eliminar: "))
        while eliminar_fila_libro not in id_filas:
            eliminar_fila_libro = int(input("El ID no existe, Escriba el ID a Eliminar: "))

        data = data.drop(eliminar_fila_libro)  # Elimina la fila
        data.to_csv('Libros.csv')

    def buscar_libro_isbn_titulo(self):
        data = self.listar_libros()
        print(data)

        print("\n¿Qué categoría desea buscar?\n")
        print("1) ISBN")
        print("2) Título")

        buscar_isbn_titulo = int(input("\nDigite un número: "))
        while buscar_isbn_titulo not in (1, 2):
            buscar_isbn_titulo = int(input("Número Incorrecto, solo puede digitar 1 o 2: "))

        if buscar_isbn_titulo == 1:  # Busqueda por ISBN
            buscar_isbn = input("\nEscriba el ISBN a buscar: ")
            isbn = data[data["isbn"].str.contains(buscar_isbn)]
            print(isbn)


        else:  # Busqueda por Título
            buscar_titulo = input("\nEscriba el Título a buscar: ")
            titulo = data[data["titulo"].str.contains(buscar_titulo)]
            print(titulo)

    def ordenar_libro(self):
        data = pd.read_csv('Libros.csv', index_col="id", encoding='utf-8')
        data = data.sort_values(by=['titulo'], ascending=[True])
        print(data)

    def bucar_libro_autor_editorial_genero(self):
        data = self.listar_libros()
        print(data)

        print("\n¿Qué categoría desea buscar?\n")
        print("1) Autor")
        print("2) Editorial")
        print("3) Género")

        buscar_autor_editorial_genero = int(input("\nDigite un número: "))
        while buscar_autor_editorial_genero not in (1, 2, 3):
            buscar_autor_editorial_genero = int(input("Número Incorrecto, solo puede digitar 1, 2 o 3: "))

        if buscar_autor_editorial_genero == 1:  # Busqueda por Autor
            buscar_autor = input("\nEscriba el autor a buscar: ").title()
            autor = data[data["autor"].str.contains(buscar_autor)]
            print(autor)

        elif buscar_autor_editorial_genero == 2:  # Busqueda por Editorial
            buscar_editorial = input("\nEscriba la editorial a buscar: ").title()
            editorial = data[data["editorial"].str.contains(buscar_editorial)]
            print(editorial)


        else:  # Busqueda por Género
            buscar_genero = input("\nEscriba el genero a buscar: ").title()
            genero = data[data["genero"].str.contains(buscar_genero)]
            print(genero)

    def editar_libro_titulo_genero_isbn_editorial_autor(self):

        data = self.listar_libros()
        print(data)

        id_filas = [id_fila for id_fila, fila in data.iterrows()]  # Extrae todos los ID en un Array
        editar_libro_id = int(input("\nEscribe el ID del Libro a editar: "))
        while editar_libro_id not in id_filas:
            editar_libro_id = int(input("El ID no existe, Escriba el ID a Eliminar: "))

        print(data.iloc[editar_libro_id - 1:editar_libro_id])  # Imprime el ID a Editar

        print("\n¿Que campo desea cambiar?")
        print("1) Título")
        print("2) Género")
        print("3) ISBN")
        print("4) Editorial")
        print("5) Autor")

        editar_libro_columna = int(input("\nDigite un número: "))

        while editar_libro_columna not in (1, 2, 3, 4, 5):
            editar_libro_columna = int(input("Número Incorrecto, solo puede digitar 1, 2, 3, 4 o 5: "))

        if editar_libro_columna == 1:  # Edita por Columna Titulo
            editar_libro_columna = "titulo"

        elif editar_libro_columna == 2:  # Edita por Columna Genero
            editar_libro_columna = "genero"

        elif editar_libro_columna == 3:  # Edita por Columna ISBN
            editar_libro_columna = "isbn"

        elif editar_libro_columna == 4:  # Edita por Columna Editorial
            editar_libro_columna = "editorial"

        else:  # Edita por Columna Autor
            editar_libro_columna = "autor"

        editar_libro_valor = input("Escribe la valor a reemplazar: ").title()
        data.loc[editar_libro_id, editar_libro_columna] = editar_libro_valor
        print(data.iloc[editar_libro_id - 1:editar_libro_id])

        data.to_csv('Libros.csv')


if __name__ == '__main__':
    try:
        while True:
            print("\nPrograma de Archivos\n")
            print("1) Leer archivo de disco duro (.txt o csv) que cargue 3 libros.")
            print("2) Listar libros.")
            print("3) Agregar libro.")
            print("4) Eliminar libro.")
            print("5) Ordenar libros por título.")
            print("6) Buscar libro por ISBN o por título.")
            print("7) Buscar libros por autor, editorial o género.")
            print("8) Buscar libros por número de autores.")
            print("9) Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores).")
            print("10) Guardar libros en archivo de disco duro (.txt o csv).")
            print("11) Salir del Programa")

            while True:
                try:
                    opcion = int(input("\nDigite la Opcion: "))
                    break
                except ValueError:
                    print("Debes digitar un número valido")

            libro = Libro()

            if opcion == 1:
                libro.leer_archivo()

            elif opcion == 2:
                data = libro.listar_libros()
                print(data)

            elif opcion == 3:
                libro.agregar_libros()

            elif opcion == 4:
                libro.eliminar_libro()

            elif opcion == 5:
                libro.ordenar_libro()

            elif opcion == 6:
                libro.buscar_libro_isbn_titulo()

            elif opcion == 7:
                libro.bucar_libro_autor_editorial_genero()

            elif opcion == 8:
                pass

            elif opcion == 9:
                libro.editar_libro_titulo_genero_isbn_editorial_autor()

            elif opcion == 10:
                pass
            elif opcion == 11:
                del libro
                break
            else:
                print("La Opcion no existe")

    except KeyboardInterrupt:
        print("Saliendo...")

exit()