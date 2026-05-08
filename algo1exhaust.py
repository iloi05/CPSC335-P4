from itertools import combinations
def maxStocks(stocks, amount):
    # output is supposed to be [10, [1, 3]]
    weight = [i[1] for i in stocks]
    w = len(stocks)

    for stock in range(1, w + 1):
        for combo in combinations(range(w), stock):
            totW = sum(weight[i] for i in combo)

            if totW == amount:
                return [amount, list(combo)]

    return [0, []]    
    


def main():
    stocks = [[1, 2], [3, 3], [5, 6], [6, 7]]
    amount = 10
    print(maxStocks(stocks, amount))

if __name__ == "__main__":
    main()


