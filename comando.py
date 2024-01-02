

from tkinter import *
janela = Tk()

def quadrado (x):
    quadrado = x ** 2
    return quadrado


def quadrado_e_cubo (x):
    quadrado = x ** 2
    cubo = x ** 3
    return quadrado, cubo


print(quadrado(5))
print(quadrado_e_cubo(6))


janela.title('Primeira janela')


bt0 = Button(janela, text = '0',height= 4, width=5) 
bt1 = Button(janela, text = '1',height= 4, width=5)
bt2 = Button(janela, text = '2',height= 4, width=5)
bt3 = Button(janela, text = '3',height= 4, width=5)
bt4 = Button(janela, text = '4',height= 4, width=5)
bt5 = Button(janela, text = '5',height= 4, width=5)
bt6 = Button(janela, text = '6',height= 4, width=5)
bt7 = Button(janela, text = '7',height= 4, width=5)
bt8 = Button(janela, text = '8',height= 4, width=5)
bt9 = Button(janela, text = '9',height= 4, width=5)
btVirg = Button(janela, text = ',',height= 4, width=5)
btHz = Button(janela, text = 'Hz',height= 4, width=5)
btKhz = Button(janela, text = 'Khz',height= 4, width=5)
btMhz = Button(janela, text = 'Mhz',height= 4, width=5)


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




janela.geometry("400x400")
janela.mainloop()




janela.mainloop() 