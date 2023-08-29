#GRADIENT= derivata simultana pe mai multe dimensiuni ( x si/sau y)


############### EX 1 ################################
x_cur=3 #val de inceput random
c=0.01 #constanta
t=0.00001 #treshold (metoda gradientului:diferenta iteratiilor < t -->se gaseste minimul functiei)
i=0 #iteration counter
max_i=10000 #maxim de iteratii
dif=1

# print('\n\nPentru functia f(x)=6x^2-12x+1')
# def f(x):
#     return 6*pow(x,2)-12*x+1
#
# def deriv(x):
#     return 12*x-12
#
# print('Iteratia 0:')
# print('x curent:',x_cur)
# print('Minimul',f(x_cur))
#
# while dif >= t and i<max_i :
#     x_ant=x_cur
#     x_cur=x_cur - c*deriv(x_ant)
#     dif=abs(x_cur-x_ant)
#     i=i+1
#     print('\nIteratia',i,'\nX curent :',x_cur)
#     print('Minimul',f(x_cur))
#
# print('Minimul local la x=',x_cur)


################### EX 2 ################################
print('\n\nPentru functia g(x,y)= x^2 + 2*y^2')
def g(x,y):
    return pow(x,2)+2*pow(y,2)

def deriv1(x):
    return 2*x
def deriv2(y):
    return 4*y
#
x0=5
y0=5
c=0.01
t=0.00001
dif_x=1
dif_y=1


print('Iteratia 0:')
print('Minimul',x0)

x_ant = x0
y_ant = y0
x = x0 - c * deriv1(x0)
y = y0 - c * deriv2(y0)
i = 1
print('Iteratia 1:', '\n Minimul=', x)

while dif_x > t and dif_y>t and i<max_i :
    i=i+1
    x_anterior = x
    x = x - c * deriv1(x)
    y_anterior = y
    y = y - c * deriv2(y)
    dif_x=abs(x-x_ant)
    dif_y=abs(y-y_ant)
    print('\nIteratia',i,'\nX curent :',x)
    print('Minimul',x)

print('Minimul local la x=',x)

x0 = 5
y0 = 5
c = 0.01
t = 0.00001
i=0
i_max=10000

def grad(x0, y0, c, t):
    print("Iteratia 0:")
    print("Minimul", x0)
    x_anterior = x0
    y_anterior = y0
    x = x0 - c * deriv1(x0)  # x(n+1)= xn - c*deriv(xn)
    y = y0 - c * deriv2(y0)  # y(n+1)= yn - c*deriv(yn)
    i = 1 # pasul (index)
    print("Iteratia 1:")
    print("Minimul", x)
    while abs(x - x_anterior) >= t and abs(y - y_anterior) >= t and i<i_max:
        i = i + 1
        x_anterior = x
        x = x - c * deriv1(x)
        y_anterior = y
        y = y - c * deriv2(y)
        print("Iteratia", i, ":")
        print("Minimul", x)


##grad(x0, y0, c, t)

########################## EX 3 ##################################
print('\n\nPentru functia h(x,y)= (1-x)^2 + 100*(x-y^2)^2')
def  h(x,y):
    return pow(1-x,2)+100*pow(x-pow(y,2),2)
def deriv1(x,y): ## dupa x
    return 202*x - 200*pow(y,2)-2  ##202x-200*y^2-2
def deriv2(y,x): ## dupa y
    return 400*y*(pow(y,2)-x) ##400y(y^2-x)

x0=2
y0=2
c=0.01
t=0.00001
i=0
i_max=10000

def grad(x0, y0, c, t):
        print("Iteratia 0:") ###### PAS 0
        print("Minimul", x0)
        x_anterior = x0
        y_anterior = y0
        x = x0 - c * deriv1(x0,y0)  # x(n+1)= xn - c*deriv(xn)
        y = y0 - c * deriv2(y0,x0)  # y(n+1)= yn - c*deriv(yn)
        i = 1  # pasul (index)
        print("Iteratia 1:") ####### PAS 1
        print("Minimul", x)
        while abs(x - x_anterior) >= t and abs(y - y_anterior) >= t and i<i_max:
            i = i + 1
            x_anterior = x
            y_anterior = y
            x = x - c * deriv1(x,y)
            y = y - c * deriv2(y,x)
            print("Iteratia", i, ":")
            print("Minimul", x)

grad(x0,y0,c,t)



