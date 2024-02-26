import pyodbc
from pyodbc import Error
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk 

# Conectar ao banco de dados
def conexao():
    global conn
    conn = None
    try:
        conn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=RIKELMENOTE;'
        'DATABASE=Caixa;'
        'UID=sa;'
        'PWD=R1kelme@@07;'
    )
    except Error as er:
         print(er)
    return conn

vcon = conexao()
    
def query(conn, sql):
    try:
        cursor = conn.cursor()
        conn.execute(sql)
        cursor.commit()
    except:
        print(Exception)

def consultar(conn, sql):
        cursor = conn.cursor()
        cursor.execute(sql)
        res = cursor.fetchall()
        return res

main= Tk()
main.resizable(False, False)
main.title("Projeto Caixa")
main.geometry("900x700")
main.configure(background="#17c9ff")
icone = "C:/Users/rikel/OneDrive/Documentos/MeusProjetos/Caixa-com-python/icon.ico"
main.iconbitmap(icone)


main.mainloop()