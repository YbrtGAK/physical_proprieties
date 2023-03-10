"""************************************************************************
                              Solid proprieties
************************************************************************"""    
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                             Aluminium proprieties
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Range : 20 to 659.85 °C
rho_s_aluminium = lambda T : 2697.6 + 0.0282*T -2*10**(-4)*T**2 # [kg/m3]
cp_s_aluminium = lambda T : 788.95 + 0.3162*T # [J/kg/°C]
lambda_s_aluminum = lambda T : 196.91 + 0.2456*T + -4*10**(-4)*T**2 + 2*10**(-7)*T**3 # [W/m/K]