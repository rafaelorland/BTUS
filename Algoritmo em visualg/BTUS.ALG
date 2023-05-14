algoritmo "BTUS"
// Disciplina   : [Linguagem e L�gica de Programa��o]  
// Fun��o : Ar Condicionado Ideal
// Autor : Rafael Orlando de Sousa Tavares
// Data : 26/04/2021
// Se��o de Declara��es
var
area:caracter
sol:caracter
local:caracter
inicio
// Se��o de Comandos
Escreval("QUAL A AREA DO AMBIENTE? ")
Escreval("1 - at� 9 metros quadrados")
Escreval("2 - 9 a 12 metros quadrados")
Escreval("3 - 12 a 15 metros quadrados")
Escreval("4 - 15 a 18 metros quadrados")
Leia (area)
Escreval("QUANTO AO SOL ")
Escreval("SD - Sol o dia todo ou pela Tarde")
Escreval("SM - Sol de Manh�")
Escreval("ST - Sombra o dia Todo")
Leia (sol)
Escreval("ONDE EST� LOCALIZADA A �REA A SER REFRIGERADA?")
Escreval("AT - Andar T�rreo")
Escreval("SC - Sob telhado Convencional")
Escreval("SL - Sob Laje")
Escreval("AI - Andar Intermedi�rio")
Leia (local)

// De 1 metros quadrados at� 9 metros quadrados
//Coluna 1
Se (area = "1") e (sol = "SD") e (local = "AT") Entao
Escreva("Ar condicionado ideal � de 7.500 Btus")
fimse
Se (area = "1") e (sol = "SM") e (local = "AT") Entao
Escreva("Ar condicionado ideal � de 7.500 Btus")
fimse
Se (area = "1") e (sol = "ST") e (local = "AT") Entao
Escreva("Ar condicionado ideal � de 7.500 Btus")
fimse
//Coluna 2
Se (area = "1") e (sol = "SD") e (local = "SC") Entao
Escreva("Ar condicionado ideal � de 7.500 Btus")
fimse
Se (area = "1") e (sol = "SM") e (local = "SC") Entao
Escreva("Ar condicionado ideal � de 7.500 Btus")
fimse
Se (area = "1") e (sol = "ST") e (local = "SC") Entao
Escreva("Ar condicionado ideal � de 7.500 Btus")
fimse
//Coluna 3
Se (area = "1") e (sol = "SD") e (local = "SL") Entao
Escreva("Ar condicionado ideal � de 7.500 Btus")
fimse
Se (area = "1") e (sol = "SM") e (local = "SL") Entao
Escreva("Ar condicionado ideal � de 7.500 Btus")
fimse
Se (area = "1") e (sol = "ST") e (local = "SL") Entao
Escreva("Ar condicionado ideal � de 7.500 Btus")
fimse
//Coluna 4
Se (area = "1") e (sol = "SD") e (local = "AI") Entao
Escreva("Ar condicionado ideal � de 7.500 Btus")
fimse
Se (area = "1") e (sol = "SM") e (local = "AI") Entao
Escreva("Ar condicionado ideal � de 7.500 Btus")
fimse
Se (area = "1") e (sol = "ST") e (local = "AI") Entao
Escreva("Ar condicionado ideal � de 7.500 Btus")
fimse
// De 9 metros quadrados at� 12 metros quadrados

//Coluna 1
Se (area = "2") e (sol = "SD") e (local = "AT") Entao
Escreva("Ar condicionado ideal � de 7.500 Btus")
fimse
Se (area = "2") e (sol = "SM") e (local = "AT") Entao
Escreva("Ar condicionado ideal � de 7.500 Btus")
fimse
Se (area = "2") e (sol = "ST") e (local = "AT") Entao
Escreva("Ar condicionado ideal � de 7.500 Btus")
fimse
//Coluna 2
Se (area = "2") e (sol = "SD") e (local = "SC") Entao
Escreva("Ar condicionado ideal � de 7.500 Btus")
fimse
Se (area = "2") e (sol = "SM") e (local = "SC") Entao
Escreva("Ar condicionado ideal � de 7.500 Btus")
fimse
Se (area = "2") e (sol = "ST") e (local = "SC") Entao
Escreva("Ar condicionado ideal � de 7.500 Btus")
fimse
//Coluna 3
Se (area = "2") e (sol = "SD") e (local = "SL") Entao
Escreva("Ar condicionado ideal � de 10.000 Btus")
fimse
Se (area = "2") e (sol = "SM") e (local = "SL") Entao
Escreva("Ar condicionado ideal � de 10.000 Btus")
fimse
Se (area = "2") e (sol = "ST") e (local = "SL") Entao
Escreva("Ar condicionado ideal � de 7.500 Btus")
fimse
//Coluna 4
Se (area = "2") e (sol = "SD") e (local = "AI") Entao
Escreva("Ar condicionado ideal � de 7.500 Btus")
fimse
Se (area = "2") e (sol = "SM") e (local = "AI") Entao
Escreva("Ar condicionado ideal � de 7.500 Btus")
fimse
Se (area = "2") e (sol = "ST") e (local = "AI") Entao
Escreva("Ar condicionado ideal � de 7.500 Btus")
fimse
// De 12 metros quadrados at� 15 metros quadrados
//Coluna 1
Se (area = "4") e (sol = "SD") e (local = "AT") Entao
Escreva("Ar condicionado ideal � de 7.500 Btus")
fimse
Se (area = "4") e (sol = "SM") e (local = "AT") Entao
Escreva("Ar condicionado ideal � de 7.500 Btus")
fimse
Se (area = "4") e (sol = "ST") e (local = "AT") Entao
Escreva("Ar condicionado ideal � de 7.500 Btus")
fimse
//Coluna 2
Se (area = "4") e (sol = "SD") e (local = "SC") Entao
Escreva("Ar condicionado ideal � de 10.000 Btus")
fimse
Se (area = "4") e (sol = "SM") e (local = "SC") Entao
Escreva("Ar condicionado ideal � de 10.000 Btus")
fimse
Se (area = "4") e (sol = "ST") e (local = "SC") Entao
Escreva("Ar condicionado ideal � de 7.500 Btus")
fimse
//Coluna 3
Se (area = "4") e (sol = "SD") e (local = "SL") Entao
Escreva("Ar condicionado ideal � de 12.000 Btus")
fimse
Se (area = "4") e (sol = "SM") e (local = "SL") Entao
Escreva("Ar condicionado ideal � de 10.000 Btus")
fimse
Se (area = "4") e (sol = "ST") e (local = "SL") Entao
Escreva("Ar condicionado ideal � de 10.000 Btus")
fimse
//Coluna 4
Se (area = "4") e (sol = "SD") e (local = "AI") Entao
Escreva("Ar condicionado ideal � de 10.000 Btus")
fimse
Se (area = "4") e (sol = "SM") e (local = "AI") Entao
Escreva("Ar condicionado ideal � de 10.000 Btus")
fimse
Se (area = "4") e (sol = "ST") e (local = "AI") Entao
Escreva("Ar condicionado ideal � de 10.000 Btus")
fimse

fimalgoritmo