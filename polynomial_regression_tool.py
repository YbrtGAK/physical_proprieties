# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 15:45:16 2023

@author: Gravi
"""


import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

url = r'https://www.thermexcel.com/english/tables/eau_atm.htm'

def getPolynomFromThermExcel(url, degree):
    
    """Given a webpage's url of ThermExcel with a table, return the table and
    the physical proprieties """
    
    tables = pd.read_html(url) # Returns list of all tables on page
    table = tables[-1] # Select table of interest
    
    for i in range(0,len(table.iloc[0])) :
        table.iloc[0][i] += ' ' + '['+ table.iloc[1][i] + ']'
        
    table.drop(index=1,inplace=True)
    table.columns = table.iloc[0] ; table.drop(index=0, inplace=True)
    table = table.astype('float')
    try : table.set_index('Boiling point [°C]', inplace=True)
    except KeyError : 
        table.set_index((table.columns[0]), inplace=True)
        table.drop('Pressure [Pa]', axis=1, inplace=True)
    
    degree = 5
    M = []
    x = table.index.values
    ys = [table.iloc[:,i] for i in range(0, len(table.columns))]
    for y in ys :
        #specify degree of 3 for polynomial regression model
        #include bias=False means don't force y-intercept to equal zero
        poly = PolynomialFeatures(degree=degree, include_bias=False)
        
        #reshape data to work properly with sklearn
        poly_features = poly.fit_transform(y.index.values.reshape(-1, 1))
        
        #fit polynomial regression model
        poly_reg_model = LinearRegression()
        poly_reg_model.fit(poly_features, y.values)
        
        #use model to make predictions on response variable
        c = poly_reg_model.coef_ 
        
        #Create a function with the parameter values
        test = lambda T : c[0]*T + c[1]*T**2 + c[2]*T**3 + c[3]*T**4 + c[4]*T**5 
        Y = test(x)
        
        #Calculate the determination coefficient
        ymean = y.mean() #Mean of the real Y serie
        R2 = 1 - (sum((y - Y)**2))/(sum((y - ymean)**2))
        
        M.append([y.name, c, R2])
    
    return(table, M)
