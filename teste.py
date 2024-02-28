import pyodbc
import tkinter as tk
from tkinter import Label, Entry, Button, Menu, Toplevel
from PIL import Image, ImageTk 

conn = None

def conexao():
    global conn
    try:
        conn = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=RIKELMENOTE;'
            'DATABASE=Caixa;'
            'UID=sa;'
            'PWD=R1kelme@@07;'
        )
    except pyodbc.Error as er:
        print(er)
    return conn

def query(sql):
    global conn
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.commit()
    except Exception as e:
        print("Erro:", e)

def adicionarProd():
    janelaProd = Toplevel()
    janelaProd.resizable(False, False)
    janelaProd.title("Adicionar Produto")
    janelaProd.geometry("900x700")
    janelaProd.configure(background="#17c9ff")
    icone = "C:/Users/rikel/OneDrive/Documentos/MeusProjetos/Caixa-com-python/imagens/icon.ico"
    janelaProd.iconbitmap(icone)

    lblTitulo = Label(janelaProd, text="Adicionar produto", background="#17c9ff")
    lblTitulo.pack()

    lblCod = Label(janelaProd, text="Código do produto", background="#17c9ff")
    lblCod.pack()

    entradaCod = Entry(janelaProd)
    entradaCod.pack()

    lbl1 = Label(janelaProd, text="Nome do produto", background="#17c9ff")
    lbl1.pack()

    entradaNome = Entry(janelaProd)
    entradaNome.pack()

    lbl2 = Label(janelaProd, text="Valor do produto", background="#17c9ff")
    lbl2.pack()

    entradaValor = Entry(janelaProd)
    entradaValor.pack()

    lbl3 = Label(janelaProd, text="Quantidade do produto", background="#17c9ff")
    lbl3.pack()

    entradaQntd = Entry(janelaProd)
    entradaQntd.pack()

    def adiciona():
        entCod = entradaCod.get()
        entNome = entradaNome.get()
        entValor = entradaValor.get()
        entQntd = entradaQntd.get()
        vsql = "INSERT INTO Produtos (Cod_Prod, ValorUnit_Prod, Quantidade_Prod, Nome_Prod) VALUES ('{}', '{}', '{}', '{}')".format(entCod, entValor, entQntd, entNome)
        query(vsql)
        # Fechar a janela após adicionar o produto
        janelaProd.destroy()

    btn = Button(janelaProd, text="Adicionar", command=adiciona)
    btn.pack()

def deletarProd():
    janelaProdApagar = Toplevel()
    janelaProdApagar.resizable(False, False)
    janelaProdApagar.title("Deletar Produto")
    janelaProdApagar.geometry("900x700")
    janelaProdApagar.configure(background="#17c9ff")
    icone = "C:/Users/rikel/OneDrive/Documentos/MeusProjetos/Caixa-com-python/imagens/icon.ico"
    janelaProdApagar.iconbitmap(icone)

    lblTitulo = Label(janelaProdApagar, text="Deletar produto", background="#17c9ff")
    lblTitulo.pack()

    lblCod = Label(janelaProdApagar, text="Digite o código do produto a ser deletado", background="#17c9ff")
    lblCod.pack()

    entradaCod = Entry(janelaProdApagar)
    entradaCod.pack()

    def deleta():
        entCod = entradaCod.get()
        vsql = "DELETE FROM Produtos WHERE Cod_Prod="+entCod
        query(vsql)
        # Fechar a janela após deletar o produto
        janelaProdApagar.destroy()

    btn = Button(janelaProdApagar, text="Deletar", command=deleta)
    btn.pack()

def consultarPorNome():
    print("Consulta por nome")

def consultarPorID():
    print("Consulta por ID")

def sobreNos():
    print("Sobre nós")

def fechar():
    main.quit()

main = tk.Tk()
main.resizable(False, False)
main.title("Projeto Caixa")
main.geometry("900x700")
main.configure(background="#17c9ff")
icone = "C:/Users/rikel/OneDrive/Documentos/MeusProjetos/Caixa-com-python/imagens/icon.ico"
main.iconbitmap(icone)

# Inicializar a conexão
conexao()

# Barra de menu
barraDeMenus = Menu(main)

menuProduto = Menu(barraDeMenus, tearoff=0)
menuProduto.add_command(label="Adicionar Produto", command=adicionarProd)
menuProduto.add_command(label="Deletar Produto", command=deletarProd)
barraDeMenus.add_cascade(label="Produtos", menu=menuProduto)

menuConsulta = Menu(barraDeMenus, tearoff=0)
menuConsulta.add_command(label="Por nome", command=consultarPorNome)
menuConsulta.add_command(label="Por ID", command=consultarPorID)
barraDeMenus.add_cascade(label="Consulta", menu=menuConsulta)

menuSobre = Menu(barraDeMenus, tearoff=0)
menuSobre.add_command(label="Sobre nós", command=sobreNos)
barraDeMenus.add_cascade(label="Sobre", menu=menuSobre)

menuFechar = Menu(barraDeMenus, tearoff=0)
menuFechar.add_command(label="Fechar", command=fechar)
barraDeMenus.add_cascade(label="Fechar", menu=menuFechar)

main.config(menu=barraDeMenus)

# Título da janela
titulo = Label(main, text="Caixa", background="#17c9ff", font=("Bahnschrift", 30))
titulo.place(x=-30, y=0, width=900, height=100)

image = Image.open("C:/Users/rikel/OneDrive/Documentos/MeusProjetos/Caixa-com-python/imagens/carrinho.ico")
photo = ImageTk.PhotoImage(image)
img = Label(main, image=photo, background="#17c9ff")
img.place(x=500, y=0)

main.mainloop()
