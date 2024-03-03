import pyodbc
import tkinter as tk
from tkinter import Frame, Label, Entry, Button, Menu, Toplevel
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
    janelaProd.configure(background="#0A81AB")
    icone = "C:/Users/rikel/OneDrive/Documentos/MeusProjetos/Caixa-com-python/imagens/icon.ico"
    janelaProd.iconbitmap(icone)

    lblTitulo = Label(janelaProd, text="Adicionar produto", font=("Trebuchet MS", 30), background="#0A81AB")
    lblTitulo.pack(pady=20)

    lblCod = Label(janelaProd, text="Código do produto", font=("Segoe UI", 16), background="#0A81AB")
    lblCod.pack(pady=10)

    entradaCod = Entry(janelaProd, background="#F9DFDC")
    entradaCod.pack()

    lbl1 = Label(janelaProd, text="Nome do produto", font=("Segoe UI", 16), background="#0A81AB")
    lbl1.pack(pady=10)

    entradaNome = Entry(janelaProd, background="#F9DFDC")
    entradaNome.pack()

    lbl2 = Label(janelaProd, text="Valor do produto", font=("Segoe UI", 16), background="#0A81AB")
    lbl2.pack(pady=10)

    entradaValor = Entry(janelaProd, background="#F9DFDC")
    entradaValor.pack()

    lbl3 = Label(janelaProd, text="Quantidade do produto", font=("Segoe UI", 16), background="#0A81AB")
    lbl3.pack(pady=10)

    entradaQntd = Entry(janelaProd, background="#F9DFDC")
    entradaQntd.pack(pady=20)

    def adiciona():
        entCod = entradaCod.get()
        entNome = entradaNome.get()
        entValor = entradaValor.get()
        entQntd = entradaQntd.get()
        vsql = "INSERT INTO Produtos (Cod_Prod, ValorUnit_Prod, Quantidade_Prod, Nome_Prod) VALUES ('{}', '{}', '{}', '{}')".format(entCod, entValor, entQntd, entNome)
        query(vsql)
        # Fechar a janela após adicionar o produto
        janelaProd.destroy()

    btn = Button(janelaProd, text="Adicionar",background="#0C4271", foreground="#F9DFDC", relief="solid" , font=("Segoe UI", 12), command=adiciona)
    btn.pack()

    Frame_igm = Label(janelaProd, background="#0A81AB")
    Frame_igm.pack()
    try: 
        image = Image.open("C:/Users/rikel/OneDrive/Documentos/MeusProjetos/Caixa-com-python/imagens/carrinhocheio.gif")
        photo = ImageTk.PhotoImage(image)
        img = Label(Frame_igm, image=photo, background="#0A81AB")
        img.pack()
    except Exception as erro:
        print(erro)

    janelaProd.mainloop()

def deletarProd():
    janelaProdApagar = Toplevel()
    janelaProdApagar.resizable(False, False)
    janelaProdApagar.title("Deletar Produto do Estoque")
    janelaProdApagar.geometry("900x700")
    janelaProdApagar.configure(background="#0A81AB")
    icone = "C:/Users/rikel/OneDrive/Documentos/MeusProjetos/Caixa-com-python/imagens/icon.ico"
    janelaProdApagar.iconbitmap(icone)

    lblTitulo = Label(janelaProdApagar, text="Deletar produto", font=("Trebuchet MS", 30), background="#0A81AB")
    lblTitulo.pack(pady=20)

    lblCod = Label(janelaProdApagar, text="Digite o código do produto a ser deletado", font=("Segoe UI", 16), background="#0A81AB")
    lblCod.pack(pady=10)

    entradaCod = Entry(janelaProdApagar, background="#F9DFDC")
    entradaCod.pack(pady=10)

    def deleta():
        entCod = entradaCod.get()
        vsql = "DELETE FROM Produtos WHERE Cod_Prod="+entCod
        query(vsql)
        # Fechar a janela após deletar o produto
        janelaProdApagar.destroy()

    btn = Button(janelaProdApagar, text="Deletar",background="#0C4271", foreground="#F9DFDC", relief="solid" , font=("Segoe UI", 12), command=deleta)
    btn.pack(pady=20)
    
    Frame_igm = Label(janelaProdApagar, background="#0A81AB")
    Frame_igm.pack()
    try: 
        image = Image.open("C:/Users/rikel/OneDrive/Documentos/MeusProjetos/Caixa-com-python/imagens/lixeiras.gif")
        photo = ImageTk.PhotoImage(image)
        img = Label(Frame_igm, image=photo, background="#0A81AB")
        img.pack()
    except Exception as erro:
        print(erro)

    janelaProdApagar.mainloop()


