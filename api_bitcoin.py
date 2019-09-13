import requests


#json_original = https://api.coindesk.com/v1/bpi/currentprice.json
#json_modificada com valor em Real(BR) = http://www.json-generator.com/api/json/get/bTwonkmGeW?indent=2

#end_point
url = 'http://www.json-generator.com/api/json/get/bUrNHrYVua?indent=2'

response = requests.get(url)
json = response.json()

#carregar json e salvar em valor.
valor = json ['bpi']['BR']['rate']

print('O valor atual do bitcoin é: R$' + valor)

#json criado em: http://www.json-generator.com.
