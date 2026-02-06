# Documentación del Proyecto Biblioteca (Versión POO)

Este documento detalla el funcionamiento y la estructura del sistema de gestión de biblioteca, el cual ha sido actualizado para seguir el paradigma de Programación Orientada a Objetos (POO).

## Cambios Realizados y Funcionalidades

Se ha reestructurado el código para encapsular la lógica en clases, mejorando la organización y mantenibilidad.

### Estructura de Clases

1.  **Clase `Libro`**:
    *   Representa la entidad libro.
    *   Gestiona su propio estado (`Disponible` o `Prestado`) mediante los métodos `prestado()` y `devolver()`.

2.  **Clase `Socio`**:
    *   Representa a los usuarios de la biblioteca.
    *   Almacena información personal y una lista de los libros que tiene actualmente en préstamo.

3.  **Clase `Biblioteca`**:
    *   Controlador principal del sistema.
    *   Mantiene las listas de objetos `Libro` y `Socio`.
    *   Contiene la lógica para registrar, consultar, prestar y devolver ítems.

### Documentación de Código

Se han agregado **docstrings** a todos los métodos del archivo `biblioteca_2.py` para describir claramente su propósito:

*   **Registro**: Métodos `registrar_libro` y `registrar_socio` para la entrada de datos.
*   **Consultas**: Métodos `ver_todos_libros`, `ver_libro_prestado` y `ver_todo_socios` que utilizan `PrettyTable` para una visualización clara.
*   **Operaciones**: Métodos `prestar_libro` y `devolver_libro` que manejan la lógica de negocio de la biblioteca.
*   **Interfaz**: Método `menu` que sirve como punto de entrada para la interacción con el usuario.

## Requisitos

*   Python 3.x
*   Librería `prettytable`
    ```bash
    pip install prettytable
    ```