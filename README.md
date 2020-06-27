# Predicting-the-stock-market
In this project I have worked on with data from [S&P500 Index](https://en.wikipedia.org/wiki/S%26P_500_Index).
The S&P500 is a stock market index. 
<br/>
Some companies are publicly traded, which means that anyone can buy and sell their shares on the open market. A share entitles the owner to some control over the direction of the company, and to some percentage (or share) of the earnings of the company. When you buy or sell shares, it's common to say that you're trading a stock.
The price of a share is based mainly on supply and demand for a given stock. For example, Apple stock has a price of 120 dollars per share as of December 2015 -- [http://www.nasdaq.com/symbol/aapl](http://www.nasdaq.com/symbol/aapl).
A stock that is in less demand, like Ford Motor Company, has a lower price --[ http://finance.yahoo.com/q?s=F](http://finance.yahoo.com/q?s=F).
Stock price is also influenced by other factors, including the number of shares a company has issued
<br/>
Stocks are traded daily, and the price can rise or fall from the beginning of a trading day to the end based on demand. Stocks that are in more in demand, such as Apple, are traded more often than stocks of smaller companies.
<br/>
Indexes aggregate the prices of multiple stocks together, and allow you to see how the market as a whole is performing. For example, the [Dow Jones Industrial Average](https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average)
aggregates the stock prices of 30 large American companies together. The S&P500 Index aggregates the stock prices of 500 large companies. When an index fund goes up or down, you can say that the underlying market or sector it represents is also going up or down. For example, if the Dow Jones Industrial Average price goes down one day, you can say that American stocks overall went down (ie, most American stocks went down in price).
<br/>
I have used historical data on the price of the S&P500 Index to make predictions about future prices. Predicting whether an index will go up or down will help us forecast how the stock market as a whole will perform. Since stocks tend to correlate with how well the economy as a whole is performing, it can also help us make economic forecasts.
<br/>
There are also thousands of traders who make money by buying and selling [Exchange Traded Funds](https://en.wikipedia.org/wiki/Exchange-traded_fund). ETFs allow you to buy and sell indexes like stocks. This means that you could "buy" the S&P500 Index ETF when the price is low, and sell when it's high to make a profit. Creating a predictive model could allow traders to make money on the stock market.
<br/>
<br/>
In this project I have worked on a csv file containing index prices.  Each row in the file contains a daily record of the price of the S&P500 Index from 1950 to 2015. The dataset is stored in sphist.csv.
The model train on the data from 1950-2012 and make predictions from 2013-2015.
<br/>
Indicators used for training are:<br/>
* The average price from the past 5 days.
* The average price for the past 30 days.
* The average price for the past 365 days.
* The ratio between the average price for the past 5 days, and the average price for the past 365 days.
* The standard deviation of the price over the past 5 days.
* The standard deviation of the price over the past 365 days.
* The ratio between the standard deviation for the past 5 days, and the standard deviation for the past 365 days.
