import numpy as np

def convertSx(sx):
    if(sx == 'female'): return 0
    else: return 1

def convertRk(rk):
    if(rk == 'full'): return 0
    elif(rk == 'associate'): return 1
    else: return 2

def convertDg(dg):
    if(dg == 'masters'): return 0
    else: return 1

def convertSl(sl):
    return float(sl.rstrip())

#le o dataset de determinado arquivo e monta a matriz e o vetor
def leDataset(arq, matriz, vetor, col):
    i = 0;
    f = open(arq, 'r')
    for line in f:
        y = line.split(',')
        vetor.append((convertSl(y[col])))
        for j in range (0, col):
            if(j == 0):
                matriz[i][j] = convertSx(y[j])
            elif(j == 1):
                matriz[i][j] = convertRk(y[j])
            elif(j == 3):
                matriz[i][j] = convertDg(y[j])
            else:
                matriz[i][j] = y[j]
        i = i+1

#testa se a aproximacao bate com o resultado esperado
def testa(x, teste, resposta):
    sum = 0
    erroAceitavel = 4000
    for i in range (0, len(teste)):
        sum = sum + x[i]*teste[i]
    if(abs(sum-resposta) < erroAceitavel): return True
    else:
        print 'aproximacao:', sum, 'teve erro de: ', abs(sum-resposta),'que eh maior que o aceitavel'
        return False


#definicao da matriz A de dados sobre o salario e do vetor b do salario em si
LIN, COL = 52, 5
A = np.zeros([LIN, COL])
b = []
leDataset('DiscriminationInSalariesDataset.txt', A, b, COL)

#faz as contas
At = A.transpose()
AtA = np.dot(At, A)
Atb = np.dot(At, b)

#coeficientes da aproximacao linear com o erro quadrado minimo possivel
x = np.linalg.solve(AtA, Atb)
print(x)

soma = 0
for i in range(0, LIN):
    if(testa(x, A[i], b[i])): print 'passou'
    else:
        print 'nao passou caso ', i
        soma = soma+1
print 'qntd de casos que falharam:', soma
