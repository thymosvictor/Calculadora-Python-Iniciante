from tkinter import *
from PIL import Image, ImageTk
import threading
from playsound import playsound

# ------------------ cores ------------------
cor1 = "#FFE4E1"
# cor2 = "#FFFDF9"
cor3 = "#fffffe"
cor4 = "#d1ebff"
cor5 = "#CFE8FF"
cor6 = "#56a2e8"  # texto
cor7 = "#bbd3e8"  # ao clicar

cor8 = "#c3d4ff"  # bg 
cor9 = "#536fb6"  # fg 
cor10 = "#8ba0d6"  # ao clicar 

# ------------------ janela ------------------
janela = Tk()
janela.title("Calculadora fofa")
janela.geometry("235x318")
janela.config(bg=cor1)
janela.resizable(False, False)

expressao = ""           
texto = StringVar()      
texto.set("")

def tocar_som_async(caminho):
    threading.Thread(target=lambda: playsound(caminho), daemon=True).start()

som_atual = [0]  # para alternar sons

def tocar_e_apagar():
    global expressao
    # toca som 
    if som_atual[0] == 0:
        tocar_som_async("aaagh.mp3")
        som_atual[0] = 1
    else:
        tocar_som_async("cozinhado.mp3")
        som_atual[0] = 0
    # apaga último caractere
    if expressao:
        expressao = expressao[:-1]
        texto.set(expressao)

def inserir_valor(v):
    global expressao
    expressao += str(v)
    texto.set(expressao)

def limpar():
    global expressao
    expressao = ""
    texto.set("")

def calcular():
    global expressao
    try:
        resultado = str(eval(expressao))
        texto.set(resultado)
        expressao = resultado
    except Exception:
        texto.set("Erro")
        expressao = ""

# ------------------ layout ------------------
frame_screen = Frame(janela, width=235, height=50, bg=cor3)
frame_screen.grid(row=0, column=0)

frame_body = Frame(janela, width=235, height=268, bg=cor3)
frame_body.grid(row=1, column=0)

# display (label)
label = Label(frame_screen, textvariable=texto, width=16, height=2, padx=7,
              relief="flat", anchor="e", justify=RIGHT, font=("Ivy", 18),
              bg=cor3, fg=cor6)
label.place(x=0, y=0)

# ------------------ linha 1 ------------------
b_1 = Button(frame_body, text="C", width=8, height=3, fg=cor6, bg=cor4,
             relief="flat", activebackground=cor7, activeforeground=cor6,
             font=("Comic Sans MS", 8, "bold"), command=limpar)
b_1.place(x=0, y=0)

b_2 = Button(frame_body, text="%", width=7, height=3, fg=cor6, bg=cor4,
             relief="flat", activebackground=cor7, activeforeground=cor6,
             font=("Comic Sans MS", 8, "bold"), command=lambda: inserir_valor("%"))
b_2.place(x=59, y=0)

b_3 = Button(frame_body, text="/", width=7, height=3, fg=cor6, bg=cor4,
             relief="flat", activebackground=cor7, activeforeground=cor6,
             font=("Comic Sans MS", 8, "bold"), command=lambda: inserir_valor("/"))
b_3.place(x=117, y=0)

# ícone fofo 
try:
    icon = Image.open("icon.jpg")
    icon = icon.resize((60, 50))
    icon_cute = ImageTk.PhotoImage(icon)
    b_4 = Button(frame_body, image=icon_cute, relief="flat", border=0, command=tocar_e_apagar)
    b_4.image = icon_cute
    b_4.place(x=176, y=0)
except Exception:
    # fallback
    b_4 = Button(frame_body, text="DEL", relief="flat", border=0, command=tocar_e_apagar)
    b_4.place(x=176, y=0)

# ------------------ linha 2 ------------------
b_5 = Button(frame_body, text="7", width=8, height=3, fg=cor6, bg=cor4,
             relief="flat", activebackground=cor7, activeforeground=cor6,
             font=("Comic Sans MS", 8, "bold"), command=lambda: inserir_valor("7"))
b_5.place(x=0, y=49)

b_6 = Button(frame_body, text="8", width=7, height=3, fg=cor6, bg=cor4,
             relief="flat", activebackground=cor7, activeforeground=cor6,
             font=("Comic Sans MS", 8, "bold"), command=lambda: inserir_valor("8"))
