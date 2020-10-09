# Biblioteca para traser dados de uma pagina na internet - pip install requests
# Biblioteca para .....- pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0. rv:11.0) like Gecko'}  # Receber os dados do Navegador
page = requests.get("https://www.google.com.br/search?source=hp&ei=rqR_X9y3Gq-75OUP7YeLiAQ&q=dolar&oq=dolar&gs_lcp=CgZwc3ktYWIQAzIFCAAQsQMyBQgAELEDMgUIABCxAzIFCAAQsQMyBQgAELEDMgUIABCxAzIFCAAQsQMyBQgAELEDMgUIABCxAzIFCAAQsQM6CAgAELEDEIMBOggILhCxAxCDAToCCAA6AgguUOoLWNYZYLUaaAJwAHgAgAGHAYgBvASSAQMwLjWYAQCgAQGqAQdnd3Mtd2l6sAEA&sclient=psy-ab&ved=0ahUKEwjcxtr0lqbsAhWvHbkGHe3DAkEQ4dUDCAc&uact=5", headers=headers)

# print(page.content)

pagina = BeautifulSoup(page.content, 'html.parser') # Criando objeto

"""
atributos = {'class':'g'}  # Varlor da class da pagina
# respostas = pagina.find_all("div", class_="g") # Outro meio

respostas = pagina.find_all("div", attrs=atributos)
print(respostas[0].get_text())
"""

# span class = DFlfde SwHCTb
atributos = {'class':'g'}

valor_dolar = pagina.find_all("span", class_="DFlfde SwHCTb")[0]

print(valor_dolar)
print(valor_dolar.text)
print(valor_dolar["data-value"])