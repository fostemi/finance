import pandas as pd
import pandas_datareader as web
import statistics
import io
import numpy as np
import matplotlib.pyplot as plt
from flask import send_file
plt.style.use('fivethirtyeight')

df_spy = web.DataReader('^GSPC', data_source = 'yahoo', start = '2020-01-01', end = '2021-01-01')

def visualize_data(underlying):
    plt.figure(figsize = (16,8))
    plt.title('Close History')
    plt.plot(underlying['Close'])
    plt.xlabel('Date', fontsize = 18)
    plt.ylabel('Close Price USD ($)', fontsize = 18)
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image
    
def target_stock(stock):
    return web.DataReader(stock, data_source = 'yahoo', start = '2020-01-01', end = '2021-01-01')

#Difference between volatility of spy and the chosen underlying
def vol_difference(stock, index, time):
    alpha = []
    for i in range(time):
        alpha.append([0])
    for i in range(len(stock)-time):
        z = (stock[i+time] - stock[i])/time
        a = (index[i+time] - index[i])/time
        alpha.append([z-a])
    return alpha

def visualize_vol(alpha):
    plt.figure(figsize = (16,8))
    plt.title('Volatility Between the Underlying and the Index')
    plt.plot(alpha)
    plt.xlabel('Date', fontsize = 18)
    plt.ylabel('Volatility of Difference', fontsize = 18)
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image
    
def outliers(alpha):
    arr = np.array(alpha)
    arr = arr.flatten()
    sd = statistics.stdev(arr)
    outliers = []
    positive_outlier_idx = []
    negative_outlier_idx = []
    for i in range(len(arr)):
        
        if not(arr[i] > sd or arr[i] < -sd):
            outliers.append(np.nan)
        
        if arr[i] > sd:
            outliers.append(arr[i])
            positive_outlier_idx.append(i)
        else:
            positive_outlier_idx.append(np.nan)
        
        if arr[i] < -sd:
            outliers.append(arr[i])
            negative_outlier_idx.append(i)
        else:
            negative_outlier_idx.append(np.nan)
            
    return (positive_outlier_idx, negative_outlier_idx)

def visualize_strategy(alpha,stock):
    outlier = []
    positive_outlier_idx, negative_outlier_idx = outliers(alpha)
    stock_price = []
    for i in range(len(stock)):
        stock_price.append([stock[i]])
    #Now plotting
    plt.figure(figsize = (16,8))
    plt.title('Volatility of Difference Vs. Stock Price')
    plt.plot(stock_price, alpha = .25)
    plt.scatter(positive_outlier_idx, stock_price[0:], label = 'Outlier', marker = 'X', color = 'Black')
    plt.scatter(negative_outlier_idx, stock_price[0:], label = 'Outlier', marker = 'X', color = 'Orange')
    plt.xlabel('Days', fontsize = 18)
    plt.ylabel('Volatility of Difference', fontsize = 18)
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image
    
def diff_volatility_strategy(arg1,arg2):
    visualize_data(df_spy)
    stock = target_stock(arg1)
    time = int(arg2)
    visualize_data(stock)
    calc_stock = pd.to_numeric(stock['Close'])
    calc_index = pd.to_numeric(df_spy['Close'])
    vd_alpha = vol_difference(calc_stock, calc_index, time)
    visualize_vol(vd_alpha)
    plot = visualize_strategy(vd_alpha, calc_stock)
    return send_file(plot, attachment_filename = 'plot.png', mimetype = 'image/png')