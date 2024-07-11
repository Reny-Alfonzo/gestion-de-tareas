import sqlite3
from ClsConexion import ClsConexion
import datetime

class ClsAlmacenamiento:
    def __init__(self):
        self.conexion = ClsConexion()
        self.conn = self.conexion.conectar()
        self.conexion.crear_tabla()

    def agregar_tarea(self, titulo, descripcion):
        try:
            fecha_creacion = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor = self.conn.cursor()
            cursor.execute('''INSERT INTO tareas (titulo, descripcion, fecha_creacion) 
                              VALUES (?, ?, ?)''', (titulo, descripcion, fecha_creacion))
            self.conn.commit()
            print("Tarea agregada exitosamente.")
        except sqlite3.Error as e:
            print(f"Error al agregar la tarea: {e}")

    def listar_tareas(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM tareas')
            tareas = cursor.fetchall()
            return tareas
        except sqlite3.Error as e:
            print(f"Error al listar las tareas: {e}")
            return []

    def eliminar_tarea(self, tarea_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute('DELETE FROM tareas WHERE id = ?', (tarea_id,))
            self.conn.commit()
            print("Tarea eliminada exitosamente.")
        except sqlite3.Error as e:
            print(f"Error al eliminar la tarea: {e}")
