import streamlit as st
from openai import OpenAI

# 初始化 OpenAI 客戶端
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# 簡化 session_state 存取
ss = st.session_state

# 如果還沒有對話紀錄，就先建立
if "history" not in ss:
    ss.history = [{"role": "system", "content": "請用繁體中文進行後續對話"}]

# 版面：左邊對話區，右邊清除按鈕
col_chat, col_clear = st.columns([9, 1])

with col_clear:
    if st.button("🗑"):
        ss.history = [
            {"role": "system", "content": "請用繁體中文進行後續對話"}
        ]  # 這是系統指令"請用繁體中文進行後續對話"
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
