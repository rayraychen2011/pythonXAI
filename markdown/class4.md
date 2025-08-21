---

# 🖥️ 我的程式學習筆記 (Python)

## 📌 字典 (dict)

字典就像一本小字典，一邊是「單字(key)」，一邊是「解釋(value)」。
👉 **key 不可以重複**，但 value 可以一樣。

```python
d = {"a": 1, "b": 2, "c": 3}
```

* 🔑 用 key 拿資料

  ```python
  print(d["a"])  # 1
  ```
* 📂 看所有 key

  ```python
  print(d.keys())  # ['a', 'b', 'c']
  ```
* 📦 看所有 value

  ```python
  print(d.values())  # [1, 2, 3]
  ```
* 👫 同時拿 key 和 value

  ```python
  print(d.items())  # [('a', 1), ('b', 2), ('c', 3)]
  ```

### ✍️ CRUD 操作

C = Create 新增
U = Update 修改
R = Read 讀取
D = Delete 刪除

```python
# 新增
d["d"] = 4

# 修改
d["a"] = 40

# 刪除
d.pop("a")
```

---

## 🖼️ 圖片小玩具 (Streamlit)

我學到可以用 **Streamlit** 把圖片放到網頁上！

```python
import streamlit as st

st.title("圖片展示")
st.image("image/金小胖.png", width=300)
```

- 可以用 `st.number_input` 改圖片大小
- 可以用 `st.selectbox` 做下拉選單選圖片
- 還能用迴圈顯示整個資料夾的圖片 ✨

---

## 🛒 購物網站小專案

我做了一個簡單的購物網站：

- 🖼️ 每個商品有圖片
- 💰 有價格
- 📦 有庫存
- 🛍️ 點「購買」會扣庫存
- 🪄 特殊商品「金小胖」只能買一次

這些功能讓我覺得超像自己在蓋網路商店！

---

## 🔄 函式 (function)

函式就像一台「小機器」，可以重複做事情。

```python
def hello():
    print("Hello, world!")
```

呼叫 `hello()` → 就會印出 Hello, world!

### 有參數的函式

```python
def hello(name):
    print(f"Hello, {name}!")

hello("Alice")  # Hello, Alice!
```

---

## ➕ ➖ 加法和減法函式

```python
def add(a, b):
    return a + b

print(add(3, 4))  # 7
```

還能寫一個會判斷的函式：

```python
def add_sub(a, b):
    if a > b:
        return a + b
    else:
        return a - b
```

---

# 🎯 我的學習收穫

1. 學會字典，像是在管理「小倉庫」。
2. 學會用 Streamlit，把程式變成網頁，還能展示圖片。
3. 自己做了一個小小購物網站，超有成就感！
4. 學到函式，讓程式可以重複使用，不用一樣的東西寫一百遍。

---
