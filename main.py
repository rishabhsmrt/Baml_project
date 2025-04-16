from baml_client import b
#resume_info = b.ExtractResume(" What is the high price and low price for TCS and ongc.")

resume_info = b.ExtractResume("What are the metrics for previous closing price and volume traded for the ASIANPAINT, JIOFIN, WIPRO")


#PART 1 
print(resume_info.__dict__)
plan_info = resume_info.__dict__
'''
plan_info = {
      "name": [
        "TCS",
        "ONGC"
      ],
      "market_parameters": [
        "HIGH",
        "LOW"
      ]
    }

print(plan_info)
'''

import pandas as pd

df = pd.read_csv('Market_data.csv')
df.set_index('SYMBOL')

df = df.set_index('SYMBOL')

def get_stock_data(symbol):
    data = df.loc[symbol]
    data = data.to_dict()
    return data


#Part 2: Executor of the plan

for stock in plan_info['name']:
    print(f"The information for the {stock} is given below")
    data = get_stock_data(stock)
    for item in plan_info['market_parameters']:
        print(f"{item} is {data[item]}")
