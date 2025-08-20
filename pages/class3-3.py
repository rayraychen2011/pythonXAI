# 算術指定運算子
a = 1
a += 1  # a=a+1
print(a)  # 2
a -= 1  # a=a-1
print(a)  # 1
a *= 2  # a=a*2
print(a)  # 2
a /= 2  # a=a/2
print(a)  # 1.0
a //= 2  # a=a//2
print(a)  # 0
a %= 2  # a=a%2
print(a)  # 0
a **= 2  # a=a**2
print(a)  # 0.0

# 優先順序
# 1.()括號
# 2.**次方
# 3. * / % // 乘 除 取商 取餘數
# 4. + - 加 減
# 5. == != > < >= <= 比較運算子
# 6. not
# 7. and
# 8. or
# 9. = += -= *= /= //= %= **= 算術指定運算子


# while會搭配一個條件使用
# 條件式為true時，會持續執行迴圈內的程式碼
# 條件式為false時，會跳出迴圈
# 每次執行完迴圈內的程式碼後，會再檢查一次條件式
i = 0
while i < 5:
    print(i)
    i += 1


i = 0
while i < 5:
    print(i)

    for j in range(5):
        print(j)

    if i == 3:
        break
    i += 1

for i in range(5):
    print(i)
    if i == 3:
        break

import random

print(random.randrange(7))  # 0-6
print(random.randrange(1, 10))  # 1-10
print(random.randrange(1, 10, 2))  # 1-10，間格為2
# random.randint()設定抽籤範圍的方式一定要設定start and end
print(random.randint(1, 10))  # 1-10，包含1和10
