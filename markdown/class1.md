---

# 🐍 我的 Python 學習筆記

## ✏️ 註解 (Comment)

* `#` 開頭的東西不會被電腦執行，只是給人看的。
* 快速鍵：

  * **單行**：`Ctrl + ?`
  * **多行**：框起來再 `Ctrl + ?`

---

## 🔢 基本型態 (Data Type)

- **整數 int**：`1, -1, 0, 2, 3...`
- **小數 float**：`1.0, 1.234`
- **字串 str**：`"apple", "1"`
- **布林 bool**：`True, False`

```python
print(1)         # 整數
print(1.23)      # 小數
print("apple")   # 字串
print(True)      # 布林
```

---

## 📦 變數 (Variable)

- 就像小盒子，可以裝資料。
- `=` 把右邊的東西放進左邊的盒子。

```python
a = 10
print(a)   # 顯示10
a = "apple"
print(a)   # 顯示apple
```

---

## ➕ 運算子 (Operators)

```python
1 + 1   # 加法
1 - 1   # 減法
1 * 1   # 乘法
1 / 1   # 除法
1 // 1  # 整數除法 (取商)
1 % 1   # 取餘數
2 ** 3  # 次方 (2的3次方=8)
```

👉 **先後順序**：括號 > 次方 > 乘除 > 加減

---

## 🔤 字串 (String)

```python
print("apple" + "pen")   # 字串相加
print("apple" * 3)       # 重複字串
```

---

## 📝 f-string (字串插入變數)

```python
name = "apple"
age = 18
print(f"My name is {name}, I am {age} years old.")
```

👉 `{}` 會把變數的值放進去。

---

## 📏 常用函式

- `len()`：算長度
- `type()`：看型態

```python
print(len("apple"))   # 5
print(type(1))        # int
```

---

## 🔄 型態轉換

```python
int(1.0)     # 小數 → 整數
float(1)     # 整數 → 小數
str(1)       # 整數 → 字串
bool(1)      # 整數 → 布林
float("1.2") # 字串 → 小數
```

---

## 🎮 輸入 input()

```python
a = input("請輸入一個數字: ")
print(int(a) + 10)   # 把輸入的數字+10
```

⚠️ `input()` 讀到的東西**一定是字串**。

---

## 🔵 圓形面積小程式

```python
r = input("請輸入半徑: ")
print(f"圓的面積是: {3.14 * float(r) * float(r)}")
```

---

## 🌐 Streamlit (做網頁)

```python
import streamlit as st

st.title("這是標題")    # 顯示大標題
st.write("這是一般文字") # 顯示多種格式
st.text("純文字")
st.markdown("""
* **粗體**
* *斜體*
* [連結](https://www.example.com)
""")
```

---

# 🎯 總結

- 註解是**旁邊的筆記**，不會跑程式。
- 基本型態有：整數、小數、字串、布林。
- 變數像**小盒子**，可以放東西。
- 運算子可以**加減乘除**，還有取商、取餘數、次方。
- f-string 可以把變數放到字串裡。
- `len()` 算長度，`type()` 看型態。
- `input()` 會把輸入的東西存成字串。
- Streamlit 可以讓 Python 做成網頁。

---
