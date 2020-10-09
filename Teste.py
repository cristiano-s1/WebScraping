import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0. rv:11.0) like Gecko'}
page = requests.get("https://www.google.com.br/search?source=hp&ei=LLt_X8_xK7Gw5wLEwqzQCQ&q=previs%C3%A3o+do+tempo&oq=pre&gs_lcp=CgZwc3ktYWIQARgAMg0IABCxAxCDARBGEIACMggIABCxAxCDATIICAAQsQMQgwEyAggAMgUIABCxAzIICAAQsQMQgwEyBQguELEDMgUIABCxAzIICAAQsQMQgwEyAggAOggILhCxAxCDAToCCC5Q2AlYwgxgghxoAHAAeACAAdIBiAHHBJIBBTAuMi4xmAEAoAEBqgEHZ3dzLXdpeg&sclient=psy-ab", headers=headers)

pagina = BeautifulSoup(page.content, 'html.parser')


atributos = {'class':'g'}

local = pagina.find_all("div", class_="wob_loc mfMhoc vk_gy vk_h")[0]
tempo = pagina.find_all("span", class_="wob_t TVtOme")[0]
hora = pagina.find_all("div", class_="wob_dts vk_gy vk_sh")[0]
descricao = pagina.find_all("div", class_="vk_gy vk_sh")[0]


print(f"Local: {local.text} / {hora.text}")
print(f"Temperatura: {tempo.text}ºC")
print(descricao.text)

