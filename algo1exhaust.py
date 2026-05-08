from itertools import combinations
def maxStocks(stocks, amount):
    # output is supposed to be [10, [1, 3]]
    # splitting weight from the arrays so it's easier to work with
    weight = [i[1] for i in stocks]
    val = [i[1] for i in stocks]

    w = len(stocks)

    best = []
    bestW = 0
    bestV = 0

    for stock in range(1, w + 1):
        for combo in combinations(range(w), stock):
            # adding up the weights in weight
            totW = sum(weight[i] for i in combo)
            totV = sum(val[i] for i in combo)

            # checking if totW is the same as the amount/cap
            if totW <= amount and totV > bestV:
                bestV = totV
                bestW = totW
                best = list(combo)
    # return nothing if solution not found
    return [bestW, best]    
    


def main():
    stocks = [[1, 2], [3, 3], [5, 6], [6, 7]]
    amount = 10
    print(maxStocks(stocks, amount))

    stocks = [[3, 5], [2, 7], [6, 9], [1, 2]]
    amount = 11
    print(maxStocks(stocks, amount))

if __name__ == "__main__":
    main()


