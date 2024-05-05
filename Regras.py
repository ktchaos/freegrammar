
import spacy
import requests
from bs4 import BeautifulSoup

class Regras:
    def __init__(self):
        # Carregar o modelo de língua portuguesa do spaCy
        self.nlp = spacy.load("pt_core_news_sm")

    def buscar_sinonimos_dicio(self, palavra):
        url = f"https://www.dicio.com.br/{palavra}/"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        sinonimos = []
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            sinonimos_list = soup.find('p', class_='adicional sinonimos')
            if sinonimos_list:
                sinonimos = [sinonimo.get_text() for sinonimo in sinonimos_list.find_all('a')]
        return sinonimos

    def contexto_compativel(self, sinonimo, tag_original):
        # Criar uma frase de contexto simples com o sinônimo
        frase_teste = f"Este é um {sinonimo}."

        # Processar a frase de teste com o spaCy
        doc = self.nlp(frase_teste)

        # Encontrar o token que corresponde ao sinônimo na frase de teste
        # Aqui, assumimos que o sinônimo é o segundo token (índice 1), o que é verdade na frase de teste acima
        token_sinonimo = doc[3]  # 'Este é um [sinônimo].'

        # Converter a tag do spaCy para um formato simplificado, se necessário
        # Isso depende de como você está comparando as tags; aqui, usamos as tags do spaCy diretamente
        tag_sinonimo = token_sinonimo.pos_

        # Verificar se a tag do sinônimo é compatível com a tag original
        # Isso pode ser tão simples quanto uma comparação direta, ou mais complexo, dependendo do seu caso de uso
        return tag_sinonimo == tag_original

    def modificar_frase(self, frase):
        doc = self.nlp(frase)
        frase_modificada = []
        for token in doc:
            sinonimos = self.buscar_sinonimos_dicio(token.text)
            sinonimo_compativel = None
            for sinonimo in sinonimos:
                if self.contexto_compativel(sinonimo, token.pos_):
                    sinonimo_compativel = sinonimo
                    break
            # Se nenhum sinônimo compatível foi encontrado, use a palavra original
            palavra_substituta = sinonimo_compativel if sinonimo_compativel else token.text
            frase_modificada.append(palavra_substituta)
        return ' '.join(frase_modificada)