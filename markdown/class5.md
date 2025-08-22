---
# 🖥 我的程式學習重點整理（含系統指令）
---

## 🌟 1. 預設參數

有時候函式可以有「預設的數字或文字」。
如果我沒有特別給它數字或文字，它就會自動用預設的。

```python
def hello(name, message="Hello"):
    print(f"{message}, {name}!")

hello("Alice")          # 沒有給 message，就用 "Hello"
hello("Bob", "早安")    # 有給 message，就用 "早安"
```

💡 就像買飲料，沒說要加什麼糖，店員就幫你用「正常甜」。

---

## 🔢 2. 限制參數的型態

在函式裡，我可以告訴電腦：「這個數字只能是整數」或「這要是文字」。

```python
def add(a: int, b: int = 0) -> int:
    return a + b

print(add(1, 2))            # 會得到 3
print(add("hi", "world"))   # 這樣其實不太對
```

💡 型態提示就像遊戲規則，不能亂用，才不會出錯。

---

## 📦 3. 區域變數 vs 全域變數

- **區域變數**：在函式裡的小秘密，用完就消失。
- **全域變數**：全世界都看得到。

```python
length = 5  # 全域變數

def calculate_square_area():
    area = length**2  # area 只在函式裡能用
    print("面積是:", area)

calculate_square_area()   # 25
print(length)             # 可以印 5
# print(area)  # ❌ 出錯！因為 area 在外面用不到
```

💡 就像房間裡的零食（區域），只有你自己能吃；
放在客廳桌上的零食（全域），大家都能吃。

---

## 🌍 4. 使用 `global` 修改全域變數

如果真的要在函式裡改外面的變數，要用 `global`。

```python
length = 5
area = 0

def calculate_square_area():
    global area
    area = length**2

calculate_square_area()
print("面積是:", area)   # 25
```

💡 但要小心，全域變數亂改會讓程式很難懂。

---

## 📖 5. 函式的說明文件

我可以在函式裡加「說明書」，讓別人知道這個函式怎麼用。

```python
def hello(name: str):
    """
    這是一個打招呼的函式
    參數:
        name: str - 姓名
    回傳:
        None
    範例:
        hello("Alice")
    """
    print(f"Hello, {name}!")
```

💡 就像玩具盒裡的說明書，讓人一看就懂怎麼玩。

---

## 🤖 6. OpenAI API 聊天

我學會怎麼讓電腦跟我聊天！
用 `openai` 可以呼叫 AI，讓它回我訊息。

```python
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# 🚦 系統指令（這是 AI 一開始的規則）
history = [{"role": "system", "content": "請用繁體中文對話"}]

while True:
    user_input = input("你：")
    if user_input == "exit":
        break
    history.append({"role": "user", "content": user_input})

    response = openai.chat.completions.create(
        model="gpt-5-mini",
        messages=history
    )

    assistant_message = response.choices[0].message.content
    print("AI：", assistant_message)
    history.append({"role": "assistant", "content": assistant_message})
```

💡 系統指令就像規則書，AI 要先照這個規則，才開始對話。

---

## 💬 7. Streamlit 聊天介面

我還會用 `streamlit` 把聊天做成網頁，變成對話泡泡。

```python
import streamlit as st

st.chat_message("user").write("這是使用者的訊息")
st.chat_message("assistant").write("這是AI的回應")


history = [
    {"role": "user", "content": "1"},
    {"role": "assistant", "content": "2"},
    {"role": "user", "content": "3"},
    {
        "role": "assistant",
        "content": "st.chat_message()可以讓你用聊天泡泡的方式呈現訊息喔!",
    },
]

for message in history:
    if message["role"] == "user":
        st.chat_message("user", avatar="😁").write(message["content"])
    else:
        st.chat_message("assistant", avatar="😲").write(message["content"])
```

💡 就像手機聊天室，對話會一格一格出來。

---

## 🗑 8. 儲存與清除聊天紀錄

我可以讓程式記住之前的聊天，
也可以按下垃圾桶清掉，重新開始。

```python
import streamlit as st
from openai import OpenAI

# 初始化 OpenAI 客戶端
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
ss = st.session_state

# 🚦 系統指令（初始化 AI 規則）
if "history" not in ss:
    ss.history = [{"role": "system", "content": "請用繁體中文對話"}]

# 版面：左邊對話區，右邊清除按鈕
col_chat, col_clear = st.columns([9, 1])

with col_clear:
    if st.button("🗑"):
        # 🚦 系統指令（清除後重新給規則）
        ss.history = [{"role": "system", "content": "請用繁體中文對話"}]
        st.rerun()  # 清空並刷新頁面

# 顯示對話紀錄
with col_chat:
    for message in ss.history:
        if message["role"] == "user":
            st.chat_message("user", avatar="😁").write(message["content"])
        elif message["role"] == "assistant":
            st.chat_message("assistant", avatar="😲").write(message["content"])

# 輸入框
prompt = st.chat_input("請輸入訊息...")
if prompt:
    ss.history.append({"role": "user", "content": prompt})

    # 呼叫 OpenAI API
    response = client.chat.completions.create(model="gpt-5-mini", messages=ss.history)

    assistant_message = response.choices[0].message.content

    # 存回歷史紀錄
    ss.history.append({"role": "assistant", "content": assistant_message})
    st.rerun()
```

💡 就像聊天室，可以清除紀錄再重新開始聊天。

---

# 🎉 總結

這次我學到的東西有：

1. **函式的預設參數**
2. **限制變數型態**
3. **全域變數 vs 區域變數**
4. **怎麼用 global 修改全域變數**
5. **幫函式加說明書**
6. **用 OpenAI API 聊天（🚦 系統指令一定要先設定）**
7. **用 Streamlit 做聊天網頁（🚦 系統指令要放在歷史紀錄最前面）**
8. **清除聊天紀錄（清除後還要重新加 🚦 系統指令）**

💡 總之，系統指令 🚦 就是 **AI 的規則書**，一定要放在最前面，讓 AI 知道要怎麼回答。

---
