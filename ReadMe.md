# Analysis of the Attractiveness of Different Securities
## Theory and Strategy 1: Difference in Volatilities of a Stock vs. it's Index
### Introduction:
Alpha is the risk relative to the market.  Extended trading funds find their alpha to see how they are doing against the market.  They look at their gains against the gains of the S&P 500 to give a value to their performance. The goal of this notebook is to find the difference of different popular stocks in the S&P 500 and find a correlation between the change of a stock price vs. it's index and the stock price.  For example, Tesla vs. S&P 500, how does the difference between the two mean about the stock?

### My Formula
Underlying Security Price: z
Overhead Index Price: i
My Formula: α = Δz/Δt - Δi/Δt

### Hypothesis:
Stock's with over inflated Alpha's are overextended and due for a recorrection.  A recorrection may be an increase or a decrease to a more median price with respect to the overhead index.

### Data And Analysis:
Follow the endpoints to see different stocks ran in the S&P 500.  

To run everything run the following command:
```
make docker-all
```
URL:
```
localhost:8080/finance
```
Graph of buying and selling when the difference of volatilities are high from 2020-2021:
```
localhost:8080/finance/myAlpha/strategy/stock/<arg1>/time/<arg2>
```
Graph of buying and selling when the difference of volatilites are high and low respectively from user input dates:
```
localhost:8080/finance/myAlpha/strategy/stock/<arg1>/time/<arg2>/start/<arg3>/end/<arg4>
```
The profits of using this strategy:
```
WIP
```

### Conclusion:
WIP