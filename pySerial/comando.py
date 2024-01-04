

# Ainda nao estah terminado

# C:\ python -m pip install pyserial

import serial
import time
from tkinter import *
janela = Tk()



def concatenar(elemento): # Concatena valores digitatos nos botoes

    equacao = inDig.get() # Leitura do campo texto
    inDig.delete(0,END) # limpa o campo de texto
    inDig.insert(0,equacao + elemento) # concatena os numeros chegados e coloca no campo texto
  
def limpar():
    inDig.delete(0,END) # Limpa o campo texto

def hz():
    valorDig= inDig.get() #Leitura do campo texto
    fHz=float(valorDig) # conversao para float
    intHz= int(fHz)  # desconsidera a casa decimal
    serialCom("FREQ,"+str(intHz))

def khz():
    valorDig= inDig.get() #Leitura do campo texto
    fKHz=float(valorDig) # conversao para float
    fKHz=fKHz*1000 # escala Khz para Hz
    intKhz=int(fKHz) # desconsidera a casa decimal
    serialCom("FREQ,"+str(intKhz))

def mhz():
    valorDig= inDig.get() #Leitura do campo texto
    fMHz=float(valorDig) # conversao para float
    fMHz=fMHz*1000000 # escala Mhz para Hz
    intMhz=int(fMHz) # desconsidera a casa decimal
    serialCom("FREQ,"+str(intMhz))

def serialCom(msg):
    print(msg)
    porta= portaSerial.get()
    #SerialObj = serial.Serial(porta)
    #SerialObj.baudrate = 115200 # set Baud rate to 115200
    #SerialObj.bytesize = 8   # Number of data bits = 8
    #SerialObj.parity  ='N'   # No parity
    #SerialObj.stopbits = 1   # Number of Stop bits = 1
    #time.sleep(3)

    #SerialObj.close()      # Close the port


janela.title('Ajusta VFO SI5351')

fonte="Helvetica 10 bold"

#=======================Elementos da GUI=========================================

bt0 =       Button(janela,font=fonte,padx=50,pady=20, text = '0',relief="raised", command=lambda:concatenar("0")) # lambda para passar paramentro para a funcao
bt1 =       Button(janela,font=fonte,padx=50,pady=20, text = '1',relief="raised", command=lambda:concatenar("1")) # lambda para passar paramentro para a funcao
bt2 =       Button(janela,font=fonte,padx=50,pady=20, text = '2',relief="raised", command=lambda:concatenar("2")) # lambda para passar paramentro para a funcao
bt3 =       Button(janela,font=fonte,padx=50,pady=20, text = '3',relief="raised", command=lambda:concatenar("3")) # lambda para passar paramentro para a funcao
bt4 =       Button(janela,font=fonte,padx=50,pady=20, text = '4',relief="raised", command=lambda:concatenar("4")) # lambda para passar paramentro para a funcao
bt5 =       Button(janela,font=fonte,padx=50,pady=20, text = '5',relief="raised", command=lambda:concatenar("5")) # lambda para passar paramentro para a funcao
bt6 =       Button(janela,font=fonte,padx=50,pady=20, text = '6',relief="raised", command=lambda:concatenar("6")) # lambda para passar paramentro para a funcao
bt7 =       Button(janela,font=fonte,padx=50,pady=20, text = '7',relief="raised", command=lambda:concatenar("7")) # lambda para passar paramentro para a funcao
bt8 =       Button(janela,font=fonte,padx=50,pady=20, text = '8',relief="raised", command=lambda:concatenar("8")) # lambda para passar paramentro para a funcao
bt9 =       Button(janela,font=fonte,padx=50,pady=20, text = '9',relief="raised", command=lambda:concatenar("9")) # lambda para passar paramentro para a funcao
btVirg =    Button(janela,font=fonte,padx=50,pady=20, text = ',',relief="raised", command=lambda:concatenar(".")) # lambda para passar paramentro para a funcao
btHz =      Button(janela,font=fonte,padx=45,pady=20, text = 'Hz',relief="raised",command = hz) # chamada da funcao sem passar paramentro
btKhz =     Button(janela,font=fonte,padx=40,pady=20, text = 'Khz',relief="raised",command = khz) # chamada da funcao sem passar paramentro
btMhz =     Button(janela,font=fonte,padx=40,pady=20, text = 'Mhz',relief="raised",command = mhz) # chamada da funcao sem passar paramentro
btLimpar =  Button(janela,font=fonte,padx=40,pady=20, text = 'DEL',relief="raised", command = limpar) # chamada da funcao sem passar paramentro

labelDig = Label(janela, font=fonte, text="Digitado:")
inDig = Entry(janela,font=fonte,width=30)

labelPorta = Label(janela,font=fonte, text="Porta Serial:")
portaSerial = Entry(janela,font=fonte,width=30)

portaSerial.insert(0,"COM1")


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


labelDig.grid(row = 5, column = 0)
inDig.grid(row = 5,    column = 1)  # linha 4

labelPorta.grid(row = 6, column = 0)
portaSerial.grid(row = 6, column = 1)  # linha 5

janela.configure(bg='WHITE')
janela.geometry("580x400")
janela.resizable(False, False)
janela.mainloop()

