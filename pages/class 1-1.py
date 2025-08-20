# 這是註解,不會被程式執行
# ctrl+?可以把單行程式碼註解起來
# 如果框選了多行程式碼,按ctrl+?可以把多行程式碼註解起來

# 基本型態
print(1)  # int這是整數，－１，０，１，２，３，４，５，６，７，８，９
print(1.00)  # float這是浮點數
print(1.234)  # float這是浮點數
print("apple")  # str這是字串＂ｓａｄａｓｄ１２３１２５５５７＂，’１’
print("１")  # str這是字串＂１＂，’１’
print(True)  # bool這是布林值，只有True／False
print(False)  # bool這是布林值，只有True／False

# 變數
a = 10  # 新增一個儲存空間並取名為ａ，＂＝＂的功能是把右邊的值１０存入左邊的
print(a)  # 在終端機顯示ａ所存的值
a = "apple"  # 將ａ的值改為＂ａｐｐｌｅ＂
print(a)  # 在終端機顯示ａ所存的值

# 運算子
print(1 + 1)  # 加法
print(1 - 1)  # 減法
print(1 * 1)  # 乘法
print(1 / 1)  # 除法
print(1 // 1)  # 取商
print(1 % 1)  # 取餘數
print(2**3)  # 次方

# 優先順序
# 1. 括號 ()
# 2. 指數運算 **
# 3. 乘 除取商 取餘數 * / // %
# 4. 加減法 + -

# 請用前面的用詞標準來完成以下的程式碼的註解

# 字串運算
print("apple" + "pen")  # 字串相加
print("apple" * 3)  # 字串乘法

# 字串格式化
name = "apple"  # 字串變數
age = 18  # 整數變數
print(f"My name is {name} and I am {age} years old.")  # 使用f-string
# 可以將其他型態的資料放入到f字串裡面的 {}，這樣就可以在字串中顯示變數或運算結果

# len()函式可以計算任何型態的資料長度
print(len("apple"))  # 計算字串長度

# type()#可以查看變數的型態
print(type(1))  # <class 'int'>
print(type(1.0))  # <class 'float'>
print(type("apple"))  # <class 'str'>
print(type(True))  # <class 'bool'>

# 型態轉換
print(int(1.0))  # 將浮點數轉換為整數
print(float(1))  # 將整數轉換為浮點數
print(str(1))  # 將整數轉換為字串
print(bool(1))  # 將整數轉換為布林值
print(int(1.234))  # 將浮點數轉換為整數
print(float("1.234"))  # 將字串轉換為浮點數
print(str(1.234))  # 將浮點數轉換為字串
print(bool(1.234))  # 將浮點數轉換為布林值

print("輸入開始")
# input()函式可以讓使用者輸入文字
# ()裡面的文字式提示訊息會先在終端機上顯示才會等待使用者輸入
a = input("請輸入一個數字: ")
print("輸入結束")
print(int(a) + 10)
print(type(a))  # 證明透過input()輸入內容都是字串

r = input("請輸入圓的半徑: ")
print(f"圓的面積是: {3.14 * float(r) * float(r)}")  # 將輸入的半徑字串轉為浮點數後計算圓面積 (π≈3.14)
