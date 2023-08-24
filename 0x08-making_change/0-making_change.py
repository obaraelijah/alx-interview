#!/usr/bin/python3
"""Making Change Task."""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values."""
    if total <= 0:
        return 0
    
    if not coins or all(coin > total for coin in coins):
        return -1

    rem = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    
    while rem > 0 and coin_idx < n:
        if rem >= sorted_coins[coin_idx]:
            rem -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
            
    return coins_count if rem == 0 else -1