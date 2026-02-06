# importamos librerias para opmizar el fincionamiento del programa
from prettytable import PrettyTable
import uuid

# base de datos en memoria
libros = []
socios = []


# creamos una funcion para mostrar un menú
def mostrar_menu():
    print("\n MINIBIBLIOTECA")
    print("1. Resgistrar Libro")
    print("2. Registrar un Socio")
    print("3. Prestar un Libro")
    print("4. Devolver Libro ")
    print("5. Ver Libro prestado")
    print("6. Ver todos los libros ")
    print("7. Ver Todos los Socios")
    print("0. Salir")


def registrar_libro():

    print("=================================")
    print("Registrar libros📖")
    print("=================================")

    print("Digite 0 si desea cancelar la creación")

    titulo = input("Titulo del libro: ").strip().lower()

    if titulo == "0":
        return

    if not titulo:
        print(":❌El titulo no puede estar vacio❌")
        return

    autor = input("Autor del libro: ").strip().lower()

    if autor == "0":
        return

    if not autor:
        print("❌El Autor del libro no puede estar vacio❌")
        return
    isbn = input("ISBN del libro: ").strip().lower()
    if isbn == "0":
        return

    if not isbn:
        print("❌El ISBN no puede estar vacio❌")
        return

    # con un ciclo for verificarmos que el isbn no se repita
    for l in libros:
        if l["isbn"] == isbn:
            print(f"❌El ISBN {isbn} ya ha sido registrado con otro libro❌")

    # crear un nuevo libro
    nuevo_libro = {
        "isbn": isbn,
        "titulo": titulo,
        "autor": autor,
        "estado": "Disponible",
        "socio_prestado": None,
    }

    libros.append(nuevo_libro)
    print("✅ Libro fue Registrado Exitosamente")
    print(f"📚 {titulo} - {autor}")
    print(f"ISBN: {isbn}")

    print("=================================")


# creamos las variables para registrar a nuestros socios
def registrar_socio():
    print("=================================")
    print("\n registro para socios nuevos")
    print("=================================")

    print("Digite 0 para cancelar la acción")

    nombre = input("Escriba el nombre del socio: ").strip().lower()
    if nombre == "0":
        return

    if not nombre:
        print("❌El nombre del usuario no debe estar vacio❌")

    apellido = input("Ingrese el apellido del usuario: ")
    if apellido == "0":
        return

    if not apellido:
        print("❌El apellido del usuario no debe estar vacio❌")

    email = input("Ingrese el email del socio: ")
    if email == "0":
        return
    if not email:
        print("❌El email del usuario no puede estar vacio ❌")

    # usamos uuid4() que es una funcion del modulo uuid
    id_usuario = str(uuid.uuid4())

    # creamos un diccionario para guardar nuestros datos en una lista
    usuario = {
        "id": id_usuario,
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "libros_prestados": [],
    }

    # agregamos nuestro diccionario a nuestra lista de socios
    socios.append(usuario)
    print("✅El socio fue registrado de forma corredcta")
    print(f" 👨‍💼{nombre} {apellido}")
    print(f"📧{email}")
    print(f"🆔 ID: {id_usuario}")


def prestar_libro():
    pass


def devolver_libro():
    pass


def ver_libro_prestado():
    pass


def ver_todos_libros():
    """'
    print("==================================================")
    print("📖Mostrando todos los libros📖")
    print("==================================================")

    if not libros:
        print("No hay libros registrados")
        return

    # creamos un ciclo for donde los interadores cumplan la funcion de clave y valor

    for i, libro in enumerate(libros, 1):
        print("===============================================")
        print(f"{i}.  Nombre del libro: {libro["titulo"]}")
        print(f"      Autor del libro: {libro["autor"]}")
        print(f"      ISBN del libro: {libro["isbn"]}")
        print(f"      Estado del libro: {libro["estado"]}")
        print("================================================")
    """
    table = PrettyTable()

    table.field_names = ["titulo", "autor", "isbn", "estado"]

    table.title = "📖Mostrando todos los libros📖"

    for i, libro in enumerate(libros, 1):
        table.add_row([libro["titulo"], libro["autor"], libro["isbn"], libro["estado"]])

    print(table)


def ver_todos_socios():

    if not socios:
        print("❌ No hay socios registrados ❌")
        return

    # creamos un ciclo for para recorrer nuestra lista y mostrar los socios
    table = PrettyTable()

    table.field_names = ["id", "nombre", "apellido", "email", "libros_prestados"]

    table.title = "🧍Mostrando todos los socios🧍"

    for s, socio in enumerate(socios):
        libros_prestados = len(socio["libros_prestados"])
        table.add_row(
            [
                socio["id"],
                socio["nombre"],
                socio["apellido"],
                socio["email"],
                libros_prestados,
            ]
        )

        print(table)
    """print("================================================================")
    print("Mostrando todos los socios")
    print("================================================================")

    if not socios:
        print("No hay socios registrados en la biblioteca")
        return
    
    for i, socio in enumerate(socios, 1):
        print("================================================================")
        print(f"{i}. ID: {socio["id"]}")
        print(f"     Nombre: {socio["nombre"]} {socio["apellido"]}")
        print(f"     Email: {socio["email"]}")
        print(f"     Libros Prestados: {len(socio["libros_prestados"])}")
        print("================================================================")
    """


def main():

    while True:
        mostrar_menu()

        opcion = input("seleccione una opcion (0-7): ").strip()

        match opcion:
            case "1":
                registrar_libro()
            case "2":
                registrar_socio()
            case "3":
                prestar_libro()
            case "4":
                devolver_libro()
            case "5":
                ver_libro_prestado()
            case "6":
                ver_todos_libros()
            case "7":
                ver_todos_socios()

            case "0":
                print("📚Gracias por usar mi MINIBIBLIOTECA!📚")
                print("📚Hasta Luego📚")
                break


main()
