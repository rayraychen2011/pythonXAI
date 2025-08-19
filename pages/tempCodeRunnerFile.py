# for迴圈
# for會搭配in來使用,in後面接一個有範圍的東西
# 範例：使用 range(5) 產生 0 到 4 的數字
# i是迴圈的變數，可以自己命名
# 迴圈變數每回合會從範圍裡取出一個資料
for i in range(5):
    print(i)

# range 可以設定起始值和結束值,但不包含結束值
# 範例：使用 range(1, 5) 產生 1 到 4 的數字
for i in range(1, 5):
    print(i)

# range 可以設定起始值,結束值與間隔值,但不包含結束值
# 範例：使用 range(1, 5, 2) 產生 1, 3 的數字
for i in range(1, 5, 2):
    print(i)
