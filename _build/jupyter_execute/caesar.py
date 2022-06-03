#!/usr/bin/env python
# coding: utf-8

# # Caesar salaus 

# In[1]:


import ipywidgets as widgets
from ipywidgets import interact

def f(viesti: str, avain: int):
    luvut=list(viesti.encode('ascii'))
    luvut=[((luku -97+avain)%26)+97 for luku in luvut ]
    salaus=[chr(luku) for luku in luvut]
    print("Viestin salakirjoitus on: "+''.join(salaus))  

interact(f,viesti="rovaniemi ", avain=widgets.IntSlider(value=5, min=0, max=25))


# In[ ]:




