#Passo a passo do projeto
#Passo 1 - Entrar no sistema da empresa 
##https://dlp.hashtagtreinamentos.com/python/intensivao/login
##pip install pyautogui 

import pyautogui
import time

#clicar - pyautogui.click
#escrever - pyautogui.write
#apertar um tecla - pyautogui.press
#apertar - pyautogui.hotkey
#scroll - pyautogui.scroll

pyautogui.PAUSE = 1
#apertar a tecla do windows
pyautogui.press("win")
#digitar o nome do programa (chrome)
pyautogui.write("Chrome")
#apertar enter
pyautogui.press("enter")

#digitar o link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

#apertar entrer 
pyautogui.press("enter") 

#espera 15 segundos 
time.sleep(3)

#Passo 2 - Fazer login
pyautogui.click(x=804, y=466)

#digitar o e-mail
pyautogui.write("naominamie1@outlook.com")

#passar para o campo de senha
pyautogui.press("tab")

#digitar a senha
pyautogui.write("minhasenha123")

#apertar login
pyautogui.click(x=953, y=679)

#Passo 3 - Importar a base de dados
#pip install pandas numpy openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index: 
    #Passo 4 - Cadastrar um produto
    pyautogui.click(x=712, y=326)
    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    #tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"])) #"1"
    pyautogui.press("tab")
    #preco_unitario
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    #obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs): #se esse informação estiver vazia #if é uma condição
        pyautogui.write(obs)
    #enviar o produto
    pyautogui.press("tab")
    pyautogui.press("enter")
    #subir a pagina 
    pyautogui.scroll(5000)
#Passo 5 - Repetir isso até acabar a base de dados  
    
    