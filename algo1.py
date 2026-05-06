def exhaust_stock(stocks, budget):
    bestStock = 0
    bestSet = []

    s = len(stocks)

    for m in range(1 << s):
        currSet = []
        currVal = 0

        for i in range(s):
            if m & (1 << i):
                currSet.append(i + 1)
                currVal += stocks[i][1]
        if currVal <= budget and currVal > bestStock:
            bestStock = currVal
            bestSet = currSet
    return bestStock, bestSet

def main():
    stocksAndVals = [[1, 2], [3, 3], [5, 6], [6, 7]]
    Amount = 10

    bestStock, bestSet = exhaust_stock(stocksAndVals, Amount)

    print([bestStock, bestSet])

if __name__ == "__main__":
    main()