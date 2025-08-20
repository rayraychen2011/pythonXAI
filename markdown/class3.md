---

# 📘 我的程式學習筆記

## 🖥️ Streamlit 基本用法

* `st.title("標題")` → 在網頁上放大大的標題。
* `st.write("文字")` → 在網頁上顯示文字。
* `st.button("按鈕")` → 放一顆可以按的按鈕。

---

## 🧩 欄位 (columns) 排版

- `st.columns(2)` → 把畫面切成左右兩欄。

  ```python
  col1, col2 = st.columns(2)
  col1.button("按鈕1")
  col2.button("按鈕2")
  ```

  👉 左邊一顆按鈕、右邊一顆按鈕。

- 欄位可以用比例：

  ```python
  col1, col2 = st.columns([1,2])
  ```

  👉 右邊比左邊大兩倍。

- 也可以有三欄：`st.columns([1,2,3])`。

- `with col1:` → 把東西放到特定的欄位。

  ```python
  with col1:
      st.write("這是col1")
      st.button("按鈕")
  ```

---

## 🔢 輸入數字

- `st.number_input("輸入數字", min_value=1, value=4, step=1)`
  👉 出現一個可以輸入數字的小框框。
- 輸入多少，就會出現幾個欄位，每欄放一顆按鈕。

---

## 🎈 小互動

- `st.balloons()` → 點按鈕會放氣球。
- `st.rerun()` → 重新整理整個畫面。

---

## 📦 session_state (記憶功能)

- `st.session_state` → 用來記住資料，不會因為重整而消失。

  ```python
  if "ans" not in st.session_state:
      st.session_state.ans = 1
  ```

  👉 如果還沒有 ans，就先幫它設成 1。

- 每按一次按鈕：

  ```python
  st.session_state.ans += 1
  ```

  👉 數字就會 +1，而且不會被重設。

---

## ✍️ 文字輸入

- `st.text_input("輸入文字", value="預設文字")`
  👉 出現一個文字框，可以打字。

---

## 🍔 點餐機小程式

1. 輸入餐點名稱。
2. 按「加入餐點」，會跑到購物車裡。
3. 購物車裡的餐點可以按「刪除」移除。

---

## ➕ 算數運算

像數學一樣：

- `+=` 加法
- `-=` 減法
- `*=` 乘法
- `/=` 除法
- `//=` 取整數
- `%=` 取餘數
- `**=` 次方

⚡ 運算順序：

1. () 括號
2. \*\* 次方
3. - / % //
4. - -
5. \== > <
6. not
7. and
8. or
9. \= += -= …

---

## 🔁 迴圈

- `while` → 一直重複，直到條件不成立。

  ```python
  i = 0
  while i < 5:
      print(i)
      i += 1
  ```

- `for` → 重複指定次數。

  ```python
  for i in range(5):
      print(i)
  ```

- `break` → 提早跳出迴圈。

---

## 🎲 random 隨機

- `random.randrange(7)` → 0 \~ 6 隨機數。
- `random.randint(1, 10)` → 1 \~ 10 隨機數。

---

## 🎮 猜數字遊戲

1. 電腦想一個 1 到 100 的數字。
2. 玩家輸入數字。
3. 電腦會回應「太大」「太小」或「猜對了」。
4. 範圍會越來越小，直到答對。

---

📓 **總結**：
我學會了怎麼用 **Streamlit** 做網頁，放按鈕、輸入框、購物車，還有怎麼用 **Python 的運算、迴圈和隨機** 來做小遊戲！

---
