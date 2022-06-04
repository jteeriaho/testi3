#!/usr/bin/env python
# coding: utf-8

# # Paraabeli interaktiivinen
# Piirtää paraabelin, tulostaa reaalijuuret ja huipun koordinaatit

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from math import sqrt

def tulosta(a,b,c):
    if b>0:
        v1='+'
    else:
        v1=''
    if c>0:
        v2='+'
    else:
        v2=''
    print('Paraabelin yhtälö: y = ',a,'x^2',v1,b,'x',v2,c)
    dk=b**2-4*a*c
    if dk<0:
        print('Juuret: ei reaalijuuria')
    elif dk==0:
        print('Juuret: kaksoisjuuri ',-b/(2*a))
    else:
        print('Juuret: kaksi reaalijuurta: ',round((-b-sqrt(dk))/(2*a),3),' ja ',round((-b+sqrt(dk))/(2*a),3))
    print('Paraabelin huippu: x =',-b/(2*a),' y =',c-b**2/(4*a))
    print('\n             Kuvaaja:')

def paraabeli(a:str, b:str,c:str):
    a1=int(a)
    b1=int(b)
    c1=int(c)
    x = np.linspace(-5, 5, 100)
    y = a1*x**2+b1*x + c1
    fig, ax = plt.subplots()
    ax.plot(x, y, 'r')
    ax.grid()
    ax.set_xlim([-5, 5])
    ax.set_ylim([-10, 10])
    ax.set_xlabel(r'$x$', loc='right')
    ax.set_ylabel(r'$y$', loc='top')
    tulosta(a1,b1,c1)
    
#paraabeli(2,3,-5)
print('Anna paraabelin kertoimet:')
widgets.interact(paraabeli,a='2',b='3',c='-5')

