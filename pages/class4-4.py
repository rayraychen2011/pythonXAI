# ------------------------------
# 定義一個沒有參數的函式 hello
# ------------------------------
def hello():
    # 每次呼叫這個函式，就會執行下面這行
    # 印出字串 "Hello, world!"
    print("Hello, world!")


# 使用 for 迴圈，讓 i 從 0 執行到 9（總共 10 次）
for i in range(10):
    # 每次迴圈都呼叫 hello() 函式
    # 因為 hello() 會印出 "Hello, world!"
    hello()


# ------------------------------
# 重新定義函式 hello（⚠️ 注意：這會覆蓋掉前一個 hello 函式）
# 這次 hello 有一個參數 name
# ------------------------------
def hello(name):
    # f-string：可以在字串中直接放入變數
    # 例如 name="Alice" → f"Hello, {name}!" = "Hello, Alice!"
    print(f"Hello, {name}!")


# 測試新的 hello(name) 函式
hello("Alice")  # 輸出 → Hello, Alice!
hello("Bob")  # 輸出 → Hello, Bob!
hello("Charlie")  # 輸出 → Hello, Charlie!

# ------------------------------
# 這裡的 for 迴圈會執行 10 次
# i 的值會依序從 0 到 9
# ------------------------------
for i in range(10):
    # 每次迴圈都會呼叫 hello(i)
    # 也就是把 i 傳給 hello 函式當參數
    # 由於 hello(name) 會印出 "Hello, {name}!"
    # 所以這裡會依序印出 Hello, 0! 到 Hello, 9!
    hello(i)


# ------------------------------
# 定義一個加法函式 add，有兩個參數 a 和 b
# ------------------------------
def add(a, b):
    # 使用 return 回傳 a + b 的結果
    # ⚠️ 注意：這裡不會自動印出結果，而是「把結果傳回給呼叫它的地方」
    return a + b


# 呼叫 add(1, 2)，會得到 3
print(add(1, 2))  # 印出 3

# 在 Python 裡，字串也能用 + 進行「拼接」
# 呼叫 add("Hello, ", "world!")，會得到 "Hello, world!"
print(add("Hello, ", "world!"))  # 印出 "Hello, world!"

# 把 add(3, 4) 的結果存進變數 sum
sum = add(3, 4)
print(sum)  # 印出 7


# ------------------------------
# 定義一個同時支援「加法」和「減法」的函式 add_sub
# ------------------------------
def add_sub(a, b):
    # 如果 a > b，就回傳加法結果
    if a > b:
        return a + b
    # 否則 (a <= b)，就回傳減法結果
    else:
        return a - b


# 測試 add_sub
print(add_sub(5, 6))  # 5 <= 6 → 走 else → 回傳 5 - 6 = -1
print(add_sub(6, 5))  # 6 > 5  → 走 if   → 回傳 6 + 5 = 11
