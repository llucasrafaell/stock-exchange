import requests
import time
import json
while True:
    #Import quotes via API
    quotation = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    quotation = quotation.json()
    
    #Filter the desired values in Dollars
    quotation_dolar = quotation['USDBRL']['bid']
    value_pay_dolar = '5.12'
    #Filters the desired values in Euro
    quotation_euro = quotation['EURBRL']['bid']
    value_pay_euro ='6.196'
    #Filter the desired values in Bitcoin
    quotation_bitcoin = quotation['BTCBRL']['bid']
    value_pay_bitcoin = '190000' \
                        ''
    #Print desired values
    print('Dólar $:', quotation_dolar,'R$ |', 'Euro €:',quotation_euro,'R$ |','BitCoin ₿:',quotation_bitcoin,'R$')

    #Compare the values with the objective
    if (quotation_dolar < value_pay_dolar):
        print ('O dólar chegou no valor desejado')
    if (quotation_euro < value_pay_euro):
        print('O Euro chegou no valor desejado')
    if (quotation_bitcoin < value_pay_euro):
        print('A bitcoin chegou no valor desejado')

    time.sleep(2)



