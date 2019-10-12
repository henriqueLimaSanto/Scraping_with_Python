from urllib.request import  urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import  re

def getElementWEb(url):

    try:
        html = urlopen(url)
    except HTTPError as error:
        print("Erro HTTP :",error)
        return None
    except URLError as error:
        print("ocorreu um erro de Url ;",error)
        return None
    except AttributeError as error:
        print("Error",error)
        return  None
    except:
        print("Timeout Ocorreu um erro na pagina")

    try:
        bsObj = BeautifulSoup(html.read(),"html.parser")
        titulo = bsObj.html
        return titulo
    except:
        print("Ocorreu novo um erro no conteudo da pagina")
        return None




titulo = input("Informe a URL :")
palavra = input("Informe a palavra a ser procurada")

obj = getElementWEb(titulo)

word_re = re.compile(palavra,re.IGNORECASE)

word_All = re.findall(word_re,str(obj))
print(word_All)