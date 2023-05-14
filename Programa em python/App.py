from tkinter import *
from tkinter import ttk
from SGESD import Sgesd

root = Tk()
#textão
text_dc = """
Esse programa foi feito para calcular 
quantos BTUS são necessário 
por metros quadrados.
"""

#Classe orientada a objeto para o funcionamento da aplicação do programa
class Aplicantion(Sgesd):
    #Criador ou Construtor
    def __init__(self):
        #criando o objeto
        self.root = root
        self.tela()
        self.subtelas()
        self.widgets()
        self.widgets_2()
        root.mainloop()
    
    #Criando a tela principal da aplicação
    def tela(self):
        self.root.title("BTUS")
        self.root.configure(background = '#1e3743')
        self.root.geometry("1080x640")
        self.root.resizable(True, True)
        self.root.maxsize(width = 692, height = 504)
        self.root.minsize(width = 580, height = 420)
    
    #Criando subtelas ou frame
    def subtelas(self):
        #Primeira subtela localizada no lado esquerdo da aplicação
        self.subtela1 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground = 'black', highlightthickness = 3)
        self.subtela1.place(relx = 0.01, rely = 0.03, relheight = 0.95, relwidth = 0.48)
        
        self.subtela2 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground = 'black', highlightthickness = 3)
        self.subtela2.place(relx = 0.5, rely = 0.03, relheight = 0.95, relwidth = 0.49)
    
    #Saída de dados para a aplicação
    def output(self):
        #Label de BTUS
        self.label_btus = Label(self.subtela2, text= self.condicao() + "BTUS   ", bg= '#dfe3ee', fg= 'black', font=('Arial Black', 10)).place(relx= 0.65, rely=0.05)
        
        #Label de consumo de energia
        self.label_ce = Label(self.subtela2, text= self.output_consumo(), bg= '#dfe3ee', fg= 'black', font=('Arial Black', 10)).place(relx= 0.55, rely=0.20)      
        
        #Label de gasto mensal
        self.label_gm = Label(self.subtela2, text= self.output_gastos(),bg= '#dfe3ee', fg= 'black', font=('Arial Black', 10)).place(relx= 0.50, rely=0.35)
        
    #Widgets da subtela1   
    def widgets(self):
        #Tema
        self.tema = Label(self.subtela1, text= 'Calculadora de BTUS', bg= '#dfe3ee', fg= 'black', font=('Arial Black', 16, 'bold')).place(relx= 0.09, rely=0.05)
        
        #Descrição
        self.dc = Label(self.subtela1, text= text_dc, bg= '#dfe3ee', fg= 'black', font=('Arial', 12, 'bold')).place(relx= 0.05, rely=0.15)
        
        #Criando a label e entrada de dados da área do ambiente na subtela1
        self.label_area = Label(self.subtela1, text= "Qual a área do ambiente?", bg= '#dfe3ee', fg= 'black', font=('Arial', 10, 'bold')).place(relx= 0.20, rely=0.45)
        self.entry_area = Entry(self.subtela1)
        self.entry_area.place(relx=0.30, rely=0.50, relwidth=0.30)
        
        #Criando a label e entrada de dados(Combobox) para fazer a escolha da condição do sol sobre o ambiente
        self.sl = ['Sol o dia todo ou pela tarde', 'Sol de manhã', 'Sombra o dia todo']
        self.label_sol = Label(self.subtela1, text= "Quanto ao sol?", bg= '#dfe3ee', fg= 'black', font=('Arial', 10, 'bold')).place(relx= 0.20, rely=0.55)
        self.boxsol = ttk.Combobox(self.subtela1, values = self.sl)
        self.boxsol.place(relx=0.30, rely=0.60, relwidth=0.45)
        
        #Criando a label e entrada de dados(Combobox) para fazer a escolha do tipo de telhado/localização
        self.ll = ['Andar Térreo', 'Sob Telhado Convecional', 'Sob Laje', 'Andar Intermediário']
        self.label_local = Label(self.subtela1, text= "Onde está localizada a área?", bg= '#dfe3ee', fg= 'black', font=('Arial', 10, 'bold')).place(relx= 0.20, rely=0.65)
        self.boxlocal = ttk.Combobox(self.subtela1, values = self.ll)
        self.boxlocal.place(relx=0.30, rely=0.70, relwidth=0.45)

        #Botão para fazer o calculo
        self.button = Button(self.subtela1,text='Calcular', command= self.output)
        self.button.place(relx=0.30, rely=0.80, relwidth=0.30)
    
    #Widgets da subtela2
    def widgets_2(self):
        self.label_btus = Label(self.subtela2, text= 'Ar condicionado ideal é de ', bg= '#dfe3ee', fg= 'black', font=('Arial Black', 10)).place(relx= 0.05, rely=0.05)
        
        self.label_ce = Label(self.subtela2, text= 'Consumo de energia é de ', bg= '#dfe3ee', fg= 'black', font=('Arial Black', 10)).place(relx= 0.05, rely=0.20)      
        
        self.label_gm = Label(self.subtela2, text= 'Gasto mensal é de', bg= '#dfe3ee', fg= 'black', font=('Arial Black', 10)).place(relx= 0.05, rely=0.35)
        self.label_gma = Label(self.subtela2, text= '*gasto mensal 8h/dias', bg= '#dfe3ee', fg= 'Red', font=('Arial', 8)).place(relx= 0.05, rely=0.40)
   
#Colocando a classe pra funcionar          
Aplicantion()