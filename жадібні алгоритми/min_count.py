

def min_count(coins: list, quantity: int):

    result = {}
    
    for el in coins:
        result[el] = 0
        while quantity >= el:
            quantity -= el
            result[el] += 1  



    return result


coins = [50, 25, 10, 5, 2, 1]

value = int(input('Введіть суму для видачі >>>  '))
print(f'Монети для здачі {min_count(coins, value)}') 