def abastProd():
    janelaAbastProd = Toplevel()
    janelaAbastProd.resizable(False, False)
    janelaAbastProd.title("Adicionar Produto ao Estoque")
    janelaAbastProd.geometry("900x700")
    janelaAbastProd.configure(background="#0A81AB")
    icone = "C:/Users/rikel/OneDrive/Documentos/MeusProjetos/Caixa-com-python/imagens/icon.ico"
    janelaAbastProd.iconbitmap(icone)

    lblTitulo = Label(janelaAbastProd, text="Abastecer estoque de um produto", font=("Trebuchet MS", 30), background="#0A81AB")
    lblTitulo.pack(pady=20)

    lbl1 = Label(janelaAbastProd, text="Nome do produto", font=("Segoe UI", 16), background="#0A81AB")
    lbl1.pack(pady=10)

    entradaNome = Entry(janelaAbastProd, background="#F9DFDC")
    entradaNome.pack(pady=10)

    lbl3 = Label(janelaAbastProd, text="Quantidade do produto a ser adicionado ao estoque", font=("Segoe UI", 16), background="#0A81AB")
    lbl3.pack(pady=10)

    entradaQntd = Entry(janelaAbastProd, background="#F9DFDC")
    entradaQntd.pack(pady=20)

    lblRes = Label(janelaAbastProd, text="", font=("Segoe UI", 16), background="#0A81AB")
    lblRes.pack(pady=20)


    def abastece():
        entNome = entradaNome.get()
        entQntd = entradaQntd.get()
        vsql = "SELECT Quantidade_Prod FROM Produtos WHERE Nome_Prod LIKE '%"+entNome+"%'" 
        res = consultar(vsql)
        if entQntd == '' or not entQntd.isdigit():
            messagebox.showwarning(title="ERRO", message="A quantidade deve ser um número válido")
            return
        if res:
            qntd = int(res[0][0])
        else:
            qntd = 0
            
        novaQntd = int(entQntd) + qntd
        try: 
            vsql2 = "UPDATE Produtos SET Quantidade_Prod = {} WHERE Nome_Prod LIKE '%{}%'".format(novaQntd, entNome)
            query(vsql2)
            lblRes.config(text="Produto reabastecido com sucesso!")
        except Exception as erro:
            print(erro)

    btn = Button(janelaAbastProd, text="Abastecer",background="#0C4271", foreground="#F9DFDC", relief="solid" , font=("Segoe UI", 12), command=abastece)
    btn.pack(pady=10)



