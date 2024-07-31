import timeit

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= coin * count
            result[coin] = count
    
    return result

# Приклад використання
print("------------ find_coins_greedy ------------")
print(find_coins_greedy(113))  # {50: 2, 10: 1, 2: 1, 1: 1}
print(find_coins_greedy(165))
print(find_coins_greedy(297))

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)
    
    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin

    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = coin_used[current_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_amount -= coin
    
    return result

# Приклад використання
print("------------ find_min_coins ------------")
print(find_min_coins(113))  # {50: 2, 10: 1, 2: 1, 1: 1}
print(find_min_coins(165))
print(find_min_coins(297))  

def compare_algorithms(amount):
    greedy_time = timeit.timeit(lambda: find_coins_greedy(amount), number=1000)
    dynamic_time = timeit.timeit(lambda: find_min_coins(amount), number=1000)
    
    print(f"Greedy Algorithm Time: {greedy_time:.6f} seconds")
    print(f"Dynamic Programming Algorithm Time: {dynamic_time:.6f} seconds")

# Приклад порівняння для різних сум
print("------------ compare for 113 ------------")
compare_algorithms(113)
print("------------ compare for 594 ------------")
compare_algorithms(594)
print("------------ compare for 1837 ------------")
compare_algorithms(1837)
