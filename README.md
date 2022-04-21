# Simulating IPO Stock Data And Finding Optimal Entry/Exit Points

### Overview

IPOs, or Initial Public Offerings is the process of offering shares of a previously private corporation to the public. On the first 30 days, IPOs have high volatility and therefore, it is difficult to make decisions on when to enter and exit a market, or even enter the market at all. Simple python formulas that can be easily scaled up can be used to find the optimal entry/exit points within a 30 day investment horizon. Optimal entry/exit points are periods within an investment horizon that give the highest profit. 



🔗 Check the [source code](https://github.com/RishiHub-S/Simulating_Stock_Data/blob/main/StockDataV2.ipynb) of the program in this repository. The following details will be based on the code.


### Objective

The python program consists of two parts:

1. Generating Scalable Stock Data 
    1. Stock Name, Day, Corresponding Day’s Price.
2. Finding Entry/Exit Points that maximize profit.

### Assumptions:

1. One cannot exit without entering the market.
2. One cannot enter and exit on the same day.
3. The random prices created in the data is an attempt to replicate the random fluctuations of prices of the first few days of an IPO.

### Visuals:


1. Bar Graph showing the frequency of the optimal entry days.

    ![image](https://user-images.githubusercontent.com/86998121/163735833-84b7f8a0-389f-4066-b051-154ed655bc63.png)

 2. Bar Graph showing the frequency of the optimal exit days.

    ![image](https://user-images.githubusercontent.com/86998121/163735935-275f607b-62a1-4cc6-9a9d-d67e211f10d9.png)

3. Scatter Plot showing the frequency of the optimal entry and exit days. The bigger the dot, the higher the frequency.
    
    ![image](https://user-images.githubusercontent.com/86998121/163735979-2861ac24-27fd-436e-a618-a9b64ede0050.png)


### Analysis/Observations

When looking at the optimal entry/exit points found by the program:

1. Entry points are distributed evenly across the 30 day investment horizon. 
2. There was a higher frequency of exit points on the last days.


### Installation/Use

There are two ways to use the source code. The desktop version (full use of features) and web version (limited use of features).



1. Desktop (RECOMMENDED):
    
    a. Search up Anaconda Navigator and download the app.
    
    b. Open Jupyter Lab and upload the .ipynb file.
    
    c. Run the code.


2. Web Version: 
    
    a. Go to this link: https://jupyterlite.readthedocs.io/en/latest/_static/lab/index.html.
   
    b. Download the .ipynb file in the source code, and upload it to the workspace in the link.
    
    c. Run the code. If there is an error in the first cell of the code, copy paste the following in the first cell.
      ```
      import scipy as sp
      import numpy as np
      import pandas as pd
      #import seaborn as sns
      #import matplotlib.pyplot as plt
      ```
