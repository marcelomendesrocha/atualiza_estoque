import sys
from httpx import put


def atualiza_estoque():
    id_aplicativo = 0
    contador = 1

    if len(sys.argv) > 1:
        id_aplicativo = int(sys.argv[1])

    while True:
        response = atualiza_estoque_por_pagina(id_aplicativo, contador)

        total_de_paginas = response.get('total_de_paginas')

        print(f"pagina {contador} de {total_de_paginas}")

        contador += 1

        if total_de_paginas < contador:
            break


def atualiza_estoque_por_pagina(id_aplicativo, pagina):
    data = {
        'id_aplicativo': id_aplicativo,
        'pagina': pagina
    }

    response = put(
        'https://appdevi3-implantacao.azurewebsites.net/api/ProdutoIntegracao/EstoquePorPagina',
        json=data,
        timeout=None
    )

    if response.status_code == 200:
        return response.json()


atualiza_estoque()
