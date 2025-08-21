# 字典 (dict) 是透過 key-value 的方式來儲存資料
# key 必須是唯一的，value 可以重複

# 建立一個字典
d = {"a": 1, "b": 2, "c": 3}

# 透過 key 取值
print(d["a"])  # 1
print(d["b"])  # 2
print(d["c"])  # 3

# 取得字典所有的 key
print(d.keys())  # dict_keys(['a', 'b', 'c'])
for key in d.keys():
    print(key)  # 分別印出 a, b, c

# 取得字典所有的 value
print(d.values())  # dict_values([1, 2, 3])
for value in d.values():
    print(value)  # 分別印出 1, 2, 3

# 取得字典所有的 key-value 配對
print(d.items())  # dict_items([('a', 1), ('b', 2), ('c', 3)])
for key, value in d.items():
    print(key, value)  # 分別印出 a 1, b 2, c 3

# CRUD 操作示範
# C: Create 新增
d["d"] = 4  # 新增 key 'd'，value 為 4
print(d)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# U: Update 修改
d["a"] = 40  # 將 key 'a' 的 value 改為 40
print(d)  # {'a': 40, 'b': 2, 'c': 3, 'd': 4}

# D: Delete 刪除
# pop() 方法會刪除指定的 key，並回傳被刪除的 value
print(d.pop("a"))  # 40 (刪除 'a' 並回傳它的 value)
print(d.pop("e", "not found"))  # 'not found' (如果 key 不存在，回傳預設值)

# 字典長度
print(len(d))  # 3 (目前有 b, c, d 三個 key)

# 檢查 key 是否存在
print("a" in d)  # False (因為 'a' 已被刪除)
print("e" in d)  # False (key 'e' 不存在)
