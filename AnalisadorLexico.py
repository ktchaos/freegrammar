import nltk
from nltk.corpus import floresta
from nltk.tokenize import word_tokenize

class AnalisadorLexico:
    def __init__(self):
        # Baixar recursos necessários da NLTK
        nltk.download('floresta')
        nltk.download('punkt')

    # Função para ajustar as tags do corpus Floresta para o formato universal
    def simplify_tag(self, t):
        if "+" in t:
            return t[t.index("+")+1:]
        else:
            return t

    # Função para realizar a análise léxica
    def analise_lexica(self, texto):
        # Carregar o tagger baseado no corpus Floresta
        t0 = nltk.DefaultTagger('n')
        t1 = nltk.UnigramTagger(floresta.tagged_sents(), backoff=t0)
        t2 = nltk.BigramTagger(floresta.tagged_sents(), backoff=t1)

        tokens = word_tokenize(texto, language='portuguese')
        tagged = t2.tag(tokens)
        # Ajustar as tags para o formato simplificado
        tagged = [(word, self.simplify_tag(tag)) for word, tag in tagged]
        return tagged