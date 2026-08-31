prices = [7,1,5,3,6,4]
max_profit=0
for i in range(len(prices)):
    for j in range(i+1,(len(prices))):
            prev_profit=prices[j]-prices[i]
            if prev_profit>max_profit:
                max_profit=prev_profit
print(max_profit)
 
