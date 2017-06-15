# coding: utf-8;

# pandimantalになるのは1桁×4桁=4桁か2桁×3桁=4桁のみ
# 1の位が6のとき、もう片割れの1の位は奇数確定。
# 1の位は1,5ではない

pand = [1,2,3,4,5,6,7,8,9]

def isPand(a,b):
    a_conf = a%10
    b_conf = b%10
    if((not a_conf) or (not b_conf)):
        return False
    if(a_conf==1 or a_conf==5 or b_conf==1 or b_conf==5):
        return False
    digs = list(set([int(x) for x in list(str(a)+str(b)+str(a*b))]))

    if(digs==pand):
        return True
    else:
        return False

# まず1桁×3桁,1桁×4桁
ans = []

for x in xrange(2,10):
    if x == 6:
        for y in xrange(123,9878,2):
            if len(str(x*y)) == 4:
                if isPand(x,y):
                    ans.append(x*y)
    else:
        for y in xrange(123,9878):
            print "bb"
            if len(str(x*y)) == 4:
                if(not x&1 and y%10==6):
                    continue
                if(not y&1 and x==6):
                    continue
                if isPand(x,y):
                    ans.append(x*y)

# 2桁×3桁
for x in xrange(13,98):
    if x%10 == 6:
        for y in xrange(123,988,2):
            if len(str(x*y)) == 4:
                if isPand(x,y):
                    ans.append(x*y)
    else:
        for y in xrange(123,988):
            print "aa"
            if len(str(x*y)) == 4:
                if(not x&1 and y%10==6):
                    continue
                if(not y&1 and x%10==6):
                    continue
                if isPand(x,y):
                    ans.append(x*y)



ans = sum(list(set(ans)))
print ans
