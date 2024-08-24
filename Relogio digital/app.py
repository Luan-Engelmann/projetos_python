#Relógio digital com interface em phyton

from tkinter import *
from datetime import datetime

cor1 = "#000000"
cor2 = "#fafcff"
cor3 = "#FF0000"
cor4 = "#eb463b"
cor5 = "#dedcdc"
cor6 = "#3080f0"

janela = Tk()
janela.title("")
janela.geometry('450x180')
janela.resizable(width=FALSE, height=FALSE)
janela.configure(background=cor1)

def atualizar_relogio():
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime("%Y")

    l1.config(text=hora)
    l2.config(text=f"{dia_semana}\u00a0{dia}/{mes}/{ano}")

    l1.after(200, atualizar_relogio)

l1=Label(janela, text="10:05:05", font=('Arial', 80),bg=cor1, fg=cor3 )
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(janela, font=('Arial, 20'), bg=cor1, fg=cor3)
l2.grid(row=1, column=0, sticky=NW, padx=5)

atualizar_relogio()

janela.mainloop()


