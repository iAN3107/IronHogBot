from services.sqlite import retornaPrecosItems

#calcula as peças para o requerente
def calculaPecas(pecas, item):
    try:
        maoDeObra = int(retornaPrecosItems('maoDeObra'))

        match item.upper():
            case 'A':
                item = 'pecaA'
            case 'B':
                item = 'pecaB'
            case 'C':
                item = 'pecaC'
            case 'D':
                item = 'pecaD'
            case 'M':
                item = 'pecaM'
            #case _:

        valorPeca = int(retornaPrecosItems(item))
        valor5Peca = int(retornaPrecosItems(str(item) + '5'))

        if int(pecas) <= 5:
            valorServico = valor5Peca * int(pecas) + maoDeObra
            valorIron = valorServico - maoDeObra
        elif(int(pecas) > 5):
            valorServico = valor5Peca * 5
            restoPecas = int(pecas) - 5
            valorServico = valorServico + (restoPecas * valorPeca) + maoDeObra
            valorIron = valorServico - maoDeObra

        return [valorServico, maoDeObra, valorIron, valorPeca, valor5Peca]

    except Exception as e:
        print('erro aqui' + str(e))
