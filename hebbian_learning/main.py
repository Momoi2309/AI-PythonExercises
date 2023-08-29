import numpy as np
import math

##Invatarea hebbiana pentru un neuron care este instruit cu:

w1=np.array([1,-1]) #ponderea initiala

x1=np.array([1,-2]) #intrarile(multimea de vectori de intrare)
x2=np.array([0,1])
x3=np.array([2,3])
x4=np.array([1,-1])

c=1

## Pt inceput presupunem ca avem neuroni bipolari binari pt care
# functia de activare bipolara binara este :f(net)=sgn(net)

print('\n\nPasul 1. Se aplica x1:')
net1=np.dot(w1,x1)
print('net1:',net1)
w2=w1+np.sign(net1)*x1
print('w2:',w2)

print('\n\nPasul 2. Se aplica x2:')
net2=np.dot(w2,x2)
print('net2:',net2)
w3=w2+np.sign(net2)*x2
print('w3:',w3)

print('\n\nPasul 3. Se aplica x3:')
net3=np.dot(w3,x3)
print('net3:',net3)
w4=w3+np.sign(net3)*x3
print('w4:',w4)

print('\n\nPasul 4. Se aplica x4:')
net4=np.dot(w4,x4)
print('net4:',net4)
w5=w4+np.sign(net4)*x4
print('w5:',w5)

############ partea 2

print('\n\nPresupunem acum ca functia de activare este continua si bipolara.LAMDA=1')
## Functia de activare bipolara continua : f(net)=2/(1+exp^(-lamda*net)) -1 , lamda >0
print('\nPasul 1. Se aplica x1:')
print('net1:',net1)
f_net1=2/(1+math.exp(-net1))-1
print('f_net1:',f_net1)
print('Pornim din nou de la w1.')
w1=w1+f_net1*x1
print('w1:',w1)

print('\n\nPasul 2. Se aplica x2:')
print('net2:',net2)
f_net2=2/(1+math.exp(-net2))-1
print('f_net2:',f_net2)
w2=w2+f_net2*x2
print('w2:',w2)

print('\n\nPasul 3. Se aplica x3:')
print('net3:',net3)
f_net3=2/(1+math.exp(-net3))-1
print('f_net3:',f_net3)
w3=w3+f_net3*x3
print('w3:',w3)

print('\nPasul 4. Se aplica x4:')
print('net4:',net4)
f_net4=2/(1+math.exp(-net4))-1
print('f_net4:',f_net4)
w4=w4+f_net4*x4
print('w4:',w4)

##se observa ca pt functia de activare continua se obtin rezultate in aceeasi directie








