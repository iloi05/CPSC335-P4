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
                    keep = weight + table[i - 1][j - weight]
                else:
                    keep = weight
            else:
                keep = 0
                
            table[i][j] = max(keep, toss)

    return table[len(stocks) - 1][amount]

def main():
    stocks = [[1, 2], [3, 3], [5, 6], [6, 7]]
    amount = 10

    print(stocksRecursive(stocks, amount))

if __name__ == "__main__":
    main()