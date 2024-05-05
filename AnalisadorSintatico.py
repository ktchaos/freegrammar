import nltk

class AnalisadorSintatico:
    def __init__(self):
        # Definir uma gramática simples
        grammar = """
        S -> NP VP Pont
        S -> S Conj S Pont
        S -> Interj S Pont
        S -> Q Pont
        NP -> Det N
        NP -> Det Adj N
        NP -> Det N PP
        NP -> Det N Adv
        NP -> Pron
        VP -> V
        VP -> V NP
        VP -> V NP PP
        VP -> V Adv
        VP -> Adv V
        VP -> Modal V
        PP -> P NP
        Q -> 'Quem' VP
        Q -> 'O que' VP
        Q -> 'Como' VP
        Q -> 'Por que' VP
        Q -> 'Quando' VP
        SubClause -> Conj S
        VP -> VP SubClause
        Det -> 'o' | 'a' | 'os' | 'as' | 'um' | 'uma' | 'uns' | 'umas' | 'O' | 'A' | 'Os' | 'As'
        N -> 'gato' | 'rato' | 'sopa' | 'queijo' | 'menino' | 'menina' | 'parque' | 'livro' | 'cidade' | 'carro'
        V -> 'comeu' | 'viu' | 'correu' | 'leu' | 'brincou' | 'estudou' | 'falou' | 'disse'
        P -> 'com' | 'de' | 'para' | 'sobre' | 'em' | 'por' | 'ante' | 'contra' | 'sem'
        Adj -> 'grande' | 'pequeno' | 'azul' | 'vermelho' | 'rápido' | 'lento' | 'novo' | 'velho'
        Adv -> 'rapidamente' | 'lentamente' | 'bem' | 'mal' | 'aqui' | 'lá'
        Conj -> 'e' | 'mas' | 'ou' | 'porque' | 'embora' | 'quando'
        Pron -> 'ele' | 'ela' | 'eles' | 'elas' | 'isso' | 'aquilo'
        Modal -> 'pode' | 'deve' | 'poderia' | 'deveria'
        Interj -> 'Olá' | 'Adeus' | 'Uau' | 'Oh'
        Pont -> '.' | ',' | '?' | '!'
        """
        # Compilar a gramática
        self.cfg = nltk.CFG.fromstring(grammar)
        # Criar um parser
        self.parser = nltk.ChartParser(self.cfg)

    def analise_sintatica(self, tokens):
        sentence = [token[0] for token in tokens]
        trees = list(self.parser.parse(sentence))
        if trees:  # Verificar se alguma árvore foi gerada
            for tree in trees:
                print(tree)  # Imprimir a árvore sintática
                tree.draw()  # Desenhar a árvore
        else:
            print("Nenhuma árvore sintática foi gerada. Verifique a gramática e a sentença.")