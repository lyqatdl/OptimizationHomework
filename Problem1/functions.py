import numpy as np

def F(x):
    assert len(x)==500
    result=0
    for i in range(499):
        result+=(1-x[i])**2+100*(x[i+1]-x[i]**2)**2
        pass
    return result
def D(x):
    assert len(x)==500
    d=np.zeros(500)
    d[0]=2*(x[0]-1)-400*(x[1]-x[0]**2)*x[0]
    d[499]=200*x[499]
    for i in range(1,499):
        d[i]=2*(x[i]-1)-400*(x[i+1]-x[i]**2)*x[i]+200*x[i]
        pass
    return d

def armijo(xk, dk):
    m=dk.reshape(1,500).dot(D(xk).reshape(500,1))
    c=0.5;T=0.5
    t=-c*m
    alpha=100
    while F(xk)-F(xk+alpha*dk)<alpha*t:
        alpha=T*alpha
    return alpha


x0=np.zeros(500)
epsilon=1e-4
print(armijo(x0,np.ones(500)))
