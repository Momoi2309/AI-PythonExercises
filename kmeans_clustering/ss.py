
import numpy as np
import random as rd


k=3   #Clusterele

p1=[45,85]
p2=[50,43]
p3=[40,80]
p4=[55,42]
p5=[200,43]
p6=[48,40]
p7=[195,41]
p8=[43,87]
p9=[190,40]

p=[]
p.append(p1)
p.append(p2)
p.append(p3)
p.append(p4)
p.append(p5)
p.append(p6)
p.append(p7)
p.append(p8)
p.append(p9)

centroizi=[]
cluster=[]

def aleator_centroizi(p , centroizi, k):
    for i in range(k):
        centroizi.append(p[rd.randint(0,8)])
    return centroizi

def d_puncte(p1,p2):
    return np.abs(p2[0]-p1[0])+np.abs(p2[1]-p1[1])

#Formarea clusterelor prin asignarea punctelor celor mai apropiaţi centroizi
def apartenenta(cluster , p  ,centroizi):
    for i in range(len(p)-1):
        dist=[]
        dist.append( d_puncte(p[i],centroizi[0]))
        dist.append(d_puncte(p[i],centroizi[1]))
        dist.append(d_puncte(p[i],centroizi[2]))
        if dist[0]==np.min(dist):
            cluster.append(0)
        elif dist[1]==np.min(dist):
            cluster.append(1)
        elif dist[2]==np.min(dist):
            cluster.append(2)
    return cluster


def centroid_recalc(centroizi,cluster):
    x1=0
    x2=0
    x3=0
    y1=0
    y2=0
    y3=0
    nr1=0
    nr2=0
    nr3=0
    for i in range(len(cluster)):
        if cluster[i]==0 :
            nr1=nr1+1
            x1=x1+p[i][0]
            y1=y1+p[i][1]
        elif cluster[i]==1:
            nr2=nr2+1
            x2=x2+p[i][0]
            y2=y2+p[i][1]
        elif cluster[i]==2:
            nr3=nr3+1
            x3=x3+p[i][0]
            y3=y3+p[i][1]
    c1=[x1/nr1,y1/nr1]
    c2=[x2/nr2,y2/nr2]
    c3=[x3/nr3,y3/nr3]
    centroid_nou =[]
    centroid_nou.append(c1)
    centroid_nou.append(c2)
    centroid_nou.append(c3)
    return centroid_nou

def k_mean(p,centroizi,k,cluster):
    cluster = apartenenta(cluster,p,centroizi)
    print ("\nCluser: ",cluster)        #punctele fiecarui cluster
    centroid_nou = centroid_recalc(centroizi,cluster)
    print ("Noii centroizi: ", centroid_nou)
    if centroizi != centroid_nou:
        cluster = []
        k_mean(p,centroid_nou,k,cluster)

centroizi = aleator_centroizi(p,centroizi,k)
print ("Centroizi: ", centroizi)
k_mean(p,centroizi,k,cluster)