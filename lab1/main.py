import csv
import pandas as pd
import numpy as np

myList = []
with open(r"C:\Users\momoi\Desktop\FACULTATE\ANU III\INTELIGENTA ARTIFICIALA\Laboratoare\lab1\iris.data") as csvfile:
 readCSV = csv.reader (csvfile,delimiter=",")
 for row in readCSV:
  if len(row) == 5:
   myList.append([float(row[0]), float(row[1]), float(row[2]), float(row[3])])

   npArray = np.array(myList) ##convertesc intai MyList in numpy array


   ##PT PRIMA COLOANA (SEPAL LENGHT)
   col0_min = np.min(npArray[:, 0])  ##accesarea unei coloane prin index+slicing :,
   col0_max=np.max(npArray[:, 0])
   col0_mean=np.mean(npArray[:, 0])
   col0_median=np.median(npArray[:, 0])
   ##PT A DOUA COLOANA (SEPAL WIDTH)
   col1_min = np.min(npArray[:, 1])
   col1_max = np.max(npArray[:, 1])
   col1_mean = np.mean(npArray[:, 1])
   col1_median = np.median(npArray[:, 1])
   ##PT A TREIA COLOANA (PETAL LENGHT)
   col2_min = np.min(npArray[:, 2])
   col2_max = np.max(npArray[:, 2])
   col2_mean = np.mean(npArray[:, 2])
   col2_median = np.median(npArray[:, 2])
   ##PT A PATRA COLOANA (PETAL WIDTH)
   col3_min = np.min(npArray[:, 3])
   col3_max = np.max(npArray[:, 3])
   col3_mean = np.mean(npArray[:, 3])
   col3_median = np.median(npArray[:, 3])

print("\nValorile din prima coloana (LUNGIMEA SEPALEI): min:", col0_min, "max:", col0_max, "medie:", col0_mean,"mediana", col0_median)
print("\nValorile din a 2 a coloana (LATIMEA SEPALEI): min:", col1_min, "max:", col1_max, "medie:", col1_mean,"mediana", col1_median)
print("\nValorile din a 3 a coloana(LUNGIMEA PETALEI): min:", col2_min, "max:", col2_max, "medie:", col2_mean,"mediana", col2_median)
print("\nValorile din a 4 a coloana(LATIMEA PETALEI: min:", col3_min, "max:", col3_max, "medie:", col3_mean,"mediana", col3_median)

print("\nNormalizarea valorilor de pe fiecare coloana folosind formula x_norm=(x-min)/(max-min):\n")
col0_norm = (npArray[:, 0]-min(npArray[:, 0])) / (max(npArray[:, 0]) -min(npArray[:, 0]))
print(col0_norm)
col1_norm = (npArray[:, 1]-min(npArray[:, 1])) / (max(npArray[:, 1]) -min(npArray[:, 1]))
#print(col1_norm)
col2_norm = (npArray[:, 2]-min(npArray[:, 2])) / (max(npArray[:, 2]) -min(npArray[:, 2]))
#print(col2_norm)
col3_norm = (npArray[:, 3]-min(npArray[:, 3])) / (max(npArray[:, 3]) -min(npArray[:, 3]))
#print(col3_norm)



# suma_col0=np.sum(npArray[0,:])
# print(suma_col0)

ponderi=[] ##lista
for i in npArray:
  ponderi.append(0.2*i[0]+1.1*i[1]+(-0.9)*i[2]+1*i[3])     ## append cu un item la sfarsitul listei
ponderi=np.array(ponderi).reshape(len(ponderi),1)          ##reshape (nr randuri,nr coloane) - 150,1
npArray=np.append(npArray,ponderi,axis=1)                  ##axis=1 append pt coloana noua (axis=0 append pt rand nou)
print("\nBaza de date finala:\n",npArray)
print("\n Setul Iris are :",len(col0_norm),"randuri")







# #    irix = pd.read_csv(r"C:\Users\momoi\Desktop\iris.data")
# #    print(irix)
#
# data=pd.read_csv(r"C:\Users\momoi\Desktop\iris.data")
# #print(data.head()) ## display la primele 5 randuri (functia are default value 5)
# #print(data.sample(10))  ##ia 10 valori random de randuri
# # print(data)
# print("\nData-setul IRIS este format din :",data.shape,"(nr.randuri, nr coloane)")
#
# # sliced_data = data[10:21]
# # print(sliced_data)
#



