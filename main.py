from ClsAlmacenamiento import ClsAlmacenamiento

def mostrar_menu():
    print("\nGestión de Tareas")
    print("1. Agregar Tarea")
    print("2. Listar Tareas")
    print("3. Eliminar Tarea")
    print("4. Salir")

def main():
    objAlmacenamiento = ClsAlmacenamiento()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            titulo = input("Ingrese el título de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            objAlmacenamiento.agregar_tarea(titulo, descripcion)
        elif opcion == '2':
            tareas = objAlmacenamiento.listar_tareas()
            for tarea in tareas:
                print(f"ID: {tarea[0]}, Título: {tarea[1]}, Descripción: {tarea[2]}, Fecha: {tarea[3]}")
        elif opcion == '3':
            tarea_id = int(input("Ingrese el ID de la tarea a eliminar: "))
            objAlmacenamiento.eliminar_tarea(tarea_id)
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
