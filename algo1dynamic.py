# Names: Ivy Loi, Homan Qiu, Robert Gutierrez, Richie Nguyen
# Emails: iloi05@csu.fullerton.edu, hqiu2006@csu.fullerton.edu, lil.rjg3@csu.fullerton.edu, richienguyen@csu.fullerton.edu
# CPSC 335 section 11
# Project 4: Algorithm 1 Part A
# Date: 5/8/2026

def stocksRecursive(stocks, amount):
    # table for candidates
    table = [[0] * (amount + 1) for _ in range(len(stocks))]
    # this entire forloop is for getting the max value
    for i in range(len(stocks)):
        # getting weights and values
        weight = stocks[i][1]
        val = stocks[i][0]

        for j in range(1, amount + 1):
            if i > 0:
                # tossing whatever exceeds the budget
                toss = table[i - 1][j]
            else:
                # toss nothing if there is nothing to toss
                toss = 0
            
            if j >= weight:
                if i > 0:
                    # keeping whatever has best weight that does not exceed budget
                    keep = val + table[i - 1][j - weight]
                else:
                    # keep the value that is good
                    keep = val
            else:
                # keep nothing if value is not good
                keep = 0
            # table is the max value found that we can get   
            table[i][j] = max(keep, toss)
        # best = for best index combos
        # j is copy of amount given
        best = []
        j = amount
    # this part is for getting the best combo of stocks
    for i in range(len(stocks) - 1, -1, -1):
        if i == 0:
            if table[i][j] > 0:
                # update best list if i = 0 and the best value found better than 0
                best.append(i)
        elif table[i][j] != table[i - 1][j]:
            # update best and weight if max val is not same as previous candidate
            best.append(i)
            j -= stocks[i][1]
    # reverse so that output is in ascending order
    best.reverse()
    # returns [max value, [best combo]]
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