def carrinho():
    janelaCarrinho = Toplevel()
    janelaCarrinho.resizable(False, False)
    janelaCarrinho.title("Carrinho")
    janelaCarrinho.geometry("900x700")
    janelaCarrinho.configure(background="#0A81AB")
    icone = "C:/Users/rikel/OneDrive/Documentos/MeusProjetos/Caixa-com-python/imagens/icon.ico"
    janelaCarrinho.iconbitmap(icone)

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
            messagebox.showinfo(title="Info", message="Produto adicionado ao carrinho!")
    
    def limpar():
        entradaNome.delete('0', 'end')
        entradaQntd.delete('0', 'end')

    def total():
        entNome = entradaNome.get()
        entQntd = entradaQntd.get()
        if entQntd == '' or not entQntd.isdigit():
            messagebox.showwarning(title="ERRO", message="A quantidade deve ser um número válido")
            return
        sqlVal = "SELECT ValorUnit_Prod FROM Produtos WHERE Nome_Prod LIKE '%" + entNome + "%'"
        res = consultar(sqlVal)
        if res:
            valorUnit = float(res[0][0])
        else:
            valorUnit = 0
            
        valTot = float(entQntd) * valorUnit
        listaTotal.append(valTot)
        lblTotal.config(text="Valor total: {}".format(sum(listaTotal)))
        entradaNome.delete('0', 'end')
        entradaQntd.delete('0', 'end')

    lblTitulo = Label(janelaCarrinho, text="Carrinho de compras", font=("Trebuchet MS", 30), background="#0A81AB")
    lblTitulo.pack(pady=20)

    lblNome = Label(janelaCarrinho, text="Nome do produto a ser adicionado ao carrinho", background="#0A81AB", font=("Segoe UI", 16))
    lblNome.pack(pady=10)

    entradaNome = Entry(janelaCarrinho, background="#F9DFDC")
    entradaNome.pack()

    lblQntd = Label(janelaCarrinho, text="Quantidade do produto", background="#0A81AB", font=("Segoe UI", 16))
    lblQntd.pack(pady=10)

    entradaQntd = Entry(janelaCarrinho, background="#F9DFDC")
    entradaQntd.pack()
    
    btnAdd = Button(janelaCarrinho, text="Adicionar ao carrinho",background="#0C4271", foreground="#F9DFDC", relief="solid" , font=("Segoe UI", 12), command=consulta)
    btnAdd.place(x = 315, y = 300)

    btnLimpar = Button(janelaCarrinho, text="Limpar",background="#0C4271", foreground="#F9DFDC", relief="solid" , font=("Segoe UI", 12), command=limpar)
    btnLimpar.place(x = 515, y = 300)

    fr_notaFiscal = Frame(janelaCarrinho, relief="solid", background="#fff")
    fr_notaFiscal.place(x = 300, y = 400, width=300, height=400)

    prodAdicionados = []
    lblProdAdicionados = Label(fr_notaFiscal, text="Produtos no carrinho: ", background="#fff", font=("Segoe UI", 16))
    lblProdAdicionados.pack(pady=10)

    listaTotal = []
    lblTotal = Label(fr_notaFiscal, text="Valor total: ", background="#fff", font=("Segoe UI", 16))
    lblTotal.pack()

    notaFiscal = []

    btnTotal = Button(janelaCarrinho, text="Mostrar total",background="#0C4271", foreground="#F9DFDC", relief="solid" , font=("Segoe UI", 12), command=total)
    btnTotal.pack()

def consultarPorNome():
    janelaConsultaNome = Toplevel()
    janelaConsultaNome.resizable(False, False)
    janelaConsultaNome.title("Consultar produto por nome")
    janelaConsultaNome.geometry("900x700")
    janelaConsultaNome.configure(background="#0A81AB")
    icone = "C:/Users/rikel/OneDrive/Documentos/MeusProjetos/Caixa-com-python/imagens/icon.ico"
    janelaConsultaNome.iconbitmap(icone)

    lblTitle = Label(janelaConsultaNome, text="Consultar produto por nome", font=("Trebuchet MS", 30), background="#0A81AB")
    lblTitle.pack(pady=20)

    lblCod = Label(janelaConsultaNome, text="Digite o nome do produto a ser consultado", font=("Segoe UI", 16), background="#0A81AB")
    lblCod.pack(pady=20)

    entradaNome = Entry(janelaConsultaNome, background="#F9DFDC")
    entradaNome.pack(pady=10)

    lblSaida = Label(janelaConsultaNome, text="", background="#0A81AB", font=("Segoe UI", 16))
    lblSaida.pack(pady=20)

    def consultaNome():
        entNome = entradaNome.get()
        vsql = "SELECT * FROM Produtos WHERE Nome_Prod LIKE '%"+entNome+"%'"
        res = consultar(vsql)
        for nome in res:
            lblSaida.config(text="Nome do produto: {};\nCódigo do produto: {};\nValor do produto: {};\nQuantidade do Produto: {}".format(nome[3], nome[0], nome[1], nome[2]))
        

    btn = Button(janelaConsultaNome, text="Consultar", background="#0C4271", fg="#F9DFDC", relief="solid" , font=("Segoe UI", 12), command=consultaNome)
    btn.pack()

    Frame_igm = Label(janelaConsultaNome, background="#0A81AB")
    Frame_igm.pack()
    try: 
        image = Image.open("C:/Users/rikel/OneDrive/Documentos/MeusProjetos/Caixa-com-python/imagens/lupa.gif")
        photo = ImageTk.PhotoImage(image)
        img = Label(Frame_igm, image=photo, background="#0A81AB")
        img.pack()
    except Exception as erro:
        print(erro)

    janelaConsultaNome.mainloop()

