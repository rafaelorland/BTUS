# Sistema de Gerenciamento de entrada e saída de Dados

class Sgesd():
    #Transformando os dados em strings
    def variaveis(self):
        self.area = int(self.entry_area.get())
        self.sol = self.boxsol.get()
        self.local = self.boxlocal.get()
    
    def fatorar(self):
        #Função variável
        self.variaveis()
        
        #Sol, tranformando informação em número
        if self.sol == 'Sol o dia todo ou pela tarde':
            self.sol = 1
        if self.sol == 'Sol de manhã':
            self.sol = 2
        if self.sol == 'Sombra o dia todo':
            self.sol = 3
        #Local, tranformando informação em número
        if self.local == 'Andar Térreo':
            self.local = 1
        if self.local == 'Sob Telhado Convecional':
            self.local = 2
        if self.local == 'Sob Laje':
            self.local = 3
        if self.local == 'Andar Intermediário':
            self.local = 4

    # Condição para saber quantos BTUS são necessário para um ambiente
    def condicao(self):
        self.variaveis()
        self.fatorar()
        
        #Até 9m²
        if self.area <= 9:
            #Coluna 1
            if self.local == 1:
                if self.sol == 1:
                    btus = 7500
                if self.sol == 2:
                    btus = 7500
                if self.sol == 3:
                    btus = 7500
            #Coluna 2
            if self.local == 2:
                if self.sol == 1:
                    btus = 7500
                if self.sol == 2:
                    btus = 7500
                if self.sol == 3:
                    btus = 7500
            #Coluna 3
            if self.local == 3:
                if self.sol == 1:
                    btus = 7500
                if self.sol == 2:
                    btus = 7500
                if self.sol == 3:
                    btus = 7500
            #Coluna 4
            if self.local == 4:
                if self.sol == 1:
                    btus = 7500
                if self.sol == 2:
                    btus = 7500
                if self.sol == 3:
                    btus = 7500
        #Até 12m²                    
        elif self.area <= 12:
            #Coluna 1
            if self.local == 1:
                if self.sol == 1:
                    btus = 7500
                if self.sol == 2:
                    btus = 7500
                if self.sol == 3:
                    btus = 7500
            #Coluna 2
            if self.local == 2:
                if self.sol == 1:
                    btus = 7500
                if self.sol == 2:
                    btus = 7500
                if self.sol == 3:
                    btus = 10000
            #Coluna 3
            if self.local == 3:
                if self.sol == 1:
                    btus = 10000
                if self.sol == 2:
                    btus = 10000
                if self.sol == 3:
                    btus = 7500
            #Coluna 4
            if self.local == 4:
                if self.sol == 1:
                    btus = 7500
                if self.sol == 2:
                    btus = 7500
                if self.sol == 3:
                    btus = 7500
        #Até 15m²                    
        elif self.area <= 15:
            #Coluna 1
            if self.local == 1:
                if self.sol == 1:
                    btus = 7500
                if self.sol == 2:
                    btus = 7500
                if self.sol == 3:
                    btus = 7500
            #Coluna 2
            if self.local == 2:
                if self.sol == 1:
                    btus = 10000
                if self.sol == 2:
                    btus = 10000
                if self.sol == 3:
                    btus = 7500
            #Coluna 3
            if self.local == 3:
                if self.sol == 1:
                    btus = 12000
                if self.sol == 2:
                    btus = 10000
                if self.sol == 3:
                    btus = 10000
            #Coluna 4
            if self.local == 4:
                if self.sol == 1:
                    btus = 7500
                if self.sol == 2:
                    btus = 7500
                if self.sol == 3:
                    btus = 7500
        #Até 18m²
        elif self.area <= 18:
            #Coluna 1
            if self.local == 1:
                if self.sol == 1:
                    btus = 10000
                if self.sol == 2:
                    btus = 10000
                if self.sol == 3:
                    btus = 10000
            #Coluna 2
            if self.local == 2:
                if self.sol == 1:
                    btus = 12000
                if self.sol == 2:
                    btus = 10000
                if self.sol == 3:
                    btus = 10000
            #Coluna 3
            if self.local == 3:
                if self.sol == 1:
                    btus = 12000
                if self.sol == 2:
                    btus = 12000
                if self.sol == 3:
                    btus = 12000
            #Coluna 4
            if self.local == 4:
                if self.sol == 1:
                    btus = 10000
                if self.sol == 2:
                    btus = 10000
                if self.sol == 3:
                    btus = 10000
        #Error
        else:
            btus = 'Error   '
        
        #retornar     
        return str(btus)
    
    #Função de saída de dados/ Consumo
    def output_consumo(self):
        
        self.btus = self.condicao()
        if self.btus == '7500':
            self.consumo = '240kwh/mês'
        if self.btus == '10000':
            self.consumo = '324kwh/mês'
        if self.btus == '12000':
            self.consumo = '348kwh/mês'
        if self.btus == 'Error   ':
            self.consumo = 'Error    '
           
        return str(self.consumo)
    
     #Função de saída de dados/ Consumo
    def output_gastos(self):
        
        self.btus = self.condicao()
        if self.btus == '7500':
            self.gastos = 'R$ 184,55'
        if self.btus == '10000':
            self.gastos = 'R$ 249,15'
        if self.btus == '12000':
            self.gastos = 'R$ 267,60'
        if self.btus == 'Error   ':
            self.gastos = 'Error   '
    
        return str(self.gastos)    