# Dados do desmatamento anual por estado, fornecidos pelo PRODES (INPE)
desmatamentoAnualAmazoniaLegalPorEstadokm2 = {
    'AC': {
        '2004': '728',
        '2005': '592',
        '2006': '398',
        '2007': '184',
        '2008': '254',
        '2009': '167',
        '2010': '259',
        '2011': '280',
        '2012': '305',
        '2013': '221',
        '2014': '309',
        '2015': '264',
        '2016': '372',
        '2017': '257',
        '2018': '444',
        '2019': '682',
        '2020': '706'
    },
    'AM': {
        '2004': '1232',
        '2005': '755',
        '2006': '788',
        '2007': '610',
        '2008': '604',
        '2009': '405',
        '2010': '595',
        '2011': '502',
        '2012': '523',
        '2013': '583',
        '2014': '500',
        '2015': '712',
        '2016': '1129',
        '2017': '1001',
        '2018': '1045',
        '2019': '1434',
        '2020': '706'
    },
    'AP': {
        '2004': '46',
        '2005': '33',
        '2006': '30',
        '2007': '39',
        '2008': '100',
        '2009': '70',
        '2010': '53',
        '2011': '66',
        '2012': '27',
        '2013': '23',
        '2014': '31',
        '2015': '25',
        '2016': '17',
        '2017': '24',
        '2018': '24',
        '2019': '32',
        '2020': '24'
    },
    'MA': {
        '2004': '755',
        '2005': '922',
        '2006': '674',
        '2007': '631',
        '2008': '1271',
        '2009': '828',
        '2010': '712',
        '2011': '396',
        '2012': '269',
        '2013': '403',
        '2014': '257',
        '2015': '209',
        '2016': '258',
        '2017': '265',
        '2018': '253',
        '2019': '237',
        '2020': '336'
    },
    'MT': {
        '2004': '11814',
        '2005': '7145',
        '2006': '4333',
        '2007': '2678',
        '2008': '3258',
        '2009': '1049',
        '2010': '871',
        '2011': '1120',
        '2012': '757',
        '2013': '1139',
        '2014': '1075',
        '2015': '1601',
        '2016': '1489',
        '2017': '1561',
        '2018': '1490',
        '2019': '1702',
        '2020': '1779'
    },
    'PA': {
        '2004': '8870',
        '2005': '5899',
        '2006': '5659',
        '2007': '5526',
        '2008': '5607',
        '2009': '4281',
        '2010': '3770',
        '2011': '3008',
        '2012': '1741',
        '2013': '2346',
        '2014': '1887',
        '2015': '2153',
        '2016': '2989',
        '2017': '2433',
        '2018': '2744',
        '2019': '4172',
        '2020': '4899'
    },
    'RO': {
        '2004': '3858',
        '2005': '3244',
        '2006': '2049',
        '2007': '1611',
        '2008': '1136',
        '2009': '482',
        '2010': '435',
        '2011': '865',
        '2012': '773',
        '2013': '932',
        '2014': '684',
        '2015': '1030',
        '2016': '1376',
        '2017': '1243',
        '2018': '1316',
        '2019': '1257',
        '2020': '1273'
    },
    'RR': {
        '2004': '311',
        '2005': '133',
        '2006': '231',
        '2007': '309',
        '2008': '574',
        '2009': '121',
        '2010': '256',
        '2011': '141',
        '2012': '124',
        '2013': '170',
        '2014': '219',
        '2015': '156',
        '2016': '202',
        '2017': '132',
        '2018': '195',
        '2019': '590',
        '2020': '386'
    },
    'TO': {
        '2004': '158',
        '2005': '133',
        '2006': '124',
        '2007': '63',
        '2008': '107',
        '2009': '61',
        '2010': '49',
        '2011': '40',
        '2012': '52',
        '2013': '74',
        '2014': '50',
        '2015': '57',
        '2016': '58',
        '2017': '31',
        '2018': '25',
        '2019': '23',
        '2020': '25'
    }
}

# Função para gerar uma lista com os anos de desmatamento


def gerarListaDeAnos(desmatamentoAnualPorEstado):
    # Conjunto vazio, utilizado para separar os anos, sem repetição de valores
    conjuntoDeAnos = set()
    # Verificacao dos anos de desmatamento para cada estado
    for estado in desmatamentoAnualPorEstado:
        # Anos de desmatamento para um determinado estado
        anos = desmatamentoAnualPorEstado[estado].keys()
        for ano in anos:
            # Adicionando cada ano no conjunto
            conjuntoDeAnos.add(ano)
    # Lista vazia, utilizada para armazenar os anos de desmatamento
    listaDeAnos = []
    for ano in conjuntoDeAnos:
        # Inclusão de cada ano na lista
        listaDeAnos.append(ano)
    # Ordenação da lista, ordem crescente
    listaDeAnos.sort()
    return listaDeAnos


# Função para a informação numérica do dado sobre desmatamento
def separarNumero(dado):
    # Separação do texto em partes, pelo 'espaço'
    partes = dado.split(' ')
    # Retorno do valor numérico
    return int(partes[0])

# Função para selecionar os estados com os menores valores de desmatamento por ano


def menorDesmatamentoAnual(desmatamentoAnualPorEstado, anos):
    menorDesmatamentoAnual = {}
    # Verificação dos valores de desmatamento para cada ano
    for ano in anos:
        # Lista onde são armazenados os valores de desmatamentos por ano
        valoresDesmatamento = []
        for estado in desmatamentoAnualPorEstado:
            # Obtenção do valor de desmatamento para cada estado e ano específico
            valorDesmatamento = desmatamentoAnualPorEstado[estado][ano]
            # Inclusão do valor de desmatamento do ano específico na lista
            valoresDesmatamento.append(int(valorDesmatamento))
        # Ordenação da lista, ordem crescente
        valoresDesmatamento.sort()
        # Obtenção do menor valor de desmatamento para o ano específico
        menorValorDesmatamento = valoresDesmatamento[0]
        for estado in desmatamentoAnualPorEstado:
            # Valor de desmatamento para um estado e ano específico
            valorDesmatamentoAno = int(desmatamentoAnualPorEstado[estado][ano])
            # Comparação se o valor de desmatamento do ano é igual ao menor para o ano
            # se for, um dado é criado com esta informação, para registro
            if valorDesmatamentoAno == menorValorDesmatamento:
                dado = {
                    ano: {
                        estado: {
                            'valorDesmatamento': valorDesmatamento
                        }
                    }
                }
                # Inclusão do dado no dicionario final, dos menores valores de desmatamento por ano
                menorDesmatamentoAnual.update(dado)
    return menorDesmatamentoAnual


# Lista com os anos em ordem crescente
anos = gerarListaDeAnos(desmatamentoAnualAmazoniaLegalPorEstadokm2)
print(anos)

# Dicionario com os menores valores de desmatamento por ano
menoresDesmatamentosAnuais = menorDesmatamentoAnual(desmatamentoAnualAmazoniaLegalPorEstadokm2, anos)
print(menoresDesmatamentosAnuais)