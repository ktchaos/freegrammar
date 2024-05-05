from AnalisadorLexico import AnalisadorLexico
from AnalisadorSintatico import AnalisadorSintatico
from Regras import Regras
from PesquisadorGoogle import PesquisadorGoogle

# Main -----
def main():
    # Solicita ao usuário que digite uma frase (claim)
    texto = input("Digite uma frase: ")

    # Realiza a análise léxica da
    analisadorLexico = AnalisadorLexico()
    tokens = analisadorLexico.analise_lexica(texto)

    # Realiza a análise sintática da frase
    analisadorSintatico = AnalisadorSintatico()
    analisadorSintatico.analise_sintatica(tokens)
    print("Análise Léxica:")
    print(tokens)
    print("----------------------------")

    # Modifica a frase com base nos sinônimos encontrados
    regras = Regras()
    frase_modificada = regras.modificar_frase(texto)
    print("Frase Original:")
    print(texto)
    print("Frase Modificada:")
    print(frase_modificada)

    # Realiza a pesquisa no Google com a frase original e exibe os snippets encontrados
    pesquisador = PesquisadorGoogle()
    snippets_frase_original = pesquisador.buscar_snippets(texto)
    print("\nSnippets encontrados na pesquisa do Google para FRASE ORIGINAL:")
    for snippet in snippets_frase_original:
        print(snippet)

    # Realiza a pesquisa no Google com a frase original e exibe os snippets encontrados
    snippets_frase_modificada = pesquisador.buscar_snippets(frase_modificada)
    print("\nSnippets encontrados na pesquisa do Google para FRASE MODIFICADA:")
    for snippet in snippets_frase_modificada:
        print(snippet)


main()