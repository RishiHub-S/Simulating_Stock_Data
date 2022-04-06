# Simulating IPO Stock Data And Finding Optimal Entry/Exit Points

### Overview

IPOs, or Initial Public Offerings is the process of offering shares of a previously private corporation to the public. On the first 30 days, IPOs have high volatility and therefore, it is difficult to make decisions on when to enter and exit a market, or even enter the market at all. Simple python formulas that can be easily scaled up can be used to find the optimal entry/exit points within a 30 day investment horizon. Optimal entry/exit points are periods within an investment horizon that give the highest profit. 


```
🔗 Check the source code of the program in this repository. The following details will be based on the code.
```

### Objective

The python program consists of two parts:

1. Generating Scalable Stock Data 
    1. Stock Name, Day, Corresponding Day’s Price.
2. Finding Entry/Exit Points that maximize profit.

### Assumptions:

1. One cannot exit without entering the market.
2. One cannot enter and exit on the same day.
3. The random prices created in the data is an attempt to replicate the random fluctuations of prices of the first few days of an IPO.

### Analysis/Observations

When looking at the optimal entry/exit points found by the program:

1. Entry points are distributed evenly across the 30 day investment horizon. 
2. There was a higher frequency of exit points on the last days.
