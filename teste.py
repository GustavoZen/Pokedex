import tkinter as tk
from tkinter import ttk
from pokemon_list import pokemons_primeira_geracao
from pokemon_list import tipos_pokemon_primeira_geracao
import os

class MyButton (tk.Button):
    tipos = ""

def on_canvas_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

def BarraDeRolagem(janela):
    scrollbar = ttk.Scrollbar(janela, orient="vertical")
    scrollbar.grid(row=0, column=1, sticky="ns")

    frame_elementos = tk.Frame(janela)
    frame_elementos.grid(row=0, column=0, sticky="nsew")

    canvas = tk.Canvas(frame_elementos, yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar.config(command=canvas.yview)

    frame_mestre = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame_mestre, anchor="nw")

    canvas.bind("<Configure>", on_canvas_configure)

    janela.grid_rowconfigure(0, weight=1)
    janela.grid_columnconfigure(0, weight=1)

    return scrollbar, frame_elementos, canvas, frame_mestre

def botao1(janela):
    print("Tamanho atual da janela: " + str(janela.winfo_width()) + " x " + str(janela.winfo_height()))
    
# Criando a janela principal
janela = tk.Tk()
janela.title("Minha Página Tkinter")
janela.geometry("652x505")
janela.resizable(width=False, height=False)

scrollbar, frame_elementos, canvas, frame_mestre = BarraDeRolagem(janela)
cont = 0
linha = 1
listaDeBotoes = []
while(cont<151):
    for coluna in range(5):
        if cont < 151:
            caminho_imagem = os.path.join("C:\\Users\\Aluno\\Desktop\\Python\\senac\\sprites", str(cont+1) + ".png")

            imagem = tk.PhotoImage(file=caminho_imagem)
            
            texto_var = tk.StringVar()
            texto_var.set(pokemons_primeira_geracao[cont] + " #" + str(cont+1) + "\n" + tipos_pokemon_primeira_geracao[cont])
            
            # Criando o botão com a imagem e o texto
            botao = MyButton(frame_mestre, image=imagem, textvariable=texto_var, compound='top',height=100,width=100)
            botao.imagem = imagem  # Para evitar que a imagem seja coletada pelo garbage collector
            botao.grid(row=linha, column=coluna, padx=10, pady=10)
            listaDeBotoes.append(botao)
            
            cont += 1
    linha += 1

# Iniciando o loop principal
listaDeBotoes[1]['command'] = lambda:botao1(janela)
janela.mainloop()