import numpy as np

#testa se a aproximacao bate com o resultado esperado
def testa(x, teste, resposta):
    sum = 0
    for i in range (0, len(teste)):
        sum = sum + x[i]*teste[i]
    aux = aproxima(sum)
    if(aux == resposta): return True
    else:
        print 'aproximacao: \"', sum, '\" -> \"', aux, '\" esperado: \"', resposta, '\"'
        return False

#le o dataset de determinado arquivo e monta a matriz e o vetor
def leDataset(arq, matriz, vetor, col):
    i = 0;
    f = open(arq, 'r')
    for line in f:
        y = line.split(',')
        vetor.append(convertIris(y[col]))
        for j in range (0, col):
            matriz[i][j] = y[j]
        i = i+1

#converte nome das flores para numero
def convertIris(name):
    if(name == "Iris-setosa\r\n"):
        return 1
    if(name == "Iris-versicolor\r\n"):
        return 2
    if(name == "Iris-virginica\r\n"):
        return 3

#converte numero das flores para nome
def convertIrisBack(number):
    if(number == 1):
        return "Iris-setosa"
    if(number == 2):
        return "Iris-versicolor"
    if(number == 3):
        return "Iris-virginica"

#ve de qual flor mais se aproxima
def aproxima(n):
    v = []
    v.append(abs(1-n))
    v.append(abs(2-n))
    v.append(abs(3-n))
    if(min(v) == v[0]):
        return 1;
    if(min(v) == v[1]):
        return 2;
    if(min(v) == v[2]):
        return 3;

#definicao da matriz A de dados sobre a flor e do vetor b de definicao
LIN, COL = 120, 4
A = np.zeros([LIN, COL])
b = []
leDataset('Iris80p.txt', A, b, COL)

#dados para teste
TAM1, TAM2 = 150, 4
T = np.zeros([TAM1, TAM2])
r = []
leDataset('IrisDataset.txt', T, r, TAM2)

#faz as contas
At = A.transpose()
AtA = np.dot(At, A)
Atb = np.dot(At, b)

#coeficientes da aproximacao linear com o erro quadrado minimo possivel
x = np.linalg.solve(AtA, Atb)
print(x)

for i in range(0, TAM1):
    if(testa(x, T[i], r[i])): print 'passou'
    else: print 'nao passou', convertIrisBack(r[i]), 'caso ', i
