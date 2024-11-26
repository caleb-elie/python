bitcoin_value_usd = 40000
def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):
    return bitcoin_amount *  bitcoin_value_usd

bitcoin_amount = float(input("Enter your amount of Bitcoin: "))
bitcoinNetworth = bitcoinToUSD(bitcoin_amount, bitcoin_value_usd)

if bitcoinNetworth < 30000:
    print(f"You currently have ${bitcoinNetworth:.2f} you have to buy some bitcoins")  
else:
    print("You are rich")

print(f"1.2 Bitcoin is worth ${bitcoinToUSD(1.2, bitcoin_value_usd):.2f} at the current rate")
