"""
# ( número de peças, valor de peças < limite , valor de peças > limite)
def mult(pecas, vMin, vMax)
    limite=5 # até 5 peças vMin, depois vMax
    if pecas>limite:
        rMult= (limite*vMin)+((pecas-limite)*vMax)
    else:
        rMult= pecas*vMin
    return rMult
"""
def calculaPecas(pecas):
    """
    #valor das peças B C D e M primeiras (< limite) e ultimas (>limite) de forma que possa ser alterado nem q manualmente aqui no código
    
    valorBCDM_p=100 
    valorBCDM_u=75
    
    #valor das peças A primeiras (<limite) e ultimas (>limite) de forma que possa ser alterado nem q manualmente aqui no código
    
    valorA_p=350 
    valorA_u=300
    
    #Nesse modelo:
    # match identifica o tipo da peça, caso no futuro haja alteração individual só adicionar novas variaveis referentes
    match tipoPeca:
        case "A":
            valorPecas= mult(pecas,valorA_p,valorA_u)
        case "B":
        case "C":
        case "D":
        case "M":
            valorPecas= mult(pecas,valorBCDM_p,valorBCDM_u)
            
    Obs.: nesse modelo continua adicionando a mão de obra depois
    """
    
    valorPecas = 75 * int(pecas) + 125

    if (int(pecas) <= 5):
        valorPecas = 100 * int(pecas)

    maoDeObra = 400
    valorIron = valorPecas
    valorPecas = valorPecas + maoDeObra
    return [valorPecas, maoDeObra, valorIron]
