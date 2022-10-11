from services.sqlite import retornaPrecosItems

#retorna a tabela a de preços
def retornaPrecosGeral():
    return '***🧰 __PRECOS REPARO__ 🧰***\n' \
           '**🔩 UN. PECAS **\n**A:** $' \
           + retornaPrecosItems('pecaA') + \
           '\n**B:** $' \
           + retornaPrecosItems('pecaB') + \
           '\n**C:** $' \
           + retornaPrecosItems('pecaC') + \
           '\n**D:** $' \
           + retornaPrecosItems('pecaD') + \
           '\n**M:** $' \
           + retornaPrecosItems('pecaM') + \
           '\n**🔑 LOCKPICK NORMAL:** _$' \
           + retornaPrecosItems('lpNormal') + \
           ' ($' \
           + retornaPrecosItems('taxaLpNormal') + \
           ' clube)_\n' \
           '**🔐 LOCKPICK AVANÇADA:** _$'\
           + retornaPrecosItems('lpAvancada') +\
           ' ($'\
           + retornaPrecosItems('taxaLpAvancada') +\
           ' clube)_\n' \
           '\n***🚨 __EMERGENCIA__ 🚨***\n' \
           '**🧰 KIT REPARO:** _$400_\n' \
           '**🔨 KIT LATARIA:** _$600_\n' \
           '**💵 TAXA HOG:** _$1000_\n' \
           '**👨 MAO DE OBRA:** _$500_\n' \
           '**🛻 GUINCHO:** _$2000_'

