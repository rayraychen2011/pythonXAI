# 預設參數
# 可以在函式定義時設定預設參數值
# 當呼叫函式時沒有提供該參數，則使用預設值
# 多個參數，預設參數必須放在非預設參數之後
def hello(name, message="Hello"):
    print(f"{message}, {name}!")


hello("Alice")
hello("Bob", "good morning")


# 限制傳入參數的類型
# 可以在函數定義時使用類型提示來限制參數的類型
# 變數:型態=預設值
# ->型態,代表回傳值的型態
def add(a: int, b: int = 0) -> int:
    return a + b


print(add(1, 2))
print(add("hello", "world"))

# def 區域變數與全域變數
length = 5  # 全域變數


def calculate_squar_area():
    area = length**2  # length是全域變數，area是區域變數
    # length=length+1#這行會出錯
    # 因為在函式內部length被視為區域變數，必須使用global關鍵字來修改全域變數
    print("面積是:", area)


calculate_squar_area()
# print("長度是",area)#這行會出錯，因為area是區域變數，無法在函式外部訪問
length = 5


def calculate_squar_area():
    area = length**2  # length是全域變數，area是區域變數
    # length=length+1#這行會出錯
    # 因為在函式內部length被視為區域變數，必須使用global關鍵字來修改全域變數
    print("面積是:", area)


length = 10
calculate_squar_area()  # 100


length = 5
area = 100


def calculate_squar_area():
    area = length**2  # length是全域變數，area是區域變數


calculate_squar_area()
print("面積是:", area)

length = 5
area = 100


def calculate_squar_area() -> int:
    area = length**2  # length是全域變數，area是區域變數
    return area  # 回傳面積


area = calculate_squar_area()
print("面積是:", area)  # 25

length = 5
area = 100


def calculate_squar_area():
    global area  # 使用global關鍵字來修改全域變數
    area = length**2  # length是全域變數，area是區域變數


calculate_squar_area()
print("面積是:", area)  # 25


def hello(name: str):  # 函數傳入參數都是區域變數
    """
    指令說明區\n
    這是一個打招呼的函數\n
    參數:\n
    name:str - 姓名

    回傳:none

    範例:hello("Alice")
    """
    print(f"Hello, {name}!")  # 打招呼
