print([])  # 這是一個空的 list
print([1, 2, 3])  # 這是一個包含三個元素的 list
print([1, 2, 3, "a", "b", "c"])  # 這是一個包含六個元素的 list，可以混合型別
print(
    [1, 2, 3, ["a", "b", "c"]]
)  # 這是一個包含四個元素的 list，其中一個元素本身是另一個 list
print(1, True, "a", 1.23)  # 這是直接列出多個值，print 會以空格分隔輸出（不是 list）

# CRUD 是一個常見的資料操作縮寫，代表創建(Create)、讀取(Read)、更新(Update)和刪除(Delete)

# CRUD Read 操作
# list 讀取元素，元素的 index 從 0 開始
L = [1, 2, 3, "a", "b", "c"]
print(L[0])  # 取得 index 0 的元素，輸出 1
print(L[1])  # 取得 index 1 的元素，輸出 2
print(L[2])  # 取得 index 2 的元素，輸出 3
print(L[3])  # 取得 index 3 的元素，輸出 'a'

L = [1, 2, 3, "a", "b", "c"]
# 切片語法 start:stop:step
# L[0::2] 代表從 index 0 開始到結尾，每次跳過 2 個元素（step=2）
# 所以會取到 index 0,2,4 -> [1, 3, 'b']
print(L[0::2])
# L[1:4] 代表從 index 1 開始到 index 4（不包含 4）
# 所以會取到 index 1,2,3 -> [2, 3, 'a']
print(L[1:4])
# L[1:4:2] 代表從 index 1 開始到 index 4（不包含 4），每次跳過 2 個元素
# 所以會取到 index 1,3 -> [2, 'a']
print(L[1:4:2])
# 切片的用法跟 range 類似，但語法不同

# list 取長度，也就是 list 中有多少個元素（不是 index 的最大值）
L = [1, 2, 3, "a", "b", "c"]
print(len(L))  # 輸出 6，表示 list 有 6 個元素

# list 走訪元素
# 可以透過 index（range）取得資料，或直接把 list 當作可迭代物件（for item in L）
# 選哪一種方式，視是否需要 index 來決定
L = [1, 2, 3, "a", "b", "c"]
for i in range(0, len(L), 2):
    # 使用 index 走訪，這裡每次跳 2 個索引，會印出 index 0,2,4 的元素
    print(L[i])

for i in L:
    # 直接以元素為單位走訪，較為簡潔
    print(i)

# CRUD Update 操作
# list 修改元素可以透過 index 指定位置來更改
L = [1, 2, 3, "a", "b", "c"]
L[0] = 2  # 將 index 0 的元素從 1 改為 2
print(L)  # 印出修改後的 list

# 值複製（call by value 的概念）
a = 1
b = a  # 將 a 的值複製給 b（原始型別為不可變，因此改變 b 不會影響 a）
b = 2
print(a, b)  # 會印出 1 2，代表 a 未被 b 的變動影響

# 參考複製（類似 call by reference 的行為）
# list 是可變物件，若直接指定 b = a，則 b 與 a 指向同一個物件
# 若想要複製出新的 list，應使用 a.copy() 或 list(a)
a = [1, 2, 3]
b = a.copy()  # 複製 a 的內容給 b，但 b 與 a 指向不同記憶體位置
b[0] = 2
print(a, b)  # a 保持 [1,2,3]，b 變成 [2,2,3]

# CRUD Delete 操作
# list 移除元素的方式有好幾種，這裡示範 remove 與 pop
# 1. 使用 remove(value) 會移除第一個符合的元素
L = [1, 2, 3, "a", "b", "c"]
L.remove("a")  # 移除第一個出現的 'a'
# remove 會從頭開始尋找，找到第一個符合的元素後就移除
# 若要移除所有符合的元素，可以搭配迴圈或 list comprehension
for i in L:
    if i == "a":
        L.remove(i)  # 注意：在迴圈中修改 list 會有副作用，實務上應避免
# 2. 使用 pop(index) 可以移除指定 index 的元素
L = ["a", "b", "c", "a"]
L.pop(0)  # 移除 index 0 的元素
# pop 若不帶參數，會移除並回傳最後一個元素
L.pop()  # 移除最後一個元素
print(L)  # 印出剩下的元素

# open() 開檔案的常見模式
# 'r' 讀取模式：檔案必須存在
# 'w' 寫入模式：檔案不存在會被創建（會覆寫原檔）
# 'a' 附加模式：在檔案末尾加入資料，檔案不存在會被創建
# 'r+' 讀寫模式：檔案必須存在
# 'w+' 讀寫模式：檔案不存在會被創建（會覆寫原檔）
# 'a+' 附加讀寫模式：檔案不存在會被創建

f = open("pages/class1-1.py", "r", encoding="utf-8")  # 以讀取模式開啟檔案
contest = f.read()  # 讀取整個檔案內容到變數 contest
print(contest)  # 印出讀取到的內容
f.close()  # 關閉檔案，釋放系統資源
##################################################
with open(
    "pages/class1-1.py", "r", encoding="utf-8"
) as f:  # 使用 with 自動管理檔案資源
    content = f.read()  # 讀取檔案內容
    print(content)  # 印出檔案內容
# 使用 with 就不用手動呼叫 f.close()，with 會在區塊結束時自動關閉檔案

# 字串的小工具：檢查字串是否以特定字尾結束
filename = "class1.md"
print(filename.endswith(".md"))  # True，因為檔名最後以 .md 結尾
filename2 = "notes.txt"
print(filename2.endswith(".md"))  # False，因為檔名最後是 .txt
