import requests
import time

while True:

    #Importa as cotações pela API
    cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacoes = cotacoes.json()

#Filtra os valores desejados em Dólar
    cotacaoDolar = cotacoes['USDBRL']['bid']
    valorMaxDolar = cotacoes['USDBRL']['high']
    valorMinDolar = cotacoes['USDBRL']['low']
    value_pay_dolar = '5.12'

# Filtra os valores desejados em Euro
    cotacaoEuro = cotacoes['EURBRL']['bid']
    valorMaxEuro = cotacoes['EURBRL']['high']
    valorMinEuro = cotacoes['EURBRL']['low']
    value_pay_euro ='6.196'
# Filtra os valores desejados em Bitcoin
    cotacaoBitcoin = cotacoes['BTCBRL']['bid']
    valorMaxBitcoin = cotacoes['BTCBRL']['high']
    valorMinBitcoin = cotacoes['BTCBRL']['low']
    value_pay_bitcoin = '190000'
    print('Dólar $:', cotacaoDolar,'R$ |', 'Euro €:',cotacaoEuro,'R$ |','BitCoin ₿:',valorMaxBitcoin,'R$')

    if (cotacaoDolar < value_pay_dolar):
        print ('O dólar chegou no valor desejado')
    if (cotacaoEuro < value_pay_euro):
        print('O Euro chegou no valor desejado')
    if (cotacaoEuro < value_pay_euro):
        print('A bitcoin chegou no valor desejado')
        
    time.sleep(2)



