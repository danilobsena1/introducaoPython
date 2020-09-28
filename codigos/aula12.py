import requests

response = requests.get("http://viacep.com.br/ws/22041001/json/")
print(response.status_code)
print(response.text)  #Imprime todo o texto da página.
print(response.json())  #Imprime em formato de dicionario
dados_cep = response.json()
print(dados_cep["logradouro"])
print(dados_cep["complemento"])
