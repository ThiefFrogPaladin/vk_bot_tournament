import math
'''
a1,a2,a3=0.07,-1/3,0.2
b1,b2,b3=-3.90132825389132, -0.52748620245725, 0.539925567459681
e=1e-13
def f(x):
    return 0.9*x**3+3.5*x**2-0.3*x-1
def iteration_method(xn,a,fe):
    xn1=xn+a*fe(xn)
    count=0
    while math.fabs(fe(xn1)) >= e and count<100:
        xn=xn1
        xn1=xn1-a*fe(xn1)
        count+=1
    print("итерация=",count, 'апостериорная оценка погрешности =',a/(1-a)*math.fabs(xn1-xn))
    return xn1
print ('1 root of the equation iteration_method for f(x) %s' % iteration_method(-4, a1, f))
print ('2 root of the equation iteration_method for f(x) %s' % iteration_method(-0.5, a2, f))
print ('3 root of the equation iteration_method for f(x) %s' % iteration_method(0.5, a3, f))
'''
a1,a2,a3=0.111,-1/3,0.2
b1,b2,b3=-3.90132825389132, -0.52748620245725, 0.539925567459681
e=1e-13
def f(x):
    return 0.9*x**3+3.5*x**2-0.3*x-1
def iteration_method(xn,a,fe,r):
    xn1=xn+a*fe(xn)
    razn1=abs(r-xn1)
    print(razn1/r*100,'razn')
    count=0
    while math.fabs(fe(xn1)) >= e and count<100:
        xn=xn1
        xn1=xn1-a*fe(xn1)
        razn2 = abs(r - xn1)
        print(razn2 / r * 100,'razn')
        print(razn1/razn2,'отношение')
        count+=1
        razn1=razn2
    print("итерация=",count, 'апостериорная оценка погрешности =',a/(1-a)*math.fabs(xn1-xn))
    return xn1
#print ('1 root of the equation iteration_method for f(x) %s' % iteration_method(-4, a1, f,-3.901328253891317))
#print ('2 root of the equation iteration_method for f(x) %s' % iteration_method(-0.5, a2, f,-0.5274862024572757))
print ('3 root of the equation iteration_method for f(x) %s' % iteration_method(0.5, a3, f,0.539925567459675))