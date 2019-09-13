import requests 

# definição do endereço servidor da api 
API_ENDPOINT = "http://pastebin.com/api/api_post.php"

# Chave de API gerada na sua conta do pastebin
API_KEY = "e7592e6e83d2324bb9b7065df9243976"

# código em python a ser inserido 
source_code = ''' 
print("Testando a api do pastebin") 
a = 10 * 2
print(a) 
'''

# dados a serem enviados para api 
dados = {'api_dev_key':API_KEY, 
		'api_option':'paste', 
		'api_paste_code':source_code, 
		'api_paste_format':'python'} 

# envia solicitação de postagem e salva a resposta 
r = requests.post(url = API_ENDPOINT, data = dados) 

# Texto de Resposta 
pastebin_url = r.text 
print("A url do pastebin é:%s"%pastebin_url) 
