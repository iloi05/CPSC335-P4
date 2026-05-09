# Names: Ivy Loi, Homan Qiu, Robert Gutierrez, Richie Nguyen
# Emails: iloi05@csu.fullerton.edu, hqiu2006@csu.fullerton.edu, lil.rjg3@csu.fullerton.edu, richienguyen@csu.fullerton.edu
# CPSC 335 section 11
# Project 4: Algorithm 1 Part A
# Date: 5/8/2026



from itertools import combinations
def maxStocks(stocks, amount):
    # output is supposed to be [10, [1, 3]]
    # splitting weight from the arrays so it's easier to work with
    # M IS OUR STOCKS
    # splitting weight and values so it's easier to work with
    weight = [i[1] for i in stocks]
    val = [i[0] for i in stocks]

    # for storing the best combos of stocks
    best = []
    bestV = 0
    # searching through input
    for stock in range(1, len(stocks) + 1):
        # checking all possible combinations of stocks
        for combo in combinations(range(len(stocks)), stock):
            # adding up the weights in weight
            totW = sum(weight[i] for i in combo)
            totV = sum(val[i] for i in combo)
        
            # checking if totW is below or same as the amount/cap
            if totW <= amount:
            # if the new value found is greater than the best value
                if totV > bestV:
                # update best value
                    bestV = totV
                # update best combo
                    best = list(combo)

    # return nothing if solution not found
    # will also return best combination if there is something found
    return [bestV, best]    
    


def main():
    stocks = [[1, 2], [3, 3], [5, 6], [6, 7]]
    amount = 10
    print("Example 1: ", maxStocks(stocks, amount))

    stocks = [[3, 5], [2, 7], [6, 9], [1, 2]]
    amount = 17
    print("Example 2: ", maxStocks(stocks, amount))

    stocks = [[3, 2], [4, 5], [6, 9], [2, 3]]
    amount = 1
    print("Example 3: ", maxStocks(stocks, amount))

if __name__ == "__main__":
    main()


