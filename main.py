import pyodbc
import tkinter as tk
from tkinter import Label, Entry, Button, Menu, Toplevel
from PIL import Image, ImageTk 
from tkinter import messagebox
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
    janelaProd.title("Adicionar Produto ao Estoque")
    janelaProd.geometry("900x700")
    janelaProd.configure(background="#17c9ff")
    icone = "C:/Users/rikel/OneDrive/Documentos/MeusProjetos/Caixa-com-python/imagens/icon.ico"
    janelaProd.iconbitmap(icone)

    lblTitulo = Label(janelaProd, text="Adicionar produto", font=("Trebuchet MS", 30), background="#17c9ff")
    lblTitulo.pack(pady=30)

    lblCod = Label(janelaProd, text="Código do produto", font=("Segoe UI", 16), background="#17c9ff")
    lblCod.pack(pady=10)

    entradaCod = Entry(janelaProd)
    entradaCod.pack()

    lbl1 = Label(janelaProd, text="Nome do produto", font=("Segoe UI", 16), background="#17c9ff")
    lbl1.pack(pady=10)

    entradaNome = Entry(janelaProd)
    entradaNome.pack()

    lbl2 = Label(janelaProd, text="Valor do produto", font=("Segoe UI", 16), background="#17c9ff")
    lbl2.pack(pady=10)

    entradaValor = Entry(janelaProd)
    entradaValor.pack()

    lbl3 = Label(janelaProd, text="Quantidade do produto", font=("Segoe UI", 16), background="#17c9ff")
    lbl3.pack(pady=10)

    entradaQntd = Entry(janelaProd)
    entradaQntd.pack(pady=10)

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

    Frame_igm = Label(janelaProd, background="#17c9ff")
    Frame_igm.pack()
    try: 
        image = Image.open("C:/Users/rikel/OneDrive/Documentos/MeusProjetos/Caixa-com-python/imagens/carrinhocheio.gif")
        photo = ImageTk.PhotoImage(image)
        img = Label(Frame_igm, image=photo, background="#17c9ff")
        img.pack()
    except Exception as erro:
        print(erro)

    janelaProd.mainloop()

def deletarProd():
    janelaProdApagar = Toplevel()
    janelaProdApagar.resizable(False, False)
    janelaProdApagar.title("Deletar Produto do Estoque")
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

def carrinho():
    janelaCarrinho = Toplevel()
    janelaCarrinho.resizable(False, False)
    janelaCarrinho.title("Carrinho")
    janelaCarrinho.geometry("900x700")
    janelaCarrinho.configure(background="#17c9ff")
    icone = "C:/Users/rikel/OneDrive/Documentos/MeusProjetos/Caixa-com-python/imagens/icon.ico"
    janelaCarrinho.iconbitmap(icone)

    lblTitulo = Label(janelaCarrinho, text="Carrinho de compras", background="#17c9ff")
    lblTitulo.pack()

    lblNome = Label(janelaCarrinho, text="Nome do produto a ser adicionado ao carrinho", background="#17c9ff")
    lblNome.pack()

    entradaNome = Entry(janelaCarrinho)
    entradaNome.pack()

    lblQntd = Label(janelaCarrinho, text="Quantidade do produto", background="#17c9ff")
    lblQntd.pack()

    entradaQntd = Entry(janelaCarrinho)
    entradaQntd.pack()

    lblSaida = Label(janelaCarrinho, text="", background="#fff")
    lblSaida.pack()

    lblProdCar = Label(janelaCarrinho, text="", background="#fff")
    lblProdCar.pack()

    prodAdicionados = []
    lblProdAdicionados = Label(janelaCarrinho, text="", background="#fff")
    lblProdAdicionados.pack()

    def consulta():
        lblProdCar.config(text="")
        entNome = entradaNome.get()
        entQntd = int(entradaQntd.get())
        vsql = "SELECT Quantidade_Prod FROM Produtos WHERE Nome_Prod LIKE '%"+entNome+"%'"
        sqlNome = "SELECT * FROM Produtos WHERE Nome_Prod LIKE '%"+entNome+"%'"
        res = consultar(vsql)
        res2 = consultar(sqlNome)
        quantidade_disponivel = int(res[0][0]) if res else 0  # Convertendo para inteiro
        if quantidade_disponivel <= 0 or res2 == False:
            messagebox.showinfo(title="Produto sem estoque ou não existe", message="Este produto está sem estoque ou não existe no estoque")
        else:
            nova_quantidade = quantidade_disponivel - entQntd
            vsql2 = "UPDATE Produtos SET Quantidade_Prod = {} WHERE Nome_Prod LIKE '%{}%'".format(nova_quantidade, entNome)
            query(vsql2)
            prodAdicionados.append(entNome)
            lblProdAdicionados.config(text= "Produtos no carrinho: {}".format(prodAdicionados))
            lblProdCar.config(text="Produto adicionado!\n")
        entradaNome.delete('0', 'end')
        entradaQntd.delete('0', 'end')

    btn = Button(janelaCarrinho, text="Adicionar ao carrinho", command=consulta)
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
menuProduto.add_command(label="Adicionar Produto ao Estoque", command=adicionarProd)
menuProduto.add_command(label="Deletar Produto do Estoque", command=deletarProd)
menuProduto.add_command(label="Carrinho", command=carrinho)
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
