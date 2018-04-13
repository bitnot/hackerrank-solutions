def count(coins, nr_coins_to_use, amount):
    if amount == 0:
        return 1
    if nr_coins_to_use == 0:
        return 0
    
    table = [[0 if i > 0 else 1 
              for i in range(amount+1) ]
              for j in range(2) ] 
    
    for j in range(nr_coins_to_use):
        table[0],table[1] = table[1],table[0]
        for i in range(1, amount+1):
            with_j = table[1][i - coins[j]] if i - coins[j] >= 0 else 0
            without_j = table[0][i] if j >= 1 else 0
            table[1][i] = with_j + without_j
 
    return table[1][amount]


n,m = [int(tmp) for tmp in input().strip().split(' ')]
c = [int(tmp) for tmp in input().strip().split(' ')]

ways = count(c, m, n)

print(ways)