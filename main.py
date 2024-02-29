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

def consultar(sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    return res


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
    janelaConsultaNome = Toplevel()
    janelaConsultaNome.resizable(False, False)
    janelaConsultaNome.title("Consultar produto por nome")
    janelaConsultaNome.geometry("900x700")
    janelaConsultaNome.configure(background="#17c9ff")
    icone = "C:/Users/rikel/OneDrive/Documentos/MeusProjetos/Caixa-com-python/imagens/icon.ico"
    janelaConsultaNome.iconbitmap(icone)

    lblCod = Label(janelaConsultaNome, text="Digite o nome do produto a ser consultado", background="#17c9ff")
    lblCod.pack()

    entradaNome = Entry(janelaConsultaNome)
    entradaNome.pack()

    lblSaida = Label(janelaConsultaNome, text="", background="#fff")
    lblSaida.pack()

    def consultaNome():
        entNome = entradaNome.get()
        vsql = "SELECT * FROM Produtos WHERE Nome_Prod LIKE '%"+entNome+"%'"
        res = consultar(vsql)
        for nome in res:
            lblSaida.config(text="Nome do produto: {};\nCódigo do produto: {};\nValor do produto: {};\nQuantidade do Produto: {}".format(nome[3], nome[0], nome[1], nome[2]))
        

    btn = Button(janelaConsultaNome, text="Consultar", command=consultaNome)
    btn.pack()

def consultarPorCod():
    janelaConsultaCod = Toplevel()
    janelaConsultaCod.resizable(False, False)
    janelaConsultaCod.title("Consultar produto por código")
    janelaConsultaCod.geometry("900x700")
    janelaConsultaCod.configure(background="#17c9ff")
    icone = "C:/Users/rikel/OneDrive/Documentos/MeusProjetos/Caixa-com-python/imagens/icon.ico"
    janelaConsultaCod.iconbitmap(icone)

    lblCod = Label(janelaConsultaCod, text="Digite o código do produto a ser consultado", background="#17c9ff")
    lblCod.pack()

    entradaCod = Entry(janelaConsultaCod)
    entradaCod.pack()

    lblSaida = Label(janelaConsultaCod, text="", background="#fff")
    lblSaida.pack()

    def consultaNome():
        entCod = entradaCod.get()
        vsql = "SELECT * FROM Produtos WHERE Cod_Prod LIKE '%"+entCod+"%'"
        res = consultar(vsql)
        for nome in res:
            lblSaida.config(text="Código do produto: {};\nNome do produto: {};\nValor do produto: {};\nQuantidade do Produto: {}".format(nome[0], nome[3], nome[1], nome[2]))
        

    btn = Button(janelaConsultaCod, text="Consultar", command=consultaNome)
    btn.pack()

    #Frame da img
    #Frame_igm = Frame(sobre, background="#aad1fc")
    #Frame_igm.place(x =40, y = 100, width= 300, height= 400)
    #foto
    #try: 
        #image = Image.open("C:/Users/rikel/OneDrive/Documentos/MeusProjetos/Caixa-com-python/imagens/joia.gif")
        #photo = ImageTk.PhotoImage(image)
        #img = Label(Frame_igm, image=photo)
        #img.pack(pady=50)
    #except EXCEPTION as erro:
        #print(erro)

def sobreNos():
    sobre = Toplevel() 
    sobre.resizable(False, False) 
    icone = "C:/Users/rikel/OneDrive/Documentos/MeusProjetos/Caixa-com-python/imagens/icon.ico"
    sobre.iconbitmap(icone)
    sobre.title("Sobre nós")
    sobre.geometry("900x700")
    sobre.configure(background="#17c9ff")
    
    #Frame da img
    Frame_igm = Label(sobre, background="#17c9ff")
    Frame_igm.place(x =40, y = 100, width= 300, height= 400)
    #foto
    try: 
        image = Image.open("C:/Users/rikel/OneDrive/Documentos/MeusProjetos/Caixa-com-python/imagens/joia.gif")
        photo = ImageTk.PhotoImage(image)
        img = Label(Frame_igm, image=photo)
        img.pack(pady=50)
    except Exception as erro:
        print(erro)


    #Frame texto
    Frame_txt = Label(sobre, background="#17c9ff")
    Frame_txt.place(x = 370, y = 100, width= 500, height= 400)
    #Parágrafos
    h1 = Label(Frame_txt,text="Obrigado!", font=("Trebuchet MS", 30), background="#17c9ff")
    h1.pack(anchor="nw", padx=10, pady=60)
    p1 = Label(Frame_txt,text="Agradeço pelo interesse e pela avaliação!", font=("Segoe UI",16), background="#17c9ff")
    p1.pack(anchor="nw", padx=10)
    p2 = Label(Frame_txt,text="Desenvolvido por Rikelme Sousa de Carvalho", font=("Segoe UI",16), background="#17c9ff")
    p2.pack(anchor="nw", padx=10)
    sobre.mainloop()

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
menuConsulta.add_command(label="Por Cod", command=consultarPorCod)
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
