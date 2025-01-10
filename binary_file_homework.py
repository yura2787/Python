import requests

url_pdf = 'https://shron1.chtyvo.org.ua/Falkovych_Hryhorii/Smyk-tyndyk.pdf?PHPSESSID=9qogt2ec4dbq4ihc8bc7fu2p26'

response = requests.get(url_pdf)

pdf_content = response.content

with open('book.pdf', mode='bw') as file:
    file.write(pdf_content)
