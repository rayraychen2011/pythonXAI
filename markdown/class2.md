---
# 🖥️ 我的程式學習筆記
---

## 🔎 比較運算子（誰大誰小？一不一樣？）

👉 比較運算子就是讓電腦幫我們檢查兩個東西，看看它們是不是一樣，或者誰比較大。

- `==` 等於
  `print(1 == 1)` ➝ True ✅

- `!=` 不等於
  `print(1 != 1)` ➝ False ❌

- `>` 大於
  `print(2 > 1)` ➝ True

- `<` 小於
  `print(1 < 3)` ➝ True

- `<=` 小於等於
  `print(5 <= 5)` ➝ True

- `>=` 大於等於
  `print(7 >= 6)` ➝ True

---

## 🧠 邏輯運算子（條件魔法）

有時候我們要同時檢查很多條件，就要用這些小工具：

- `and`：兩個條件都要對，才會是 True
- `or`：只要有一個對，就是 True
- `not`：把 True 變 False，把 False 變 True（顛倒魔法 ✨）

例子：

```python
print(True and False)  # False
print(True or False)   # True
print(not True)        # False
```

---

## 🏆 運算優先順序（誰先算？）

電腦有一個「算式規則」，就像數學一樣：

1. 括號 `()`
2. 次方 `**`
3. 乘除 `% // * /`
4. 加減 `+ -`
5. 比較運算子 `== != > < >= <=`
6. `not`
7. `and`
8. `or`

---

## 🔐 密碼檢查（if / elif / else）

我們可以用 `if` 來做判斷，像是輸入密碼的遊戲。

```python
password = input("請輸入密碼：")
if password == "0423":
    print("密碼正確，歡迎進入！")
elif password == "1120":
    print("管理員密碼正確！")
else:
    print("密碼錯誤！")
```

---

## 🌐 Streamlit 小工具（做互動網頁）

1. **輸入數字**

```python
number = st.number_input("請輸入一個數字", step=1, min_value=0, max_value=100, value=50)
```

2. **顯示成績**

```python
if number < 60:
    st.write("F")
elif number < 70:
    st.write("D")
elif number < 80:
    st.write("C")
elif number < 90:
    st.write("B")
else:
    st.write("A")
```

3. **按鈕+動畫 🎈❄️**

```python
if st.button("按我一下", key="balloons"):
    st.balloons()

if st.button("按我一下", key="snow"):
    st.snow()
```

---

## 🔁 for 迴圈（重複做事情）

就像數數字一樣，電腦會幫我們重複跑。

```python
for i in range(5):
    print(i)  # 印出 0,1,2,3,4
```

也可以自己設定範圍：

```python
for i in range(1, 5):
    print(i)  # 1,2,3,4
```

---

## 🔢 數字金字塔

```python
number = st.number_input("請輸數字1-9", step=1, min_value=1, max_value=9, value=1)
for i in range(1, number + 1):
    st.write(str(i) * i)
```

輸入 5 →

```
1
22
333
4444
55555
```

---

## 📋 List（清單）

清單就像一個資料盒，可以放很多東西。

```python
print([1, 2, 3])
print([1, 2, 3, "a", "b"])
```

👉 **取資料（Read）**

```python
L = [1, 2, 3, "a"]
print(L[0])  # 1
print(L[1])  # 2
```

👉 **改資料（Update）**

```python
L[0] = 99
print(L)  # [99, 2, 3, 'a']
```

👉 **刪資料（Delete）**

```python
L.remove("a")
L.pop(0)
```

---

## 📂 檔案操作

- `r` 讀取
- `w` 寫入（會覆蓋原本）
- `a` 加在後面

```python
with open("class1-1.py", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

---

## 📝 小結論

- 比較運算子 ➝ 誰大誰小？
- 邏輯運算子 ➝ 條件魔法！
- if / elif / else ➝ 做選擇
- for ➝ 重複做事
- list ➝ 資料盒
- 檔案 ➝ 讀寫小幫手
- Streamlit ➝ 做互動網頁，還能放動畫 🎈❄️

---
