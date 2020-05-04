bonus1 = 100000 * 0.1 # <= 10万
bonus2 = bonus1 + 100000 * 0.075 # 10-20万
bonus3 = bonus2 + 200000 * 0.05 #20-40万
bonus4 = bonus3 + 200000 * 0.03 #40-60万
bonus5 = bonus4 + 400000 * 0.015 #60-100万

i = int(input('input gain:\n'))
if i <= 100000:
    bonus = i * 0.1
elif i <= 200000:
    bonus = bonus1 + (i - 100000) * 0.075
elif i <= 400000:
    bonus = bonus2 + (i - 200000) * 0.05
elif i <= 600000:
    bonus = bonus3 + (i - 400000) * 0.03
elif i <= 1000000:
    bonus = bonus4 + (i - 600000) * 0.015
else:
    bonus = bonus5 + (i - 1000000) * 0.01
print('bonus : %d'%bonus)