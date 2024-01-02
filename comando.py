

from tkinter import *
janela = Tk()



def concatenar(): # Concatena valores digitatos nos botoes



    return


janela.title('Ajusta VFO')


bt0 =    Button(janela, text = '0',height= 4, width=5) 
bt1 =    Button(janela, text = '1',height= 4, width=5)
bt2 =    Button(janela, text = '2',height= 4, width=5)
bt3 =    Button(janela, text = '3',height= 4, width=5)
bt4 =    Button(janela, text = '4',height= 4, width=5)
bt5 =    Button(janela, text = '5',height= 4, width=5)
bt6 =    Button(janela, text = '6',height= 4, width=5)
bt7 =    Button(janela, text = '7',height= 4, width=5)
bt8 =    Button(janela, text = '8',height= 4, width=5)
bt9 =    Button(janela, text = '9',height= 4, width=5)
btVirg = Button(janela, text = ',',height= 4, width=5)
btHz =   Button(janela, text = 'Hz',height= 4, width=5)
btKhz =  Button(janela, text = 'Khz',height= 4, width=5)
btMhz =  Button(janela, text = 'Mhz',height= 4, width=5)

labelDig = Label(janela, text="Digitado:")
inDig = Entry(janela,width=30)

labelPorta = Label(janela, text="Porta Serial:")
portaSerial = Entry(janela,width=30)


bt7.grid(row = 0, column = 0, sticky = W, pady = 5)
bt8.grid(row = 0, column = 1, sticky = W, pady = 5)
bt9.grid(row = 0, column = 2, sticky = W, pady = 5)
btHz.grid(row = 0, column = 3, sticky = W, pady = 5)

bt4.grid(row = 1, column = 0, sticky = W, pady = 5)
bt5.grid(row = 1, column = 1, sticky = W, pady = 5)
bt6.grid(row = 1, column = 2, sticky = W, pady = 5)
btKhz.grid(row = 1, column = 3, sticky = W, pady = 5)

bt1.grid(row = 2, column = 0, sticky = W, pady = 5)
bt2.grid(row = 2, column = 1, sticky = W, pady = 5)
bt3.grid(row = 2, column = 2, sticky = W, pady = 5)
btMhz.grid(row = 2, column = 3, sticky = W, pady = 5)

bt0.grid(row = 3, column = 0, sticky = W, pady = 5)
btVirg.grid(row = 3, column = 1, sticky = W, pady = 5)


labelDig.grid(row = 4, column = 0, sticky = W, pady = 5)
inDig.grid(row = 4, column = 1, columnspan=100)

labelPorta.grid(row = 5, column = 0, sticky = W, pady = 5)
portaSerial.grid(row = 5, column = 1, columnspan=100)






janela.geometry("270x400")
janela.mainloop()




janela.mainloop() 