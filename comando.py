

# Ainda nao estah terminado

from tkinter import *
janela = Tk()



def concatenar(elemento): # Concatena valores digitatos nos botoes

    equacao = inDig.get() # Leitura do campo texto
    inDig.delete(0,END) # limpa o campo de texto
    inDig.insert(0,equacao + elemento) # concatena os numeros chegados e coloca no campo texto
  


def limpar():
    inDig.delete(0,END) # Limpa o campo texto

def hz():
    valorDig= inDig.get()

def khz():
    valorDig= inDig.get()

def mhz():
    valorDig= inDig.get()
    
   



janela.title('Ajusta VFO')

fonte_utilizada="Helvetica 10 bold"

#=======================Elementos da GUI=========================================

bt0 =       Button(janela,font=fonte_utilizada,padx=100,pady=20, text = '0', command=lambda:concatenar("0")) # lambda para passar paramentro para a funcao
bt1 =       Button(janela,font=fonte_utilizada,padx=100,pady=20, text = '1', command=lambda:concatenar("1")) # lambda para passar paramentro para a funcao
bt2 =       Button(janela,font=fonte_utilizada,padx=100,pady=20, text = '2', command=lambda:concatenar("2")) # lambda para passar paramentro para a funcao
bt3 =       Button(janela,font=fonte_utilizada,padx=100,pady=20, text = '3', command=lambda:concatenar("3")) # lambda para passar paramentro para a funcao
bt4 =       Button(janela,font=fonte_utilizada,padx=100,pady=20, text = '4', command=lambda:concatenar("4")) # lambda para passar paramentro para a funcao
bt5 =       Button(janela,font=fonte_utilizada,padx=100,pady=20, text = '5', command=lambda:concatenar("5")) # lambda para passar paramentro para a funcao
bt6 =       Button(janela,font=fonte_utilizada,padx=100,pady=20, text = '6', command=lambda:concatenar("6")) # lambda para passar paramentro para a funcao
bt7 =       Button(janela,font=fonte_utilizada,padx=100,pady=20, text = '7', command=lambda:concatenar("7")) # lambda para passar paramentro para a funcao
bt8 =       Button(janela,font=fonte_utilizada,padx=100,pady=20, text = '8', command=lambda:concatenar("8")) # lambda para passar paramentro para a funcao
bt9 =       Button(janela,font=fonte_utilizada,padx=100,pady=20, text = '9', command=lambda:concatenar("9")) # lambda para passar paramentro para a funcao
btVirg =    Button(janela,font=fonte_utilizada,padx=100,pady=20, text = ',', command=lambda:concatenar(".")) # lambda para passar paramentro para a funcao
btHz =      Button(janela,font=fonte_utilizada,padx=100,pady=20, text = 'Hz',command = hz) # chamada da funcao sem passar paramentro
btKhz =     Button(janela,font=fonte_utilizada,padx=100,pady=20, text = 'Khz',command = khz) # chamada da funcao sem passar paramentro
btMhz =     Button(janela,font=fonte_utilizada,padx=100,pady=20, text = 'Mhz',command = mhz) # chamada da funcao sem passar paramentro
btLimpar =  Button(janela,font=fonte_utilizada,padx=100,pady=20, text = 'Limpar', command = limpar) # chamada da funcao sem passar paramentro

labelDig = Label(janela, font=fonte_utilizada, text="Digitado:")
inDig = Entry(janela,font=fonte_utilizada,width=30)

labelPorta = Label(janela,font=fonte_utilizada, text="Porta Serial:")
portaSerial = Entry(janela,font=fonte_utilizada,width=30)

portaSerial.insert(0,"COM 1")


#=============Colocando componentes na grid===============================
bt7.grid(row = 0, column = 0)
bt8.grid(row = 0, column = 1) # linha 0
bt9.grid(row = 0, column = 2)
btHz.grid(row = 0, column = 3)

bt4.grid(row = 1, column = 0)
bt5.grid(row = 1, column = 1)  # linha 1
bt6.grid(row = 1, column = 2)
btKhz.grid(row = 1, column = 3)

bt1.grid(row = 2, column = 0)
bt2.grid(row = 2, column = 1)  # linha 2
bt3.grid(row = 2, column = 2)
btMhz.grid(row = 2, column = 3)

bt0.grid(row = 3, column = 0)
btVirg.grid(row = 3, column = 1)  # linha 3
btLimpar.grid(row = 3, column =2)


labelDig.grid(row = 4, column = 0)
inDig.grid(row = 4,    column = 1)  # linha 4

labelPorta.grid(row = 5, column = 0)
portaSerial.grid(row = 5, column = 1)  # linha 5


janela.geometry("940x400")
janela.mainloop()

janela.mainloop() 