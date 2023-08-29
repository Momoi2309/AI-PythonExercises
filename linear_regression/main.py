import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\momoi\Desktop\FACULTATE\ANU III\INTELIGENTA ARTIFICIALA\Laboratoare\tema3\tema_regresia_liniara\Salary_Data.csv')
# data.shape
# data.describe()
plt.rcParams['figure.figsize'] = (15,5) ## parametrii pt afisarea figurii

X = data.iloc[:, 0] ## ia val de pe toate randurile prima coloana ( din excel)  -- pt x (years of experience)
Y = data.iloc[:, 1] ## ia val de pe toate randurile a 2 a coloana  -- pt y (salary)

n = len(data) #lungime
w1 = 0  # w1 = panta ec dreptei y=w1x+w2
prag1 = 1
w2 = 0
prag2 = 1
c = 0.01 ## constanta de invatare/rata de instruire
nr_epoci = 0
tresh = 0.00001

while ((prag1 > tresh) or (prag2 > tresh)):
    Y_pred = w1 * X + w2 ## ec dreptei de regresie
    deriv_w1 = (-1 / n) * sum(X * (Y - Y_pred))
    deriv_w2 = (-1 / n) * sum(Y - Y_pred)
    w1_copie = w1
    w2_copie = w2
    w1 = w1 - c * deriv_w1  # Actualizam parametrii
    w2 = w2 - c * deriv_w2
    prag1 = abs(w1 - w1_copie)
    prag2 = abs(w2 - w2_copie)
    nr_epoci = nr_epoci + 1

print('Nr de epoci:', nr_epoci)
print('Coeficientii estimati :\nw1 =', w1)
print('w2 =', w2)

plt.scatter(X, Y) ## scattered points graph
plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='blue') ##The data points are plotted along with a linear regression line
# naming the x axis
plt.xlabel('YearsExperience[x]')
# naming the y axis
plt.ylabel('Salary[y]')
#giving title to graph
plt.title('Regresie liniara')
# function to show the plot
plt.show()
print(n)
