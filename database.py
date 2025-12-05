import sqlite3


class Database:
    def __init__(self, db_name="agenda.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS contactos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                telefono TEXT NOT NULL,
                email TEXT
            );
        """)
        self.conn.commit()

    # ---------------------------
    #            CRUD
    # ---------------------------

    def agregar(self, nombre, telefono, email):
        self.cursor.execute(
            "INSERT INTO contactos (nombre, telefono, email) VALUES (?, ?, ?)",
            (nombre, telefono, email)
        )
        self.conn.commit()

    def obtener_todos(self):
        self.cursor.execute("SELECT id, nombre, telefono, email FROM contactos")
        return self.cursor.fetchall()

    def editar(self, contacto_id, nombre, telefono, email):
        self.cursor.execute(
            "UPDATE contactos SET nombre=?, telefono=?, email=? WHERE id=?",
            (nombre, telefono, email, contacto_id)
        )
        self.conn.commit()

    def eliminar(self, contacto_id):
        self.cursor.execute("DELETE FROM contactos WHERE id=?", (contacto_id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
