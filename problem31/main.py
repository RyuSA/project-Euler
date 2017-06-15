# coding: utf-8
sum_limit = 200
coins = [1,2,5,10,20,50,100,200]

# cur位置のcoinに関して、targetペンスが何枚存在するかを計算
def counter(cur, target):
    global coins
    if cur == 0:
        return 1
    else:
        ans = 0
        # coins[cur]が最大何枚まで使えるのか
        maximun = target//coins[cur] + 1
        for x in xrange(maximun):
            ans += counter(cur-1, target-coins[cur]*x)
        return ans

print counter(len(coins)-1, sum_limit)