b_6.place(x=59, y=49)

b_7 = Button(frame_body, text="9", width=7, height=3, fg=cor6, bg=cor4,
             relief="flat", activebackground=cor7, activeforeground=cor6,
             font=("Comic Sans MS", 8, "bold"), command=lambda: inserir_valor("9"))
b_7.place(x=117, y=49)

b_8 = Button(frame_body, text="*", width=7, height=3, fg=cor9, bg=cor8,
             relief="flat", activebackground=cor10, activeforeground=cor9,
             font=("Comic Sans MS", 8, "bold"), command=lambda: inserir_valor("*"))
b_8.place(x=176, y=49)

# ------------------ linha 3 ------------------
b_9 = Button(frame_body, text="4", width=8, height=3, fg=cor6, bg=cor4,
             relief="flat", activebackground=cor7, activeforeground=cor6,
             font=("Comic Sans MS", 8, "bold"), command=lambda: inserir_valor("4"))
b_9.place(x=0, y=100)

b_10 = Button(frame_body, text="5", width=7, height=3, fg=cor6, bg=cor4,
              relief="flat", activebackground=cor7, activeforeground=cor6,
              font=("Comic Sans MS", 8, "bold"), command=lambda: inserir_valor("5"))
b_10.place(x=59, y=100)

b_11 = Button(frame_body, text="6", width=7, height=3, fg=cor6, bg=cor4,
              relief="flat", activebackground=cor7, activeforeground=cor6,
              font=("Comic Sans MS", 8, "bold"), command=lambda: inserir_valor("6"))
b_11.place(x=117, y=100)

b_12 = Button(frame_body, text="-", width=7, height=3, fg="#e8ba00", bg="#fff0b6",
              relief="flat", activebackground="#ffe67f", activeforeground="#e8ba00",
              font=("Comic Sans MS", 8, "bold"), command=lambda: inserir_valor("-"))
b_12.place(x=176, y=100)

# ------------------ linha 4 ------------------
b_13 = Button(frame_body, text="1", width=8, height=3, fg=cor6, bg=cor4,
              relief="flat", activebackground=cor7, activeforeground=cor6,
              font=("Comic Sans MS", 8, "bold"), command=lambda: inserir_valor("1"))
b_13.place(x=0, y=155)

b_14 = Button(frame_body, text="2", width=7, height=3, fg=cor6, bg=cor4,
              relief="flat", activebackground=cor7, activeforeground=cor6,
              font=("Comic Sans MS", 8, "bold"), command=lambda: inserir_valor("2"))
b_14.place(x=59, y=155)

b_15 = Button(frame_body, text="3", width=7, height=3, fg=cor6, bg=cor4,
              relief="flat", activebackground=cor7, activeforeground=cor6,
              font=("Comic Sans MS", 8, "bold"), command=lambda: inserir_valor("3"))
b_15.place(x=117, y=155)

b_16 = Button(frame_body, text="+", width=7, height=3, fg="#a170bb", bg="#efc3ff",
              relief="flat", activebackground="#d099e4", activeforeground="#a170bb",
              font=("Comic Sans MS", 8, "bold"), command=lambda: inserir_valor("+"))
b_16.place(x=176, y=155)

# ------------------ linha 5 ------------------
b_17 = Button(frame_body, text="0", width=15, height=3, fg=cor6, bg=cor4,
              relief="flat", activebackground=cor7, activeforeground=cor6,
              font=("Comic Sans MS", 8, "bold"), command=lambda: inserir_valor("0"))
b_17.place(x=0, y=215)

b_18 = Button(frame_body, text=".", width=9, height=3, fg=cor6, bg=cor4,
              relief="flat", activebackground=cor7, activeforeground=cor6,
              font=("Comic Sans MS", 10, "bold"), command=lambda: inserir_valor("."))
b_18.place(x=115, y=215)

b_19 = Button(frame_body, text="=", width=8, height=3, fg="#3b9f1d", bg="#adff95",
              relief="flat", activebackground="#80c46b", activeforeground="#3b9f1d",
              font=("Comic Sans MS", 8, "bold"), command=calcular)
b_19.place(x=176, y=215)

# ------------------ loop ------------------
janela.mainloop()

