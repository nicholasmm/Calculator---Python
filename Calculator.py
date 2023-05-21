##importanto a biblioteca Tkinter##

from tkinter import *
from tkinter import ttk

#cores
color1 =  "#1b1c1c" #black
color2 =  "#feffff" #white
color3 =  "#38576b" # blue charged
color4 =  "#ECEFF1" # grey
color5 =  "#FFAB40" #ORANGE



janela = Tk()
janela.title ("Calculator")
janela.geometry("318x450")
janela.config(bg= color1)

#separar tela que aparecerá os cálculos matemáticos do teclado numérico##
frame_tela = Frame(janela, width=318, height= 100, bg=color3)
frame_tela.grid(row=0, column= 0)
##--------------------------##

#parte do Numpad do app
Frame_numpad = Frame(janela, width=318, height= 350)
Frame_numpad.grid(row= 1, column= 0)

#VARIÁVEL QUE VAI CONTER TODOS OS VALORES DIGITADOS PELO NUMPAD##
todos_valores = ''

##lógica##

def entrar_valores(event):
    global todos_valores
    
    todos_valores = todos_valores + str(event)

    

    #sending value to screen#
    valor.set(todos_valores)

#Função para calcular o resultado

def calcular():
    global todos_valores

    resultado = eval(todos_valores)
    valor.set(str(resultado))


#função para atualizar a tela com o resultado

def limpa_tela():
    global todos_valores
    
    todos_valores = ''
    valor.set("")




#CRIANDO LABEL#
valor = StringVar()
app_label = Label(frame_tela, textvariable=valor, width=19, height=3, padx=6, relief=FLAT, anchor="e", justify= RIGHT, font=('Ivy 20 '), bg=color3, fg=color2)
app_label.place(x = 0, y = 0)



#botões Numpad#
b1 = Button(Frame_numpad, command= limpa_tela, text= "C", width=17, height=3, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x = 0, y = 0)

b2 = Button(Frame_numpad, command= lambda: entrar_valores('%'), text= "%", width=6, height=3, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x = 180, y = 0)

b3 = Button(Frame_numpad, command= lambda: entrar_valores('/'), text= "/", width=6, height=3, bg=color5, fg= color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b3.place(x = 249, y = 0)


b4 = Button(Frame_numpad, command= lambda: entrar_valores('9'), text= "9", width=6, height=3, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x = 180, y = 71)

b5 = Button(Frame_numpad, command= lambda: entrar_valores('8'), text= "8", width=7, height=3, bg=color4, fg= color1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x = 100, y = 71)

b7 = Button(Frame_numpad, command= lambda: entrar_valores('4'), text= "4", width=9, height=3, bg=color4, fg= color1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b7.place(x = 0, y = 142)

b8 = Button(Frame_numpad, command= lambda: entrar_valores('1'), text= "1", width=9, height=3, bg=color4, fg= color1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x = 0, y = 213)

b9 = Button(Frame_numpad, command= lambda: entrar_valores('7'),text= "7", width=9, height=3, bg=color4, fg= color1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x = 0, y = 71)

b10 = Button(Frame_numpad, command= lambda: entrar_valores('5'),text= "5", width=7, height=3, bg=color4, fg= color1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b10.place(x = 100, y = 142)

b11 = Button(Frame_numpad, command= lambda: entrar_valores('2'),text= "2", width=7, height=3, bg=color4, fg= color1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b11.place(x = 100, y = 213)

b12 = Button(Frame_numpad, command= lambda: entrar_valores('6'),text= "6", width=6, height=3, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b12.place(x = 180, y = 142)

b13 = Button(Frame_numpad, command= lambda: entrar_valores('3'),text= "3", width=6, height=3, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b13.place(x = 180, y = 213)

b14 = Button(Frame_numpad, command= lambda: entrar_valores('.'),text= ".", width=6, height=3, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b14.place(x = 180, y = 284)

b7 = Button(Frame_numpad, command= lambda: entrar_valores('*'),text= "*", width=6, height=3, bg=color5, fg= color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b7.place(x = 249, y = 71)

b15 = Button(Frame_numpad, command= lambda: entrar_valores('-'),text= "-", width=6, height=3, bg=color5, fg= color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b15.place(x = 249, y = 142)

b16 = Button(Frame_numpad, command= lambda: entrar_valores('+'),text= "+", width=6, height=3, bg=color5, fg= color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b16.place(x = 249, y = 213)

b17 = Button(Frame_numpad, command= calcular,text= "=", width=6, height=3, bg=color5, fg= color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b17.place(x = 249, y = 284)

b18 = Button(Frame_numpad, command= lambda: entrar_valores('0'),text= "0", width=17, height=3, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b18.place(x = 0, y = 284)





janela.mainloop()




