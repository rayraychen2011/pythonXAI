import streamlit as st
import streamlit as st
import streamlit as st

# 最小化且只使用教材已出現的語法與 st API 的學習筆記

st.title("程式學習筆記（依課堂出現之內容）")

st.markdown("## 1 — 基本型態")
st.write("整數 (int)、浮點數 (float)、字串 (str)、布林 (bool)。")
st.markdown("**範例**")
st.markdown(
    """
```python
print(1)        # int
print(1.23)     # float
print('apple')  # str
print(True)     # bool
```
"""
)

st.markdown("## 2 — 變數與賦值")
st.write("把資料放進變數，方便重複使用與閱讀程式。")
st.markdown("**範例**")
st.markdown(
    """
```python
num = 10
word = 'apple'
flag = True
print(num, word, flag)
```
"""
)

st.markdown("## 3 — 運算子與優先順序")
st.write("常用運算子：+ - * / // % **。優先順序會影響計算結果，可用括號調整。")
st.markdown("**範例**")
st.markdown(
    """
```python
print(1 + 1)
print(2 * 3)
print(2 ** 3)
```
"""
)

st.markdown("## 4 — 字串操作與格式化")
st.write("字串可以相加或重複；教材中示範過 f-string（格式化字串）。")
st.markdown("**範例**")
st.markdown(
    """
```python
print('apple' + 'pen')
print('apple' * 3)
name = '小明'
age = 18
print(f"My name is {name} and I am {age} years old.")
```
"""
)

st.markdown("## 5 — 型態檢查與轉換")
st.write("使用 type() 查看型態；用 int()/float()/str()/bool() 做轉換。")
st.markdown("**範例**")
st.markdown(
    """
```python
print(type(1))
print(int(1.234))
print(float('1.234'))
print(str(123))
print(len('apple'))
```
"""
)

st.markdown("## 6 — 長度與終端輸入（教材示範）")
st.write(
    "課堂有示範 input() 在終端機的範例；下方僅以程式碼區塊展示（網頁使用時請改用對應的輸入元件）。"
)
st.markdown("**範例（終端機）**")
st.markdown(
    """
```python
# 終端機輸入範例（教材）
name = input('請輸入你的名字: ')
print('你好，' + name + '!')

# 半徑轉換範例
r = input('請輸入圓的半徑: ')
area = 3.14 * float(r) * float(r)
print('圓面積為', area)
```
"""
)

st.markdown("## 7 — 條件判斷（if / elif / else）")
st.write("教材示範了用 if/elif/else 判斷分數或密碼，這裡展示簡短範例。")
st.markdown("**範例**")
st.markdown(
    """
```python
password = input('請輸入密碼: ')
if password == '0423':
    print('密碼正確')
elif password == '1120':
    print('管理員密碼')
else:
    print('密碼錯誤')
```
"""
)

st.markdown("## 8 — 迴圈（for）")
st.write(
    "使用 for 搭配 range 或其他可疊代物件做重複操作；教材示過 range(n)、range(start, end) 與 step。"
)
st.markdown("**範例**")
st.markdown(
    """
```python
for i in range(5):
    print(i)

for i in range(1, 5, 2):
    print(i)
```
"""
)
st.markdown("**進階示例（教材提及）**")
st.markdown(
    """
```python
# 以 list 直接迭代
L = [1, 2, 3]
for item in L:
    print(item)

# 以 index 與 len() 迭代（可搭 step）
for i in range(0, len(L), 2):
    print(L[i])
```
"""
)

st.markdown("## 9 — 清單（list）與基本操作")
st.write(
    "教材示範 list 的建立、索引、切片、len() 與簡單的新增/更新/刪除（remove/pop）範例）。"
)
st.markdown("**範例**")
st.markdown(
    """
```python
L = [1, 2, 3, 'a', 'b', 'c']
print(L[0])        # 取 index 0
print(L[0::2])     # 切片
print(len(L))      # 長度
L[0] = 2           # 更新
L.remove('a')      # 刪除第一個 'a'
L.pop()            # 刪除最後一個
```
"""
)
st.markdown("**補充（教材中有提）**")
st.markdown(
    """
```python
# 多參數 print：以空格分隔輸出
print(1, True, 'a', 1.23)

# 切片範例：start:stop:step
L = [1,2,3,'a','b','c']
print(L[1:4])      # index 1~3
print(L[0::2])     # every 2nd element

# 複製 list（避免直接指派造成共用參考）
a = [1,2,3]
b = a.copy()
b[0] = 9
print(a, b)

# 在迭代中刪除元素要小心，教材示範了可能副作用
L = ['a','b','c','a']
for i in L:
    if i == 'a':
        L.remove(i)  # 教材指出此做法會有副作用，實務上建議改用 list comprehension
print(L)
```
"""
)

st.markdown("## 10 — 檔案讀寫（教材有示範）")
st.write("教材示範了 open() 基本模式與 with open(...) 的自動關閉用法。")
st.markdown("**範例**")
st.markdown(
    """
```python
# 以 open 讀檔（簡單示範）
f = open('pages/class1-1.py', 'r', encoding='utf-8')
content = f.read()
print(content)
f.close()

# 使用 with 自動關閉
with open('pages/class1-1.py', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
```
"""
)

st.markdown("## 11 — 比較與邏輯運算（教材範例）")
st.markdown(
    """
```python
# 比較運算
print(1 == 1)
print(1 != 1)
print(1 > 1)
print(1 < 1)
print(1 <= 1)
print(1 >= 1)

# 邏輯運算
print(True and False)
print(True or False)
print(not True)
```
"""
)

st.markdown("## 12 — Streamlit 小元件（教材範例）")
st.write("教材範例出現過以下互動元件，於網頁互動時可使用：")
st.markdown(
    """
```python
# 數字輸入
number = st.number_input('請輸入一個數字', step=1, min_value=0, max_value=100, value=50)

# 按鈕與互動
if st.button('按我一下', key='balloons'):
    st.balloons()

st.button('按我一下', key='button1')
```
"""
)

st.markdown("---")
st.write(
    "本手冊僅包含 `pages/` 教材中已出現的語法與 API（例如 f-string、input、len、type、int/float/str/bool、if/elif/else、for、range，以及 st.title/st.write/st.text/st.markdown）。\n\n若教材新增語法，下一次掃描會自動納入。"
)
