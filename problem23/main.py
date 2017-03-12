import abundant as ab

ans = 0
ab.listAbundant()

for x in range(ab.maximun):
    if(not ab.isSumOfAbundants(x)):
        ans = ans + x
print(ans)
