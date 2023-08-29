import numpy as np

y = [[45, 85, -1],  # pattern-urile de instruire cu intrarea suplimentara -1
     [50, 43, -1],
     [40, 80, -1],
     [55, 42, -1],
     [200, 43, -1],
     [48, 40, -1],
     [195, 41, -1],
     [43, 87, -1],
     [190, 40, -1]]

max = 0
min = 99999

#y1,y2,...,y9
array = [[], [], [], [], [], [], [], [], []]
for data in y:
    for i in range(len(data) - 1):
        if data[i] > max:
            max = data[i]
        elif data[i] < min:
            min = data[i]
i = 0

for data in y:
    for val in range(len(data) - 1):
        array[i].append((data[val] - min) / (max - min))  # Scalarea val din setul de date
    array[i].append(-1)
    i = i + 1

d = [[1, -1, -1],  # Stabilim iesirile dorite
     [-1, 1, -1],
     [1, -1, -1],
     [-1, 1, -1],
     [-1, -1, 1],
     [-1, 1, -1],
     [-1, -1, 1],
     [1, -1, -1],
     [-1, -1, 1]]

d = np.array(d)
array = np.array(array)

w = 2 * np.random.random((3,3)) - 1  # Ponderile cu val aleaotoare din interval [-1,1] face o matrice de 3 pe 3 cu val intre 0 si 1. inmultesti cu 2 si o sa fie intre 0 si 2 si dupa scad 1 si o sa fie intre -1 si 1
K = 3  # Nr de perceptroni
c = 1  # Constanta de instruire
Emax = 0.0004  # Emax cu val cat mai mica
E = 0

def f(net):
    return ((2 / (1 + np.exp(-net))) - 1)  # Functia de activare a perceptronilor ( continua bipolara)


print("\nSe incepe algoritmul. Erorile calculate:")
while True:
    o = []
    for i in range(9):
        o.append(f(np.dot(w, array[i]))) ## pasul 2: se calculeaza iesirile fiecarui perceptron
    o = np.array(o)
    for p in range(0, len(array)): ## parcurg fiecare y (9)
        for j in range(0, len(o[0])): ## parcurg fiecare output perceptron(3) --j= indicilele perceptronului
            for i in range(0, len(array[0])): ## ponderile 3 corespunzatoare y urilor --i= indicele intrarii
                w[j, i] = w[j, i] + c * (d[p, j] - o[p][j]) * (1 - o[p][j] ** 2) * array[p, i]  # actualizam ponderile
    E = 0
    for p in range(0, len(array)):
        for i in range(0, len(d[0]) -2):
            E = E + (d[p, i] - o[p][i]) ** 2  # Calculam eroarea cumulata
    print("Eroarea:", E) ## printeaza erorile pana cand E devine o val mai mica decat EMAX
    if E < Emax:
        break

output = []
for i in range(9):
    output.append(f(np.dot(w, array[i])))
print('\n',output)

for i in range(len(output)): ## se parcurg cele 9 patternuri
    if np.sign(output[i][0]) == -1:
        if np.sign(output[i][1]) == -1:
            print("\nIesirea: ", output[i], "PAT")
        else:
            print("\nIesirea: ", output[i], "MASA")
    else:
        print("\nIesirea: ", output[i], "SCAUN")



