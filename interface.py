import tkinter as tk
from tkinter import font
import random

def gerar_numero():
    return "55 " + str(random.randint(10, 99)) + " " + str(random.randint(1000, 9999)) + "-" + str(random.randint(1000, 9999))

def mostrar_mensagem1(event=None):
    esconder_contatos()  
    quadrado_mensagem1.place(x=104, y=20)
    label_mensagem1.place(x=135, y=7)
    label_conteudo.place(x=100, y=60)
    botao_adicionar.place(x=105, y=160) 
    botao_enviar.place(x=125, y=280) 
    label_enviando.place(x=195, y=400)   

def esconder_mensagem1(event=None):
    label_mensagem1.place_forget()
    label_conteudo.place_forget()
    quadrado_mensagem1.place_forget()
    botao_adicionar.place_forget()
    botao_enviar.place_forget()  
    label_enviando.place_forget()  

def mostrar_contatos(event=None):
    esconder_mensagem1()  
    quadrado_contatos.place(x=104, y=50)
    label_contatos.place(x=105, y=7)
    label_contato1.place(x=10, y=50)  
    label_numero1.place(x=170, y=50)  
    label_contato2.place(x=10, y=80)  
    label_numero2.place(x=170, y=80)  
    label_imagem_contato1.place(x=300, y=50)  
    label_imagem_contato2.place(x=300, y=80)  

    botao_adicionar_grupo.place(x=160, y=240)  
    label_enviando_grupo.place(x=200, y=400)  

    
    botao_adicionar.place_forget()
    label_enviando.place_forget()

def esconder_contatos(event=None):
    label_contatos.place_forget()
    quadrado_contatos.place_forget()
    label_contato1.place_forget()  
    label_numero1.place_forget()  
    label_contato2.place_forget()  
    label_numero2.place_forget()  
    label_imagem_contato1.place_forget()  
    label_imagem_contato2.place_forget()  

    botao_adicionar_grupo.place_forget()  
    label_enviando_grupo.place_forget()  

def adicionar_contato():
    
    novo_contato = gerar_numero()
    
    if label_contato1.cget("text") == "":
        label_contato1.config(text="Novo Contato 1")
        label_numero1.config(text=novo_contato)
    elif label_contato2.cget("text") == "":
        label_contato2.config(text="Novo Contato 2")
        label_numero2.config(text=novo_contato)

janela = tk.Tk()
janela.title("Minha Interface")

quadrado_direita = tk.Frame(janela, width=500, height=450, bg="#232323")
quadrado_direita.pack_propagate(0)  
quadrado_direita.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

label_quadrado_direita = tk.Label(quadrado_direita, text="", font=font.Font(family="Helvetica", size=14), bg="#232323", fg="white")
label_quadrado_direita.pack(pady=10)

fonte = font.Font(family="Helvetica", size=12)

menu_esquerda = tk.Frame(janela, width=400, height=450, bg="black", bd=2, relief=tk.SOLID)
menu_esquerda.pack(side=tk.LEFT, fill=tk.BOTH)

imagem = tk.PhotoImage(file="./image_1.png")
imagem = imagem.subsample(3, 3)
label_imagem = tk.Label(menu_esquerda, image=imagem, bg="black")
label_imagem.pack(pady=(25, 40))

quadrado_mensagem1 = tk.Frame(quadrado_direita, bg="#1c1a1b", width=350, height=120)  
label_mensagem1 = tk.Label(quadrado_mensagem1, text="Mensagem 1", font=fonte, fg="white", bg="#1c1a1b")
label_conteudo = tk.Label(quadrado_mensagem1, text="Conteúdo Mensagem", font=fonte, fg="white", bg="#1c1a1b")
botao_adicionar = tk.Button(quadrado_direita, text="+ Adicionar Contatos", command=adicionar_contato, font=fonte, fg="#808080", bg="#1c1a1b", width=38, height=5, bd=0)  
botao_enviar = tk.Button(quadrado_direita, text="Enviar", font=fonte, fg="#FFF", bg="#343230", width=33, height=2, bd=0)  
label_enviando = tk.Label(quadrado_direita, text="Enviando 1/20000...", font=fonte, fg="#54b82b", bg="#232323")

quadrado_contatos = tk.Frame(quadrado_direita, bg="#1c1a1b", width=350, height=120)  
label_contatos = tk.Label(quadrado_contatos, text="Grupo de Contatos 1", font=fonte, fg="white", bg="#1c1a1b")
label_contato1 = tk.Label(quadrado_contatos, text="Contato 1", font=fonte, fg="white", bg="#1c1a1b")  
label_numero1 = tk.Label(quadrado_contatos, text=gerar_numero(), font=fonte, fg="white", bg="#1c1a1b")  
label_contato2 = tk.Label(quadrado_contatos, text="Contato 2", font=fonte, fg="white", bg="#1c1a1b")  
label_numero2 = tk.Label(quadrado_contatos, text=gerar_numero(), font=fonte, fg="white", bg="#1c1a1b")  

# Carregar a imagem
imagem_contato = tk.PhotoImage(file="./green.png")

# Carregar a segunda imagem
imagem_contato2 = tk.PhotoImage(file="./x.png")

# Redimensionar a imagem
imagem_contato2 = imagem_contato2.subsample(3, 3)  

# Redimensionar a imagem
imagem_contato = imagem_contato.subsample(3, 3)  

# Criar um rótulo com a imagem
label_imagem_contato1 = tk.Label(quadrado_contatos, image=imagem_contato, bg="#1c1a1b")
label_imagem_contato2 = tk.Label(quadrado_contatos, image=imagem_contato2, bg="#1c1a1b")

# Posicionar o rótulo na interface
label_imagem_contato1.place(x=300, y=30)  
label_imagem_contato2.place(x=300, y=60)  

botao_adicionar_grupo = tk.Button(quadrado_direita, text="+ Adicionar Grupo de Contatos", command=adicionar_contato, font=fonte, fg="#FFF", bg="#232323", bd=0, highlightthickness=0)
botao_adicionar_grupo.place(x=10, y=90)


label_enviando_grupo = tk.Label(quadrado_direita, text="Enviando 1/2000...", font=fonte, fg="#54b82b", bg="#232323")
label_enviando_grupo.place(x=10, y=280)  

botao1 = tk.Button(menu_esquerda, text="Mensagens", command=mostrar_mensagem1, bg="#111111", fg="white", bd=0, highlightthickness=0, height=2, width=15, font=fonte)
botao1.pack(pady=6, padx=(0, 0), fill=tk.X)

botao2 = tk.Button(menu_esquerda, text="Contatos", command=mostrar_contatos, bg="#111111", fg="white", bd=0, highlightthickness=0, height=2, width=15, font=fonte)
botao2.pack(pady=6, padx=0, fill=tk.X)

botao3 = tk.Button(menu_esquerda, text="Registro", command=lambda: print("Botão 3 clicado"), bg="#111111", fg="white", bd=0, highlightthickness=0, height=2, width=15, font=fonte)
botao3.pack(pady=6, padx=0, fill=tk.X)

botao4 = tk.Button(menu_esquerda, text="Configurações", command=lambda: print("Botão 4 clicado"), bg="#111111", fg="white", bd=0, highlightthickness=0, height=2, width=15, font=fonte)
botao4.pack(side=tk.BOTTOM, pady=25, padx=0, fill=tk.X)


mostrar_mensagem1()


janela.mainloop()
