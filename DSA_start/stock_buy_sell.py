num = [5,2,1,5,6,4,8] 
def gain_profit(arr):
    n = len(arr)
    total = 0
    maxi = 0
    for i in range(0,n):
        buy = 0
        for j in range(0,n):
            buy  = arr[i]
            sell= arr[j]
            profit = buy - sell
            maxi = max(maxi , profit)
    return maxi        
result = gain_profit(num) # time complexty O(n^2)
print("find max profit = ",result) # space complexty O(1)
# Method second 

def sort_trick(arr):
    buy = min(arr)
    sell = max(arr)
    profit = sell - buy
    return profit
result1 = sort_trick(num) # time complexty O(n)
print("new trick find max profit = ",result1) # space complexty O(1)

# method third -> optimal way
def find_maxProfit(arr):
    min_prise = 999999
    max_profit = 0
    for i in range(0,len(arr)):
        min_prise = min(min_prise , arr[i])      
        profit =  arr[i] - min_prise
        max_profit  = max(max_profit , profit)
    return max_profit    
print(find_maxProfit(num))   # time complexty O(n) -> space O(1)    