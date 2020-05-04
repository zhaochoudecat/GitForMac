#一个数加上100是一个完全平方数，再加上268又是一个完全平方数，求该数

#从100000内找，先将该数加上100开放，然后将该数加上268后开方，开方后的结果满足条件即可成立

import math
for i in range (100000):
    #转换为整型
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if (x * x == i + 100) and (y * y == i +268):
        print(i)