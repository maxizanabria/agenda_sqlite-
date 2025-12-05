import tkinter as tk
from tkinter import messagebox
from database import Database


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda con SQLite")

        self.db = Database()

        # ---------------------------
        #       LISTBOX
        # ---------------------------
        self.lista = tk.Listbox(root, width=45, height=12)
        self.lista.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.cargar_lista()

        # ---------------------------
        #      CAMPOS DE TEXTO
        # ---------------------------
        tk.Label(root, text="Nombre:").grid(row=1, column=0, sticky="w")
        tk.Label(root, text="Teléfono:").grid(row=2, column=0, sticky="w")
        tk.Label(root, text="Email:").grid(row=3, column=0, sticky="w")

        self.e_nombre = tk.Entry(root, width=30)
        self.e_tel = tk.Entry(root, width=30)
        self.e_email = tk.Entry(root, width=30)

        self.e_nombre.grid(row=1, column=1, pady=2)
        self.e_tel.grid(row=2, column=1, pady=2)
        self.e_email.grid(row=3, column=1, pady=2)

        # ---------------------------
        #          BOTONES
        # ---------------------------
        tk.Button(root, text="Agregar", width=12, command=self.agregar).grid(row=4, column=0, pady=10)
        tk.Button(root, text="Editar", width=12, command=self.editar).grid(row=4, column=1)
        tk.Button(root, text="Eliminar", width=12, command=self.eliminar).grid(row=4, column=2)

    # =====================================================
    #                    FUNCIONES
    # =====================================================

    def cargar_lista(self):
        self.lista.delete(0, tk.END)

        self.contactos = self.db.obtener_todos()

        for c in self.contactos:
            contacto_id, nombre, tel, email = c
            self.lista.insert(tk.END, f"{nombre} | {tel} | {email}")

    def obtener_indice(self):
        sel = self.lista.curselection()
        if not sel:
            messagebox.showwarning("Atención", "Seleccioná un contacto.")
            return None
        return sel[0]

    # --------------------------- CRUD ---------------------------

    def agregar(self):
        nombre = self.e_nombre.get()
        tel = self.e_tel.get()
        email = self.e_email.get()

        if not nombre or not tel:
            messagebox.showwarning("Error", "Nombre y teléfono son obligatorios.")
            return

        self.db.agregar(nombre, tel, email)
        self.cargar_lista()
        self.limpiar()

    def editar(self):
        idx = self.obtener_indice()
        if idx is None:
            return

        contacto = self.contactos[idx]
        contacto_id = contacto[0]

        nombre = self.e_nombre.get()
        tel = self.e_tel.get()
        email = self.e_email.get()

        if not nombre or not tel:
            messagebox.showwarning("Error", "Nombre y teléfono no pueden quedar vacíos.")
            return

        self.db.editar(contacto_id, nombre, tel, email)
        self.cargar_lista()
        self.limpiar()

    def eliminar(self):
        idx = self.obtener_indice()
        if idx is None:
            return

        contacto = self.contactos[idx]
        contacto_id = contacto[0]

        self.db.eliminar(contacto_id)
        self.cargar_lista()
        self.limpiar()

    def limpiar(self):
        self.e_nombre.delete(0, tk.END)
        self.e_tel.delete(0, tk.END)
        self.e_email.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
