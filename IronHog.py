import discord
from discord.ext import commands

from services.valueCalcultor import calculaPecas

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix='$')

##CALCULADORA DE PECAS
@bot.command()
async def reparo(self, message):

    if (int(message) < 0):
        await self.send('**PROIBIDO VALORES MENORES QUE ZERO**')

    elif (int(message) <= 100):
        list = calculaPecas(message)
        maoDeObra = list[1]
        valorIron = list[2]
        valorServico = list[0]
        await self.send('**Valor a ser cobrado:** _' + str(valorServico) + '_\n**Mão de Obra:** _' + str(maoDeObra) + '\n_**Iron Hog: **_' + str(valorIron) + '_')

    else:
        await self.send('**PROIBIDO VALORES MAIORES QUE 100**')
@reparo.error
async def reparo_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        print('erro')
        await ctx.send('Digite o número de peças!')

################################################################

##TABELA DE PREÇOS
@bot.command()
async def precos(self):
    await self.send('***🧰 __PRECOS REPARO__ 🧰***\n'
                    '**🔩 UN. PECAS _(B, C, D, M)_:** _$75_\n'
                    '**🔩 UN. PECAS _(A)_:** _$300_\n'
                    '**🔑 LOCKPICK NORMAL:** _$800-$700 (300 clube)_\n'
                    '**🔐 LOCKPICK AVANÇADA:** _$4200-$3500 (2000 clube)_\n'
                    '\n***🚨 __EMERGENCIA__ 🚨***\n'
                    '**🧰 KIT REPARO:** _$400_\n'
                    '**🔨 KIT LATARIA:** _$600_\n'
                    '**💵 TAXA HOG:** _$1000_\n'
                    '**👨 MAO DE OBRA:** _$500_\n'
                    '**🛻 GUINCHO:** _$2000_')

################################################################
bot.run('TOKEN')
