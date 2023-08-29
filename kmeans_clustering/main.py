import numpy as np
import random as rd
import math

# r1=rd.randint(0,10)
# print('random nr bet 0 and 10:',r1)

k=3 ## K clustere

##Initializarea punctelor

P1=[45,85]
P2=[50,43]
P3=[40,80]
P4=[55,42]
P5=[200,43]
P6=[48,40]
P7=[195,41]
P8=[43,87]
P9=[190,40]

puncte=[]
puncte.append(P1)
puncte.append(P2)
puncte.append(P3)
puncte.append(P4)
puncte.append(P5)
puncte.append(P6)
puncte.append(P7)
puncte.append(P8)
puncte.append(P9)

centroizi=[]
cluster=[]

## Initializarea random a centroizilor
def rand_centroizi (puncte,centroizi,k):
    for i in range(k):
        centroizi.append(puncte[rd.randint(0,8)])
    return centroizi

##distanta dintre puncte
def distanta_p(P1,P2):
    return np.abs(P2[0] - P1[0]) + np.abs(P2[1] - P1[1])

#Formarea clusterelor prin asignarea pctelor celor mai apropiati centroizi
def asociere(cluster,puncte,centroizi):
    for i in range(len(puncte)): ## len puncte -1
        dist=[]
        dist.append(distanta_p(puncte[i],centroizi[0])) ##calc distanta de la fiecare punct la fiecare centroid
        dist.append(distanta_p(puncte[i], centroizi[1]))
        dist.append(distanta_p(puncte[i], centroizi[2]))
        if dist[0]==np.min(dist): ##daca prima distanta e minimul dintre toate distantele catre centroizi (de la primu punct)
            cluster.append(0) ## primu cluster
        elif dist[1]==np.min(dist):
            cluster.append(1)
        elif dist[2] == np.min(dist):
            cluster.append(2)
        ## i=i+1
    return cluster

def centroid_recalc(centroizi,cluster):
    x1=0 #toate x urile pctelor din fiecare cluster
    x2=0
    x3=0
    y1=0 #toate y urile pctelor din fiecare cluster
    y2=0
    y3=0
    nr1=0 #nr de pcte din fiecare cluster
    nr2=0
    nr3=0
    for i in range(len(cluster)):
        if cluster[i]==0: ## punctele din cluster asociate primului cluster
            nr1=nr1+1
            x1=x1+puncte[i][0]
            y1=y1+puncte[i][1]
        elif cluster[i]==1:
            nr2=nr2+1
            x2=x2+puncte[i][0]
            y2=y2+puncte[i][1]
        elif cluster[i]==2:
            nr3=nr3+1
            x3=x3+puncte[i][0]
            y3=y3+puncte[i][1]
    c1=[x1/nr1,y1/nr1] #recalcularea centroizilor pt fiecare clustere
    c2=[x2/nr2,y2/nr2]
    c3=[x3/nr3,y3/nr3]
    centroid_nou=[]
    centroid_nou.append(c1)
    centroid_nou.append(c2)
    centroid_nou.append(c3)
    return centroid_nou

def k_means(puncte,centroizi,k,cluster):
    cluster=asociere(cluster,puncte,centroizi)
    print('\nCluster: ',cluster)  #pctele fiecarui cluster
    centroid_nou=centroid_recalc(centroizi,cluster)
    print('Noii centroizi: ',centroid_nou)
    if centroizi != centroid_nou:
        cluster=[]
        k_means(puncte,centroid_nou,k,cluster)

centroizi=rand_centroizi(puncte,centroizi,k)
print('Centroizi: ',centroizi)
k_means(puncte,centroizi,k,cluster)
