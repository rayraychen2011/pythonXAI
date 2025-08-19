print([])  # 這是一個空的list
print([1, 2, 3])  # 這是一個包含三個元素的list
print([1, 2, 3, "a", "b", "c"])  # 這是一個包含六個元素的list
print([1, 2, 3, ["a", "b", "c"]])  # 這是一個包含四個元素的list
print(1, True, "a", 1.23)  # 這是一個包含四個元素的list

# CRUD是一個常見的資料庫操作縮寫，代表創建(Create)、讀取(Read)、更新(Update)和刪除(Delete)。

# CRUD Read 操作
# list讀取元素,元素的index從0開始
L = [1, 2, 3, "a", "b", "c"]
print(L[0])  # 1
print(L[1])  # 2
print(L[2])  # 3
print(L[3])  # a

L = [1, 2, 3, "a", "b", "c"]
# 就是取index 0到最後,每次取2個元素,所以是[1,3,"b"]
print(L[0::2])
# 就是取index 1到3的元素,不包含index 4,所以是[2, 3, "a"]
print(L[1:4])
# 就是取index 1到3的元素,不包含index 4,而且每次取2個元素,所以是[2,"a"]
print(L[1:4:2])
# 跟range一樣的用法,只是符號不同

# list 取長度,也就是list中有多少個元素,不是index的最大值
L = [1, 2, 3, "a", "b", "c"]
print(len(L))  # 6

# list 走訪元素
# 可以透過取得index的方式來找到list中的資料
# 也可以直接把list當作一個範圍來取得資料
# 這兩種方式都可以,但是看使用的情況是否會需要index來決定要用哪一種方式
L = [1, 2, 3, "a", "b", "c"]
for i in range(0, len(L), 2):
    print(L[i])

    for i in L:
        print(i)

# CRUD Update 操作
# list修改元素
# 可以透過index來修改list中的元素
L = [1, 2, 3, "a", "b", "c"]
L[0] = 2  # 把index 0的元素修改成2
print(L)

# call by value
a = 1
b = a  # 複製a的值給b
b = 2
print(a, b)  # (1, 2)

# call by reference
a = [1, 2, 3]
b = a.copy()  # 複製a的值給b,但是b跟a指向不同的記憶體位置
b[0] = 2
print(a, b)  # a還是[1,2,3], b變成[2,2,3]

# CRUD Delete 操作
# list的移除元素方式有兩種
# 1.使用remove,可以移除指定的元素
L = [1, 2, 3, "a", "b", "c"]
L.remove("a")  # 移除第一個"a"
# 代表remove會從頭開始找,找到第一個符合的元素就會移除
# 如果想要移除所有的符合的元素,可以使用迴圈
for i in L:
    if i == "a":
        L.remove(i)
# 2.使用pop,可以移除指定的index元素
L = ["a", "b", "c", "a"]
L.pop(0)  # 移除index 0的元素
# 代表pop會移除指定的index的元素
# 如果不指定index,則會移除最後一個元素
L.pop()  # 移除最後一個元素
print(L)

# open()開啟模式
# 'r' 讀取模式,檔案必須存在
# 'w' 寫入模式,檔案不存在則會創建
# 'a' 附加模式,檔案不存在則會創建
# 'r+' 讀寫模式,檔案必須存在
# 'w+' 讀寫模式,檔案不存在則會創建
# 'a+' 附加模式,檔案不存在則會創建

f = open("pages/class1-1.py", "r", encoding="utf-8")  # 開啟檔案
contest = f.read()  # 讀取檔案內容
print(contest)  # 印出檔案內容
f.close()  # 關閉檔案
##################################################
with open("pages/class1-1.py", "r", encoding="utf-8") as f:  # 使用with開啟檔案
    content = f.read()  # 讀取檔案內容
    print(content)  # 印出檔案內容
# 不用寫f.close(),with會自動關閉檔案

# 字串的小工具,用來檢查字串最後是否有特定的字串
filename = "class1.md"
print(filename.endswith(".md"))  # True,因為字串最後是.md
filename2 = "notes.txt"
print(filename2.endswith(".md"))  # False,因為字串最後是.txt
