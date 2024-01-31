import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import time


# Função para importar imagens
def load_image(filename, width=None, height=None):
    image = Image.open(filename)
    if width and height:
        image = image.resize((width, height))
    image = ImageTk.PhotoImage(image)
    return image

def show_custom_message(message):
    custom_message = ctk.CTk()
    custom_message.title("Mensagem de parabenização")
    custom_message.geometry("600x400")

    label = ctk.CTkLabel(
        master=custom_message,
        text=message,
        font=('Verdana', 20),
        bg_color='teal',
        fg_color='#C08B66',
        corner_radius=10,
        text_color='black',
        width=600, height=400,
    )
    label.pack()

    # Adiciona animação simples de fade in
    alpha = 0
    def fade_in():
        nonlocal alpha
        if alpha < 1:
            alpha += 0.05
            label.configure(bg_color='transparent')
            custom_message.after(50, fade_in)
    fade_in()
    custom_message.after(40000, custom_message.destroy)  # Fecha a janela após 10 segundos
    custom_message.mainloop()


# minha janela principal
root = ctk.CTk()
root.title("Sorteio - Tuane Palma")
root.geometry("995x700")
root.resizable(False, False)
imagem_canva = load_image('sorteio4.png', width=1300, height=800)

# arte do sorteio
label = ctk.CTkLabel(
    master=root,
    image=imagem_canva,
    text='',
    width=1300, height=800,
    bg_color='#FF66C4',
    corner_radius=20
)
label.pack()

# Campo de texto - inicialmente vazio
textbox = ctk.CTkTextbox(
    master=root,
    width=560, height=50,
    scrollbar_button_color='teal',
    scrollbar_button_hover_color='#0064B3',
    border_width=5,
    bg_color='#302F2F',
    text_color='black',
    corner_radius=30,
    fg_color='white',
)
textbox.place(x=320, y=428)
textbox.configure(font=('Verdana', 28))
textbox.insert(ctk.END, "Seu username aparecerá aqui...")


# botão para sortear
btn_sortear = ctk.CTkButton(
    master=root,
    width=220, height=60,
    text='SORTEAR',
    fg_color='#545454',
    bg_color="#302F2F",
    hover_color="#242424",
    corner_radius=80,
    border_color="#242424",
    border_width=5,

)
btn_sortear.place(x=488, y=530)


# Função para sortear os nomes das pessoas que comentaram!
def sortear():
    # Criando a janela da barra de progressão
    root_barra = tk.Tk()
    root_barra.geometry("500x100")
    root_barra.title("Carregando...")
    

    # Criando a barra de progresso
    progress = ttk.Progressbar(
        master=root_barra,
        orient="horizontal",
        length=300,
        mode="determinate"
    )
    # Posicionando a barra de progresso na tela
    progress.pack(pady=10)

    # Função que simula o carregamento
    for i in range(101):
        # Atualiza o valor da barra de progresso
        progress['value'] = i
        # Atualiza a tela
        root_barra.update()
        # Adiciona um pequeno atraso para simular o processo
        time.sleep(0.05)

    # esonder a janela da barra de progressão
    root_barra.withdraw()

    nova_lista_em_ordem = [
    # 29 comentários
    'pamelaneves6568', 'pamelaneves6568', 'pamelaneves6568', 'pamelaneves6568', 'pamelaneves6568', 
    'pamelaneves6568', 'pamelaneves6568', 'pamelaneves6568', 'pamelaneves6568', 'pamelaneves6568', 
    'pamelaneves6568', 'pamelaneves6568', 'pamelaneves6568', 'pamelaneves6568', 'pamelaneves6568', 
    'pamelaneves6568', 'pamelaneves6568', 'pamelaneves6568', 'pamelaneves6568', 'pamelaneves6568', 
    'pamelaneves6568', 'pamelaneves6568', 'pamelaneves6568', 'pamelaneves6568', 'pamelaneves6568', 
    'pamelaneves6568', 'pamelaneves6568', 'pamelaneves6568', 'pamelaneves6568'
    ]


    sorteio = random.choice(nova_lista_em_ordem)
   

    # Atualiza o texto do CTkTextbox com o nome sorteado
    textbox.delete(1.0, ctk.END)  # Limpa o conteúdo atual
    textbox.insert(ctk.END, sorteio)

    root_barra.after(1000, lambda:show_custom_message(
        f"PARABÉNS!\n\n>> {sorteio} <<\n\nVocê acabou de receber o seu Momento Spa\ncom todos os protocolos de Boas Vindas\ne de BÔNUS:\n\n- Pé e mão pela Profissional\n\nDhanny Nails\n\nAproveite "))

# Configurando a função de sorteio para ser chamada pelo botão
btn_sortear.configure(command=sortear)


# Inicia o loop principal
root.mainloop()
