# 比較運算子（用來比較兩個東西誰比較大、是不是一樣）
# 注意：最好比較的是同一種類的東西（像都是數字），比較不同型態可能會錯誤或沒意義

# 等於 == ：檢查左右兩邊是否一樣，會回傳 True 或 False
print(1 == 1)  # True，因為 1 跟 1 一樣

# 不等於 != ：檢查左右兩邊是否不一樣
print(1 != 1)  # False，因為 1 跟 1 是一樣的，所以不等於為 False

# 大於 > ：檢查左邊是否比右邊大
print(1 > 1)  # False，因為 1 並不大於 1

# 小於 < ：檢查左邊是否比右邊小
print(1 < 1)  # False，因為 1 並不小於 1

# 小於等於 <= ：左邊小於或等於右邊時為 True
print(1 <= 1)  # True，因為 1 等於 1

# 大於等於 >= ：左邊大於或等於右邊時為 True
print(1 >= 1)  # True，因為 1 等於 1


# 邏輯運算子（用來把多個條件連在一起）
# and：左右兩邊都要是 True 時，結果才是 True
print(True and True)  # True
print(True and False)  # False
print(False and False)  # False
print(False and True)  # False

# or：只要左右其中一邊是 True，結果就是 True
print(True or True)  # True
print(True or False)  # True
print(False or False)  # False
print(False or True)  # True

# not：把 True 變成 False，或把 False 變成 True（取反）
print(not True)  # False
print(not False)  # True


# 優先順序
# 1.()括號
# 2.**次方
# 3. * / % // 乘 除 取商 取餘數
# 4. + - 加 減
# 5. == != > < >= <= 比較運算子
# 6. not
# 7. and
# 8. or


# 密碼檢查範例（示範 if / elif / else）
# 使用 input() 讓使用者輸入密碼，然後檢查密碼是否正確
password = input("請輸入密碼：")
if password == "0423":
    print("密碼正確，歡迎進入系統！")  # 當密碼是 0423 時顯示歡迎訊息
elif password == "1120":
    print("管理員密碼正確，歡迎進入管理系統！")  # 當密碼是 1120 時顯示管理員歡迎
else:
    print("密碼錯誤。")  # 其他情況都顯示密碼錯誤

# 小說明：
# - if 會先檢查第一個條件，若為 True 就執行對應的區塊並跳過其他 elif
# - elif（意思是 else if）可以接著檢查其他條件
# - else 在所有條件都不成立時執行
# 使用 elif 可以讓判斷更簡單、速度更快；如果用多個獨立的 if，
# 每個 if 都會被檢查，程式會比較慢一點
