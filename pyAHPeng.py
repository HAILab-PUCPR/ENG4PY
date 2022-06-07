# PyAHPeng - Autor: Gustavo Riz - Pontifícia Universidade Católica do Paraná (PUCPR)
# Para utilizar este modelo, chame a função pyAHPeng, e envie como parâmetro o número de critérios
# É necessário criar uma pasta chamada "base" na estrutura do Python, e salvar o CSV com os dados
# Da avaliação do especialista (modelo multicritério) e indicadores coletados do paciente
import sys
import numpy as np
import csv

def pyAHPeng(numCriterios, modelMcdaName, patientId): #Esta função serve para chamar o pyAHPeng por parâmetro
    calcPesosModelo(numCriterios, modelMcdaName)  # Chama a função de cálculo dos pesos do modelo multicritério
    calcPesosPaciente(numCriterios, patientId)  # Chama a função de cálculo dos pesos dos indicadores do paciente
    prioridades = calcPrioridades(numCriterios, modelMcdaName)  # Chama a função de cálculo dos pesos de prioridade
    valor = calcEngajamento(numCriterios, prioridades, patientId)  # Calcula o Engajamento do Paciente

    # Retorna com o nível do engajamento obtido
    return(valor)

def main(): #Módulo principal
    return("pyAHPeng")

def calcPesosModelo(criterios, modelMcdaName): #Calculo dos pesos do modelo avaliado pelo especialista
    x = criterios
    rCsv = []
    # Importa o arquivo CSV com o modelo multicritério
    with open(modelMcdaName, 'rt', encoding='utf-8-sig') as ficheiro:
        reader = csv.reader(ficheiro, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        try:
            for linha in reader:
                rCsv.append(linha)
        except csv.Error as e:
            sys.exit('ficheiro %s, linha %d: %s' % (ficheiro, reader.line_num, e))

    nCsv = np.asarray(rCsv, dtype=np.float32)

    # Realiza o cálculo da matriz
    for i in range(x):
        nCsv[i, i] = 1
        for j in range(i + 1, x, 1):
            nCsv[j, i] = 1 / nCsv[i, j]

    # Grava o resultado em um arquivo CSV
    with open(modelMcdaName, "w", encoding="utf-8-sig") as csv_file:
        writer = csv.writer(csv_file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        writer.writerows(nCsv)


def calcPesosPaciente(criterios, patientId): #Calculo dos pesos do modelo avaliado pelo especialista
    x = criterios
    rCsv = []
    # Importa o arquivo CSV com o modelo multicritério
    with open('static/base/Result/' + patientId + '.csv', 'rt', encoding='utf-8-sig') as ficheiro:
        reader = csv.reader(ficheiro, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        try:
            for linha in reader:
                rCsv.append(linha)
        except csv.Error as e:
            sys.exit('ficheiro %s, linha %d: %s' % (ficheiro, reader.line_num, e))

    nCsv = np.asarray(rCsv, dtype=np.float32)

    # Realiza o cálculo da matriz
    j = 0
    for i in range(0, x * 3, 3):
        nCsv[i, j] = 1
        nCsv[i + 1, j + 1] = 1
        nCsv[i + 2, j + 2] = 1
        nCsv[i + 1, j] = 1 / nCsv[i, j + 1]
        nCsv[i + 2, j] = 1 / nCsv[i, j + 2]
        nCsv[i + 2, j + 1] = 1 / nCsv[i + 1, j + 2]

    # Grava o resultado no arquivo CSV
    with open('static/base/patients/' + patientId + '.csv', "w", encoding="utf-8-sig") as csv_file:
        writer = csv.writer(csv_file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        writer.writerows(nCsv)


def calcPrioridades(numCriterios, modelMcdaName): # Calcula o valor dos pesos de prioridade para cada critério
    # Calcula os níveis de prioridade
    x = numCriterios
    sumPri = np.zeros(x)
    pri = np.zeros((x, x))
    rCsv = []
    prioridades = [0, 0, 0, 0, 0, 0, 0, 0]
    # Importa o arquivo CSV com o modelo multicritério
    with open(modelMcdaName, 'rt', encoding='utf-8-sig') as ficheiro:
        reader = csv.reader(ficheiro, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        try:
            for linha in reader:
                rCsv.append(linha)
        except csv.Error as e:
            sys.exit('ficheiro %s, linha %d: %s' % (ficheiro, reader.line_num, e))

    nCsv = np.asarray(rCsv, dtype=np.float32)

    # Faz a soma para calculo das prioridades locais
    for i in range(x):
        for j in range(x):
            sumPri[i] = sumPri[i] + nCsv[j, i]

    # Calcula a matriz normalizada
    for i in range(x):
        for j in range(x):
            pri[j, i] = nCsv[j, i] / sumPri[i]

    # Calcula as prioridades locais
    for i in range(x):
        for j in range(x):
            prioridades[i] = prioridades[i] + pri[i, j]

    for i in range(x):
        prioridades[i] = prioridades[i] / x

    return (prioridades)


def calcEngajamento(numCriterios, prioridades, patientId): # Calcula o nível de engajamento do paciente
    # Carrega o peso avaliado para cada critério
    x = numCriterios # número de critérios
    y = 3 # número de linhas
    z = 4 # número de colunas
    cri = np.zeros((x, y, z))
    priori = [0, 0, 0]
    rCsv = []
    # Importa o arquivo CSV com o modelo multicritério
    with open('static/base/patients/' + patientId + '.csv', 'rt', encoding='utf-8-sig') as ficheiro:
        reader = csv.reader(ficheiro, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        try:
            for linha in reader:
                rCsv.append(linha)
        except csv.Error as e:
            sys.exit('ficheiro %s, linha %d: %s' % (ficheiro, reader.line_num, e))

    nCsv = np.asarray(rCsv, dtype=np.float32)

    # Atribui valores aos critérios
    lin = 0
    for i in range(8):
        for j in range(3):
            for k in range(3):
                cri[i, j, k] = nCsv[lin, k]
            lin = lin + 1

    # Calcula as prioridades de cada critério
    for i in range(8):
        for j in range(3):
            for k in range(3):
                cri[i, j, 3] = cri[i, j, 3] + (cri[i, j, k] / (cri[i, 0, k] + cri[i, 1, k] + cri[i, 2, k]))
            cri[i, j, 3] = cri[i, j, 3]/3

    # Calcula o nível de engajamento
    for i in range(8):
        for j in range(3):
            priori[j] = priori[j] + (cri[i, j, 3] * prioridades[i])

    return(priori)

if __name__ == '__main__':
    main()