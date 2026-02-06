from prettytable import PrettyTable


class Libro:
    def __init__(self, isbn, titulo, autor):
        """Inicializa un nuevo libro con ISBN, título y autor."""
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.estado = "Disponible"
        self.socio_prestado = None

    def prestado(self, id_socio):
        """Marca el libro como prestado a un socio si está disponible."""
        if self.estado == "Disponible":
            self.estado = "Prestado"
            self.socio_prestado = id_socio
            return True
        return False

    def devolver(self):
        """Restablece el estado del libro a Disponible y elimina la asignación del socio."""
        self.estado = "Disponible"
        self.socio_prestado = None


class Socio:
    def __init__(self, id_, nombre, apellido, email):
        """Inicializa un nuevo socio con ID, nombre, apellido y email."""
        self.id = id_
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.libros_prestados = []


class Biblioteca:
    def __init__(self):
        """Inicializa la biblioteca con listas vacías para libros y socios."""
        self.libros = []  #  lista de libros (objetos)
        self.socios = []  # lista de socios (objetos)
        self.contador_socios = 1
        self.menu()

    def registrar_libro(self):
        """Solicita datos al usuario para registrar un nuevo libro, validando que el ISBN no exista."""

        print("================================================================")
        print("📖 Registrar Libros 📖")
        print("================================================================")
        print("Digite 0 si quiere cancelar la creacion")

        titulo = input("Título del libro: ").strip().lower()

        if titulo == "0":
            return

        if not titulo:
            print("❌ El Título no puede estar vacío ❌")
            return

        autor = input("Autor del Libro: ").strip().lower()

        if autor == "0":
            return

        if not autor:
            print("❌ El Autor no puede estar vacío ❌")
            return

        isbn = input("ISBN del Libro: ").strip().lower()

        if isbn == "0":
            return

        if not isbn:
            print("❌ El ISBN no puede estar vacío ❌")
            return

        # el diccionario se devolvera un objeto y debemos instanciarlo como tal el iterador seeguido de un punto y el objeto a instanciar (iterador. objeto )(i.libro)
        for libro in self.libros:
            if libro.isbn == isbn:
                print(f"❌ Ya existe un libro con el ISBN {isbn} ❌")

        # crear el nuevo libro objeto

        self.libros.append(Libro(isbn, titulo, autor))
        print("✅ Libro Registrado Exitosamente 📖")
        print(f"📚 {titulo} - {autor}")
        print(f"ISBN: {isbn}")

        print("================================================================")

    def ver_todos_libros(self):
        """Muestra una tabla con todos los libros registrados y su estado actual."""

        table = PrettyTable()

        table.field_names = ["titulo", "autor", "isbn", "estado"]

        table.title = "📖 Mostrando Libros 📖"

        # la lista se devolvera un objeto y debemos instanciarlo como tal el iterador seeguido de un punto y el objeto a instanciar (iterador. objeto )(i.libro)
        for libro in self.libros:
            table.add_row([libro.titulo, libro.autor, libro.isbn, libro.estado])

        print(table)

    def ver_libro_prestado(self):
        """Muestra una tabla filtrada solo con los libros que se encuentran prestados."""

        table = PrettyTable()

        table.field_names = ["titulo", "autor", "isbn", "id_socio"]

        table.title = "📖 Mostrando Libros Prestados 📖"

        for libro in self.libros:
            if libro.estado == "Prestado":
                table.add_row(
                    [libro.titulo, libro.autor, libro.isbn, libro.socio_prestado]
                )
                table.add_divider()

        print(table)

    def ver_todo_socios(self):
        """Muestra una tabla con todos los socios registrados y la cantidad de libros que tienen prestados."""
        table = PrettyTable()
        # tarea opcion que muestre libros prestados
        table.field_names = ["ID", "Nombre", "Apellido", "Email", "Libros Prestados"]

        table.title = "👤 Mostrando Socios 👤"

        for socio in self.socios:
            libros_prestados = len(socio.libros_prestados)
            table.add_row(
                [
                    socio.id,
                    socio.nombre,
                    socio.apellido,
                    socio.email,
                    libros_prestados,
                ]
            )
            table.add_divider()

        if not self.socios:
            print("================================================================")
            print("No hay socios registrados en la biblioteca")
            print("================================================================")
            return

        print(table)

    def registrar_socio(self):
        """Solicita datos al usuario para registrar un nuevo socio, generando un ID secuencial."""

        print("================================================================")
        print("Registrar Socio 👤")
        print("================================================================")
        print("Digite 0 si quiere cancelar la creacion")

        nombre = input("Nombre del socio: ").strip().lower()

        if nombre == "0":
            return

        if not nombre:
            print("❌ El nombre no puede estar vacío ❌")
            return

        apellido = input("Apellido del socio: ").strip().lower()

        if apellido == "0":
            return

        if not apellido:
            print("❌ El apellido no puede estar vacío ❌")
            return

        email = input("Email del socio: ").strip().lower()

        if email == "0":
            return

        if not email:
            print("❌ El email no puede estar vacío ❌")
            return

        id_ = 1

        # Verificar si ya existe un socio con ese email
        for socio in self.socios:
            if socio.email == email:
                print(f"❌ Ya existe un socio con el email {email} ❌")
                return
        for socio in self.socios:
            id_ += self.contador_socios

        self.socios.append(Socio(id_, nombre, apellido, email))
        print("✅ Se registro un nuevo socio")
        print(f"🧑‍💼 El socio {nombre} {apellido} se registro con el email {email}")
        print(f" 🆔Tiene el id {id_}")

    def prestar_libro(self):
        """Gestiona el préstamo de un libro a un socio, validando disponibilidad y existencia de ambos."""

        print("📖Prestamo de libros📖")
        #  pedimos el isbn del libro para prestarlo aun socio
        isbn = input("ISBN del libro a prestar: ").strip()

        if not isbn:
            print("❌El ISBN no puede estar vacio❌")
            return isbn

        # creamos una variable temporal para saber si el libro fue encontrado
        libro_encontrado = None

        # recorremos nuestra lista de libros para verificar si tenemos el libro
        for libro in self.libros:
            if libro.isbn == isbn:
                libro_encontrado = libro
                break

        if libro_encontrado.estado != "Disponible":
            print("Actualmente el libro solicitado no está disponible")
            return

        # pedimos el ID del socio
        id_socio = int(input("ID del socio: "))

        if not id_socio:
            print("❌ El ID del socio no puede estar vacio❌")
            return id_socio

        # creamos una variable temporal para ver si el socio ha sido registrado
        id_socio_econtrado = None

        print(id_socio)
        for socio in self.socios:
            if socio.id == id_socio:
                id_socio_econtrado = socio
                break

        if not id_socio_econtrado:
            print(f"⚠️ No se encontro un usuario con el id {id_socio}⚠️")
            return id_socio_econtrado

        libro_encontrado.estado = "Prestado"
        libro_encontrado.socio_prestado = id_socio
        # agregamos el isbn del libro al socio
        id_socio_econtrado.libros_prestados.append(isbn)

        print("================================================================")
        print("Libro prestado con exito")
        print({libro_encontrado.titulo})
        print(f"Prestado a: {id_socio_econtrado.nombre}")
        print("================================================================")

    def devolver_libro(self):  # aplicar cambios
        """Gestiona la devolución de un libro, actualizando su estado y el registro del socio."""
        isbn = input("ISBN del libro a devolver: ").strip()

        if not isbn:
            print("❌El ISBN no puede estar vacio❌")
            return

        # creamos una variable temporal para saber si el libro fue encontrado
        libro_encontrado = None

        # recorremos nuestra lista de libros para verificar si tenemos el libro
        for libro in self.libros:
            if libro.isbn == isbn:
                libro_encontrado = libro
                break

        if not libro_encontrado:
            print(f"⚠️ No se econtro un libro con el ISBN {isbn} ⚠️")
            return
        print(f"El libro {libro_encontrado.titulo}, ha sido devuelto exitosamente")

        # buscamos el ID del socio que se ha prestado el libro
        id_socio = libro_encontrado.socio_prestado

        # buscamos al socio y removemos el registro del libro por medio del isbn
        for socio in self.socios:
            if socio.id == id_socio:
                if isbn in socio.libros_prestados:
                    socio.libros_prestados.remove(isbn)
                break

        libro_encontrado.estado = "Disponible"
        libro_encontrado.socio_prestado = None

    def menu(self):
        """Muestra el menú principal de la aplicación y gestiona la navegación del usuario."""

        while True:
            print(" MINIBIBLIOTECA ")
            print("1. Regristar Libro")
            print("2. Registrar un Socio")
            print("3. Prestar Libro")
            print("4. Devolver Libro")
            print("5. Ver libros Pestados")
            print("6. Ver todos los Libros")
            print("7. Ver todos los Socios")
            print("0. Salir")

            opcion = input("Seleccion una opción(0-7): ").strip()

            match opcion:
                case "1":
                    self.registrar_libro()
                case "2":
                    self.registrar_socio()
                case "3":
                    self.prestar_libro()
                case "4":
                    self.devolver_libro()
                case "5":
                    self.ver_libro_prestado()  # en proceso
                case "6":
                    self.ver_todos_libros()
                case "7":
                    self.ver_todo_socios()
                case "0":
                    print("📚 Gracias por usar MiniBiblio! 📚")
                    print("📚 Hasta Luego 📚")
                    break
                case _:
                    print("Opcion no válida. Por favor, selecion una opción del 0 al 7")


# instaciamos nuestra clase biblioteca2
biblioteca1 = Biblioteca()
"""biblioteca1.registrar_libro()
biblioteca1.registrar_socio()
"""
