#You cannot buy on day 2 and sell on day 1. Find the max profit

def maxProfit(prices:list()) -> int:
    left,right = 0,1
    max_profit = 0
    
    while right < len(prices):
        if prices[left] < prices[right]:
            current_profit = prices[right] - prices[left]
            max_profit = max(current_profit,max_profit)

        else:
            left = right 
        right = right + 1

    return max_profit


if __name__ == '__main__':    
    prices = [7,1,5,3,6,4]
    maxprof = maxProfit(prices)
    print(maxprof)