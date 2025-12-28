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
import sqlite3
from typing import List, Tuple, Optional


class Database:
    """SQLite database handler for contacts."""

    def __init__(self, db_name: str = "agenda.db") -> None:
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self._create_table()

    def _create_table(self) -> None:
        """Create contacts table if it does not exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT
            )
        """)
        self.connection.commit()

    # -------- CRUD --------

    def add_contact(self, name: str, phone: str, email: Optional[str]) -> None:
        self.cursor.execute(
            "INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)",
            (name, phone, email)
        )
        self.connection.commit()

    def get_all_contacts(self) -> List[Tuple[int, str, str, Optional[str]]]:
        self.cursor.execute(
            "SELECT id, name, phone, email FROM contacts"
        )
        return self.cursor.fetchall()

    def update_contact(
        self,
        contact_id: int,
        name: str,
        phone: str,
        email: Optional[str]
    ) -> None:
        self.cursor.execute(
            "UPDATE contacts SET name=?, phone=?, email=? WHERE id=?",
            (name, phone, email, contact_id)
        )
        self.connection.commit()

    def delete_contact(self, contact_id: int) -> None:
        self.cursor.execute(
            "DELETE FROM contacts WHERE id=?",
            (contact_id,)
        )
        self.connection.commit()

    def close(self) -> None:
        self.connection.close()
