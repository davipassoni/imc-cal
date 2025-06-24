from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser


co0 = "#000000"
co1 = "#FFFFFF"
co2 = "#FFFFFF"
co3 = "#8A4040"
co4 = "#000000"
co5 = "#000000"


janela = Tk()
janela.title("IMC")
janela.geometry("310x350")
janela.configure(bg=co1)
janela.resizable(False, False)


frame_cima = Frame(janela, width=310, height=50, bg=co1, relief="flat")
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=310, height=300, bg=co1, relief="flat")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

def abrir_nova_janela():
    nome = e_nome.get()
    peso = e_peso.get()
    altura = e_altura.get()

    if nome == "" or peso == "" or altura == "":
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
        return

    try:
        peso = float(peso.replace(',', '.'))
        altura = float(altura.replace(',', '.'))
        imc = peso / (altura ** 2)

        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif 18.5 <= imc < 25:
            classificacao = "Peso normal"
        elif 25 <= imc < 30:
            classificacao = "Sobrepeso"
        elif 30 <= imc < 35:
            classificacao = "Obesidade grau I"
        elif 35 <= imc < 40:
            classificacao = "Obesidade grau II"
        else:
            classificacao = "Obesidade grau III"

        
        nova = Toplevel(janela)
        nova.title("Resultado")
        nova.geometry("300x200")
        nova.configure(bg=co1)

        msg = (
            f"Olá, {nome}!\n\n"
            f"Peso: {peso:.2f} kg\n"
            f"Altura: {altura:.2f} m\n\n"
            f"Seu IMC é: {imc:.2f}\n"
            f"Classificação: {classificacao}"
        )
        Label(nova, text=msg, font=('Ivy', 12), bg=co1, fg=co4, justify=LEFT).pack(pady=20)
       

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos para peso e altura (ex: 70,5).")


Label(frame_cima, text="CALCULADORA DE IMC", height=1, anchor=NE, font=('Ivy', 15), bg=co1, fg=co4).place(x=5, y=5)
Label(frame_cima, width=275, text="", height=1, anchor=NW, font=("Ivy", 1), bg=co5).place(x=10, y=45)


Label(frame_baixo, text="Nome *", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4).place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, font=("", 15), relief="solid")
e_nome.place(x=14, y=50)

Label(frame_baixo, text="Peso (kg)", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4).place(x=10, y=90)
e_peso = Entry(frame_baixo, width=25, font=("", 15), relief="solid")
e_peso.place(x=14, y=120)

Label(frame_baixo, text="Altura (m)", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4).place(x=10, y=160)
e_altura = Entry(frame_baixo, width=25, font=("", 15), relief="solid")
e_altura.place(x=14, y=180)


botao_confirmar = Button(frame_baixo, text="Calcular IMC", width=39, height=2, bg=co2, fg=co5,
                         font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE, command=abrir_nova_janela)
botao_confirmar.place(x=15, y=240)

janela.mainloop()
