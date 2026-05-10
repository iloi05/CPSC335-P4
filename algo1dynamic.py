# Names: Ivy Loi, Homan Qiu, Robert Gutierrez, Richie Nguyen
# Emails: iloi05@csu.fullerton.edu, hqiu2006@csu.fullerton.edu, lil.rjg3@csu.fullerton.edu, richienguyen@csu.fullerton.edu
# CPSC 335 section 11
# Project 4: Algorithm 1 Part A
# Date: 5/8/2026

def stocksRecursive(stocks, amount):
    # make a table to keep track of candidates
    dpTable = [[{"val": 0, "stock": []} for _ in range(amount + 1)]
               for _ in range(len(stocks))
    ]
    # looping through stocks
    for i in range(len(stocks)):
        # splitting weights and values
        weight = stocks[i][1]
        val = stocks[i][0]
        # this part calculates what to toss and what to keep
        for j in range(1, amount + 1):
            # checking current element in stocks
            if i > 0:
                # marking whatever is not good as toss
                toss = {"val": dpTable[i - 1][j]["val"],
                        "stock": dpTable[i - 1][j]["stock"][:]}
            else:
                # nothing to toss then toss is empty
                toss = {"val": 0, "stock": []}
            if j >= weight:
                if i > 0:
                    # oldCandidate was whatever was last found and was good
                    oldCandidate = dpTable[i - 1][j - weight]
                    # marking the oldCandidate for keeping
                    keep = {"val": val + oldCandidate["val"],
                            "stock": oldCandidate["stock"] + [i]
                            }
                else:
                    # updating keep if something better is found
                    keep = {"val": val, "stock": [i]}
            else:
                # keep stays empty if nothing is found
                keep = {"val": 0, "stock": []}
                # if keep is greater than toss then we update the table to be keep
            if keep["val"] > toss["val"]:
                dpTable[i][j] = keep
            else:
                # keeping whatever we marked for tossing if nothing better is found
                dpTable[i][j] = toss
    # for shorter return statement
    output = dpTable[len(stocks) - 1][amount]
    return [output["val"], output["stock"]]

def main():
    stocks = [[1, 2], [3, 3], [5, 6], [6, 7]]
    amount = 10

    print("Example 1: ", stocksRecursive(stocks, amount))

    stocks = [[5, 6], [4, 7], [7, 9], [3, 2]]
    amount = 17
    print("Example 2: ", stocksRecursive(stocks, amount))

    stocks = [[3, 2], [4, 5], [6, 9], [2, 3]]
    amount = 1
    print("Example 3: ", stocksRecursive(stocks, amount))

    stocks = [[5, 6], [10, 20], [7, 8], [14, 30]]
    print()
    print("User sample:", stocks)
    amount = int(input("Enter your budget: "))
    print("Your best stocks to buy: ", stocksRecursive(stocks, amount))

if __name__ == "__main__":
    main()