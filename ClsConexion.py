import sqlite3

class ClsConexion:
    def __init__(self, db_name="dbtareas.db"):
        self.db_name = db_name
        self.conn = None

    def conectar(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            print(f"Conexión establecida con {self.db_name}")
        except sqlite3.Error as e:
            print(f"Error al conectar con la base de datos: {e}")
        return self.conn

    def crear_tabla(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS tareas (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                titulo TEXT NOT NULL,
                                descripcion TEXT NOT NULL,
                                fecha_creacion TEXT NOT NULL
                              )''')
            self.conn.commit()
            print("Tabla 'tareas' creada exitosamente.")
        except sqlite3.Error as e:
            print(f"Error al crear la tabla: {e}")
