import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def verdict(row, key):
    if(key == "Net"):
        if(row["Cumulative_Profit"] > 0):
            return "Profit"
        else:
            return "Loss"
    elif (key == "Solo"):
        if(row["Trade_Profit"] > 0):
            return "Profit"
        else:
            return "Loss"

transactions = pd.DataFrame({
    "Traded_Price" : np.random.uniform(20,30,10),
    "Traded_Shares" : np.random.choice( np.concatenate( [np.arange(-10,-1) , np.arange(1,10)] ) , size=10),
    "Valuation_Price" : np.random.uniform(20,30,10)
})
#traded shares is +ve when bought, cashflow is +ve when sold (individually)
transactions["NetCashFlow"] = transactions["Traded_Shares"] * transactions["Traded_Price"] * -1
transactions["Trade_Profit"] = transactions["NetCashFlow"] + transactions["Traded_Shares"]*transactions["Valuation_Price"]
transactions["Trade_verdict"] = transactions.apply(verdict, axis = 1, args=("Solo",))
transactions["Cumulative_Profit"] = transactions["Trade_Profit"].cumsum() #culumative
transactions["Cumulative_verdict"] = transactions.apply(verdict, axis = 1, args=("Net",))


valuation_price = 25
nt = transactions["Traded_Shares"].sum() 
nc = transactions["NetCashFlow"].sum()

profit = transactions["Trade_Profit"].sum()

print("Valuation Price : " , valuation_price)
print("Net Traded : ", nt )
print("Net CashFlow : " , nc)
print("Profit : ", profit)
print(transactions)

transactions.plot(y = ["Trade_Profit", "Cumulative_Profit"])
plt.show()