def consultarPorCod():
    janelaConsultaCod = Toplevel()
    janelaConsultaCod.resizable(False, False)
    janelaConsultaCod.title("Consultar produto por código")
    janelaConsultaCod.geometry("900x700")
    janelaConsultaCod.configure(background="#0A81AB")
    icone = "C:/Users/rikel/OneDrive/Documentos/MeusProjetos/Caixa-com-python/imagens/icon.ico"
    janelaConsultaCod.iconbitmap(icone)

    
    lblTitle = Label(janelaConsultaCod, text="Consultar produto por código", font=("Trebuchet MS", 30), background="#0A81AB")
    lblTitle.pack(pady=20)

    lblCod = Label(janelaConsultaCod, text="Digite o código do produto a ser consultado", font=("Segoe UI", 16), background="#0A81AB")
    lblCod.pack(pady=20)

    entradaCod = Entry(janelaConsultaCod, background="#F9DFDC")
    entradaCod.pack(pady=10)

    lblSaida = Label(janelaConsultaCod, text="", background="#0A81AB")
    lblSaida.pack(pady=20)

    def consultaNome():
        entCod = entradaCod.get()
        vsql = "SELECT * FROM Produtos WHERE Cod_Prod LIKE '%"+entCod+"%'"
        res = consultar(vsql)
        for nome in res:
            lblSaida.config(text="Código do produto: {};\nNome do produto: {};\nValor do produto: {};\nQuantidade do Produto: {}".format(nome[0], nome[3], nome[1], nome[2]))
        

    btn = Button(janelaConsultaCod, text="Consultar", background="#0C4271", fg="#F9DFDC", relief="solid" , font=("Segoe UI", 12), command=consultaNome)
    btn.pack()

    Frame_igm = Label(janelaConsultaCod, background="#0A81AB")
    Frame_igm.pack()
    try: 
        image = Image.open("C:/Users/rikel/OneDrive/Documentos/MeusProjetos/Caixa-com-python/imagens/lupa.gif")
        photo = ImageTk.PhotoImage(image)
        img = Label(Frame_igm, image=photo, background="#0A81AB")
        img.pack()
    except Exception as erro:
        print(erro)

    janelaConsultaCod.mainloop()

def sobreNos():
    sobre = Toplevel() 
    sobre.resizable(False, False) 
    icone = "C:/Users/rikel/OneDrive/Documentos/MeusProjetos/Caixa-com-python/imagens/icon.ico"
    sobre.iconbitmap(icone)
    sobre.title("Sobre nós")
    sobre.geometry("900x700")
    sobre.configure(background="#0A81AB")
    
    #Frame da img
    Frame_igm = Label(sobre, background="#0A81AB")
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
    Frame_txt = Label(sobre, background="#0A81AB")
    Frame_txt.place(x = 370, y = 100, width= 500, height= 400)
    #Parágrafos
    h1 = Label(Frame_txt,text="Obrigado!", font=("Trebuchet MS", 30), background="#0A81AB")
    h1.pack(anchor="nw", padx=10, pady=60)
    p1 = Label(Frame_txt,text="Agradeço pelo interesse e pela avaliação!", font=("Segoe UI",16), background="#0A81AB")
    p1.pack(anchor="nw", padx=10)
    p2 = Label(Frame_txt,text="Desenvolvido por Rikelme Sousa de Carvalho", font=("Segoe UI",16), background="#0A81AB")
    p2.pack(anchor="nw", padx=10)
    sobre.mainloop()

def fechar():
    main.quit()

main = tk.Tk()
main.resizable(False, False)
main.title("Projeto Caixa")
main.geometry("900x700")
main.configure(background="#0A81AB")
icone = "C:/Users/rikel/OneDrive/Documentos/MeusProjetos/Caixa-com-python/imagens/icon.ico"
main.iconbitmap(icone)

# Inicializar a conexão
conexao()

# Barra de menu
barraDeMenus = Menu(main)

menuProduto = Menu(barraDeMenus, tearoff=0)
menuProduto.add_command(label="Adicionar Produto ao Estoque", command=adicionarProd)
menuProduto.add_command(label="Deletar Produto do Estoque", command=deletarProd)
menuProduto.add_command(label="Abastecer Estoque de um Produto", command=abastProd)
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
titulo = Label(main, text="Caixa", background="#0A81AB", font=("Bahnschrift", 30))
titulo.place(x=-30, y=0, width=900, height=100)

image = Image.open("C:/Users/rikel/OneDrive/Documentos/MeusProjetos/Caixa-com-python/imagens/carrinho.ico")
photo = ImageTk.PhotoImage(image)
img = Label(main, image=photo, background="#0A81AB")
img.place(x=500, y=0)

main.mainloop()
