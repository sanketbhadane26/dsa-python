accounts = [[1,5], [7,3], [3,5]]

max_wealth = 0

for customer in accounts:
    wealth = 0

    for money in customer:
        wealth = wealth + money

    if wealth > max_wealth:
        max_wealth = wealth

print(max_wealth)