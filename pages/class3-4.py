import random

ans = random.randint(1, 100)
max_num = 100
min_num = 1
while True:
    password = int(input(f"請輸入一個介於 {min_num} 和 {max_num} 之間的數字: "))

    if num > ans:
        print("猜的數字太大了")
        if num < max_num:
            max_num = num
    elif num < ans:
        print("猜的數字太小了")
        if num > min_num:
            min_num = num
    else:
        print("恭喜你猜對了！")
        break
