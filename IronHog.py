import discord
from discord.ext import commands

from services.precos import retornaPrecosGeral
from services.sqlite import resetTabelaPreco, definePreco, colunaDeItems
from services.valueCalcultor import calculaPecas

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix='$')

##CALCULADORA DE PECAS
@bot.command()
async def reparo(self, pecas, item):

    if not pecas.isnumeric():
        await self.send('**PERMITIDO APENAS NÚMEROS**')

    if (int(pecas) < 0):
        await self.send('**PROIBIDO VALORES MENORES QUE ZERO**')

    elif (int(pecas) <= 100):
        if (item.upper() == 'A' or item.upper()  == 'B' or
            item.upper()  == 'C' or  item.upper()  == 'D' or  item.upper()  == 'M'):
            list = calculaPecas(pecas, item)
            maoDeObra = list[1]
            valorIron = list[2]
            valorServico = list[0]
            valorPeca = list[3]
            valor5Peca = list[4]
            await self.send('**Valor a ser cobrado: ** _$' + str(valorServico) + '_\n**Mão de Obra:** _$'
                            + str(maoDeObra) + '\n_**Iron Hog: **_$' + str(valorIron) + '_')
        else:
            await self.send('O item '+ item + ' não encontrado...')
    else:
        await self.send('**PROIBIDO VALORES MAIORES QUE 100**')


@reparo.error
async def reparo_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        print('erro')
        await ctx.send('**DIGITE O NUMERO DE PEÇAS E O TIPO.** _Exemplo: $pecas 10 M_')
    if isinstance(error, commands.CommandError):
        print(error)
################################################################
##TABELA DE PREÇOS
@bot.command()
async def precos(self):
    await self.send(retornaPrecosGeral())

################################################################

##RESETA O BANCO DE DADOS DO BOT
@bot.command()
async def reprecos(self):
    resetTabelaPreco()
    colunaDeItems()
    await self.send('***`TABELA DE PREÇOS RESETADA!`*** \n\n' + retornaPrecosGeral())

################################################################

################################################################
#muda os precos de um componente no SQL
@bot.command()
async def mudarpreco(self, item, preco):
    await self.send(definePreco(item, preco))

################################################################
#apresenta os comandos possiveis no bot
@bot.command()
async def comandos(self):
    await self.send(
                    "***COMANDOS***\n\n"
                    "`$reparo 'n.pecas' 'tipo peça'`\n"
                    "_Calcula e cadastra um reparo, tipos aceitos(A, B, C, D e M)._\n\n"
                    "`$precos`\n"
                    "_Mostra os preços das peças atuais._\n\n"
                    "`$reprecos`\n"
                    "_Reseta os preços da tabela de preços._\n\n"
                    "`$mudarpreco 'item' 'preço'`\n"
                    "_Muda os preços dos items, como Lockpick e peças._\n\n"
                    "`$listaitems`\n"
                    "_Lista de items que conseguem ser alteradas com o comando $mudarpreco._")

################################################################

@bot.command()
async def listaitems(self):
    await self.send(colunaDeItems())

bot.run('TOKEN')
