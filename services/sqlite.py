import sqlite3

con = sqlite3.connect("ironhog.db")
cur = con.cursor()
def resetTabelaPreco():
    cur.execute("DROP TABLE precos")
    cur.execute("CREATE TABLE precos(pecaA, pecaB, pecaC, pecaD, pecaM, lpNormal, lpAvancada, maoDeObra, "
                "taxaLpNormal, taxaLpAvancada, pecaA5, pecaB5, pecaC5, pecaD5, pecaM5)")
    cur.execute("INSERT INTO precos VALUES (300,75,75,75,75,800,3500,400,300,2000,350,100,100,100,100)")
    con.commit()

def retornaPrecosItems(item):

    if (item == 'pecaA' or item == 'pecaB' or item == 'pecaC' or item == 'pecaD'
          or item == 'pecaM' or item == 'lpNormal' or item == 'lpAvancada' or item == 'maoDeObra'
          or item =='taxaLpNormal' or item =='taxaLpAvancada' or item == 'pecaA5' or item == 'pecaB5'
          or item == 'pecaC5' or item == 'pecaD5' or item == 'pecaM5'):
        res = cur.execute('SELECT ' + item + ' from precos')
        valor = res.fetchone()[0]
        return str(valor)

def definePreco(item, preco):
    if not preco.isnumeric():
        return 'O preço precisa ser um número!'

    elif (item == 'pecaA' or item == 'pecaB' or item == 'pecaC' or item == 'pecaD'
            or item == 'pecaM' or item == 'lpNormal' or item == 'lpAvancada' or item == 'maoDeObra'
            or item =='taxaLpNormal' or item =='taxaLpAvancada' or item == '5pecaA' or item == '5pecaB'
            or item == '5pecaC' or item == '5pecaD'):

        cur.execute("UPDATE precos SET " + item + " = " + preco)
        return 'O preço do item ' + item + ' foi mudado para $' + preco
