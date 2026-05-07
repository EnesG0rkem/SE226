import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

try:
    db_conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="#EnesG0rkem#",
        database="StudentDatabase"
    )
    cursor = db_conn.cursor()
except mysql.connector.Error as err:
    print("Bağlantı hatası:")
    exit()

def add_student():
    name = entry_name.get()
    try:
        score = int(entry_score.get())
        cursor.execute("INSERT INTO Students (name, score) VALUES (%s, %s)", (name, score))
        db_conn.commit()
        messagebox.showinfo("Başarılı", "Öğrenci eklendi!")
        display_students()
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir skor girin.")

def display_students():
    try:
        filter_val = int(entry_filter.get()) if entry_filter.get() else 0
    except ValueError:
        filter_val = 0

    for i in tree.get_children():
        tree.delete(i)
    
    query = "SELECT * FROM Students WHERE score > %s"
    cursor.execute(query, (filter_val,))
    
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)

root = tk.Tk()
root.title("SE 226 - Lab 8")

tk.Label(root, text="İsim:").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Skor:").grid(row=1, column=0, padx=5, pady=5)
entry_score = tk.Entry(root)
entry_score.grid(row=1, column=1)

tk.Button(root, text="Öğrenci Ekle", command=add_student).grid(row=2, column=0, columnspan=2, pady=10)

tk.Label(root, text="Minimum Skor Filtresi:").grid(row=3, column=0, padx=5, pady=5)
entry_filter = tk.Entry(root)
entry_filter.grid(row=3, column=1)
tk.Button(root, text="Filtrele", command=display_students).grid(row=4, column=0, columnspan=2, pady=5)

tree = ttk.Treeview(root, columns=("ID", "Name", "Score"), show='headings')
tree.heading("ID", text="ID")
tree.heading("Name", text="Öğrenci Adı")
tree.heading("Score", text="Skor")
tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

display_students()

root.mainloop()

if db_conn.is_connected():
    cursor.close()
    db_conn.close()