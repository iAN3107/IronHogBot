"""
def mult(pecas, vMin, vMax)
    if pecas>5:
        rMult= (5*vMin)+((pecas-5)*vMax)
    else:
        rMult= pecas*vMin
    return rMult
"""
def calculaPecas(pecas):
    """
    valor das peças B C D e M primeiras (<5) e ultimas (>5) de forma que possa ser alterado nem q manualmente aqui no código
    
    valorBCDM_p=100 
    valorBCDM_u=75
    
    valor das peças A primeiras (<5) e ultimas (>5) de forma que possa ser alterado nem q manualmente aqui no código
    
    valorA_p=350 
    valorA_u=300
    
    Nesse modelo:
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
    valorPecas = valorPecas + maoDeObra
    valorIron = valorPecas - maoDeObra
    return [valorPecas, maoDeObra, valorIron]
