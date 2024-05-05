import requests

class PesquisadorGoogle:
    def __init__(self):
        self.api_key = "AIzaSyCyQiOJkXnmGzdftz1zpXjSSBLHKrnDsrQ"
        self.cse_id = "3065b43a395fe445f"

    def buscar_snippets(self, query):
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "key": self.api_key,
            "cx": self.cse_id,
            "q": query,
        }
        response = requests.get(url, params=params)
        resultados = response.json()
        snippets = []
        if "items" in resultados:
            for item in resultados["items"]:
                snippets.append(item["snippet"])
        return snippets