# for 迴圈
# 說明：for 會搭配 in 使用，in 後面接一個可迭代的物件（例如 range、list）
# 範例 1：使用 range(5) 會產生 0 到 4 的數字（不包含 5）
# i 為迴圈變數，每次迴圈會取出一個元素放入 i
for i in range(5):
    print(i)  # 依序印出 0,1,2,3,4

# range 可以設定起始值與結束值（不包含結束值）
# 範例 2：range(1, 5) 會產生 1 到 4 的數字
for i in range(1, 5):
    print(i)  # 依序印出 1,2,3,4

# range 也可以設定起始值、結束值與間隔（step），仍不包含結束值
# 範例 3：range(1, 5, 2) 會產生 1 與 3
for i in range(1, 5, 2):
    print(i)  # 依序印出 1,3
