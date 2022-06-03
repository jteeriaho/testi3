#!/usr/bin/env python
# coding: utf-8

# # Suora
# Suoran parametrit ovat kulmakerroin ja vakiotermi. Tutustutaan seuraavaksi miten nämä vaikuttavat suoran yhtälöön sekä suoran kuvaajaan:
# Klikkaa raketti-ikonia ja valitse 'Live Code'. Paina tämän jälkeen 'restart & run all'. Säädä liukusäätimiä käyttäen suoran parametreja, suoran kuvaaja sekä sen yläpuolella oleva suoran yhtälö (ratkaistu muoto) päivittyy automaattisesti.

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets


def tee_suoran_yhtälön_printtauksen_teksti(kulmakerroin, vakiotermi):
    if np.sign(kulmakerroin) > 0:
        kulmakertoimen_teksti = ''
    else:
        kulmakertoimen_teksti = '-'
    if np.abs(kulmakerroin) != 1:
        kulmakertoimen_teksti += str(np.abs(kulmakerroin))
    vakiotermin_teksti = ''
    if vakiotermi != 0:
        if np.sign(vakiotermi) > 0:
            vakiotermin_teksti += '+'
        else:
            vakiotermin_teksti += '-'
        vakiotermin_teksti += str(np.abs(vakiotermi))
    return 'y = {}x{}'.format(kulmakertoimen_teksti, vakiotermin_teksti)

def suoran_maaritys_ja_plottaus(kulmakerroin, vakiotermi):
    x = np.linspace(-5, 5, 100)
    y = kulmakerroin*x+vakiotermi
    fig, ax = plt.subplots()
    ax.plot(x, y, 'r')
    ax.grid()
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_xlabel(r'$x$', loc='right')
    ax.set_ylabel(r'$y$', loc='top')
    fig.suptitle(tee_suoran_yhtälön_printtauksen_teksti(kulmakerroin, vakiotermi))
    
    return kulmakerroin, vakiotermi

def suoran_maaritys_ja_plottaus_interaktiivisesti():
    interactive_plot = widgets.interactive(suoran_maaritys_ja_plottaus,
                                           kulmakerroin=widgets.FloatSlider(value=0.1, min=-5, max=5, step=0.1,
                                                                              description='kulmakerroin'),
                                           vakiotermi=widgets.FloatSlider(value=0.0, min=-5, max=5, step=0.1,
                                                                              description='vakiotermi'))
                                          
    return interactive_plot


# In[2]:


interactive_plot=suoran_maaritys_ja_plottaus_interaktiivisesti()
interactive_plot

