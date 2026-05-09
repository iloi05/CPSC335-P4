def stocksRecursive(stocks, amount):
    table = [[0] * (amount + 1) for _ in range(len(stocks))]

    for i in range(len(stocks)):
        weight = stocks[i][1]
        val = stocks[i][0]
        for j in range(amount + 1):
            if i > 0:
                toss = table[i - 1][j]
            else:
                toss = 0
            
            if j >= weight:
                if i > 0:
                    keep = val + table[i - 1][j - weight]
                else:
                    keep = val
            else:
                keep = 0
                
            table[i][j] = max(keep, toss)

        best = []
        j = amount

    for i in range(len(stocks) - 1, -1, -1):
        if i == 0:
            if table[i][j] > 0:
                best.append(i)
        elif table[i][j] != table[i - 1][j]:
            best.append(i)
            j -= stocks[i][1]
    best.reverse()

    return [table[len(stocks) - 1][amount], best]

def main():
    stocks = [[1, 2], [3, 3], [5, 6], [6, 7]]
    amount = 10

    print("Example 1: ", stocksRecursive(stocks, amount))

    stocks = [[3, 5], [2, 7], [6, 9], [1, 2]]
    amount = 17
    print("Example 2: ", stocksRecursive(stocks, amount))

    stocks = [[3, 2], [4, 5], [6, 9], [2, 3]]
    amount = 1
    print("Example 3: ", stocksRecursive(stocks, amount))

if __name__ == "__main__":
    main()