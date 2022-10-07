def calculaPecas(pecas):
    valorPecas = 75 * int(pecas) + 125

    if (int(pecas) <= 5):
        valorPecas = 100 * int(pecas)

    maoDeObra = 400
    valorPecas = valorPecas + maoDeObra
    valorIron = valorPecas - maoDeObra
    return [valorPecas, maoDeObra, valorIron]
