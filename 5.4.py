# coding=utf-8
# 代码文件: ch05/ch5_4.py
# 计算水仙花数。提示：水仙花数是一个三位数，三位数各位的立方之和等于三位数本身。

for a in range(10):
    for b in range(10):
        for c in range(10):
            if a**3 + b**3 + c**3 == a*100 + b*10 + c:
                num = a*100 + b*10 + c
                if a == 0:
                    continue
                print(num)

