# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 10:45:58 2023

@author: Gravi
"""

"""Physical proprieties of matter function of thermodynamic variables (T,P)"""

"""************************************************************************
                              Liquid proprieties
************************************************************************"""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                            Boiling water proprieties
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Find the source, normally works for T included in 0 to 100 °C
rho_l_water = lambda T : 1001.1 - 0.0867*T - 0.0035*T**2 # [kg/m3]
cp_l_water = lambda T : 4.214*1000 - 2.286*T + \
    4.991*10**(-2)*T**2 - 4.519*10**(-4)*T**3 + 1.857*10**(-6)*T**4 # [J/kg/°C]
lambda_l_water = lambda : 0.598
    
