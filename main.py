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

def teste():
     print("")

main= Tk()
main.resizable(False, False)
main.title("Projeto Caixa")
main.geometry("900x700")
main.configure(background="#17c9ff")
icone = "C:/Users/rikel/OneDrive/Documentos/MeusProjetos/Caixa-com-python/imagens/icon.ico"
main.iconbitmap(icone)

#######################################################################################

#barra de menu

barraDeMenus = Menu(main)
menuProduto = Menu(barraDeMenus, tearoff=0)
menuProduto.add_command(label="Adicionar Produto", command=teste)
menuProduto.add_command(label="Deletar Produto", command=teste)
barraDeMenus.add_cascade(label="Produtos", menu=menuProduto)

menuConsulta = Menu(barraDeMenus, tearoff=0)
menuConsulta.add_command(label="Por nome", command=teste)
menuConsulta.add_command(label="Por ID", command=teste)
barraDeMenus.add_cascade(label="Consulta", menu=menuConsulta)


menuSobre = Menu(barraDeMenus, tearoff=0)
menuSobre.add_command(label="Sobre nós", command=teste)
barraDeMenus.add_cascade(label="Sobre", menu=menuSobre)

menuFechar = Menu(barraDeMenus, tearoff=0)
menuFechar.add_command(label="Fechar", command=main.quit)
barraDeMenus.add_cascade(label="Fechar", menu=menuFechar)



main.config(menu = barraDeMenus)

#######################################################################################

#titulo da janela

titulo = Label(main, text="Caixa", background="#17c9ff", font=("Bahnschrift", 30))
titulo.place(x = -30, y = 0, width=900, height=100)

image = Image.open("C:/Users/rikel/OneDrive/Documentos/MeusProjetos/Caixa-com-python/imagens/carrinho.ico")
photo = ImageTk.PhotoImage(image)
img = Label(main, image=photo, background="#17c9ff")
img.place(x = 500, y = 0)


main.mainloop()