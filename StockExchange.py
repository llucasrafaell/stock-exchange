import requests
import time
import json

from tkinter import *
janela = Tk()
janela.resizable(False, False)
janela.geometry('600x200')
janela['background'] = 'green'
janela.title('COTAÇÃO DÓLAR, EURO, BITCOIN')

while True:

    #Importa as cotações pela API
    cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacoes = cotacoes.json()

    #Filtra os valores desejados em Dólar
    cotacaoDolar = cotacoes['USDBRL']['bid']
    valorMaxDolar = cotacoes['USDBRL']['high']
    valorMinDolar = cotacoes['USDBRL']['low']

    # Filtra os valores desejados em Euro
    cotacaoEuro = cotacoes['EURBRL']['bid']
    valorMaxEuro = cotacoes['EURBRL']['high']
    valorMinEuro = cotacoes['EURBRL']['low']

    # Filtra os valores desejados em Bitcoin
    cotacaoBitcoin = cotacoes['BTCBRL']['bid']
    valorMaxBitcoin = cotacoes['BTCBRL']['high']
    valorMinBitcoin = cotacoes['BTCBRL']['low']

    #Imprime valores da cotação do Dólar na janela
    lbD = Label(janela, text='Dólar $ / Real R$', bg='lightgreen', fg = "black", font = "Helvetica 12 bold", width=20, height=1)
    lbDolar= Label(janela, text=cotacaoDolar, bg='lightgreen', fg = "black", font = "Helvetica 12 bold", width=20, height=1, command = time.sleep(2))
    lbVarDolar = Label(janela, text= ('Var Max', valorMaxDolar , 'Var Min' , valorMinDolar), bg='lightgreen', fg = "black", font = "Helvetica 8 bold italic", width=28, height=1)
    lbD.grid(row=0, column=0)
    lbDolar.grid(row=1, column=0)
    lbVarDolar.grid(row=2,column=0)

    # Imprime valores da cotação do Euro na janela
    lbE = Label(janela, text='Euro € / Real R$', bg='orange', fg = "black", font = "Helvetica 13 bold", width=18, height=1)
    lbEuro = Label(janela, text=cotacaoEuro, bg='orange', fg="black", font="Helvetica 13 bold", width=18, height=1, command = time.sleep(2))
    lbVarEuro = Label(janela, text=('Var Max', valorMaxEuro, 'Var Min', valorMinEuro), bg='orange', fg="black",font="Helvetica 8 bold italic", width=26, height=1)
    lbE.grid(row=0, column=1)
    lbEuro.grid(row=1, column=1)
    lbVarEuro.grid(row=2, column=1)

    # Imprime valores da cotação do Bitcoin na janela
    lbB = Label(janela, text='BitCoin ₿ / Real R$', bg='purple', fg = "black", font = "Helvetica 13 bold", width=18, height=1)
    lbBitcoin = Label(janela, text=cotacaoBitcoin, bg='purple', fg="black", font="Helvetica 13 bold", width=18, height=1, command = time.sleep(2))
    lbVarBitcoin = Label(janela, text=('Var Max', valorMaxBitcoin, 'Var Min', valorMinBitcoin), bg='purple', fg="black",font="Helvetica 8 bold italic", width=26, height=1)
    lbB.grid(row=0, column=2)
    lbBitcoin.grid(row=1, column=2)
    lbVarBitcoin.grid(row=2, column=2)

    print(cotacoes)
    janela.mainloop()
