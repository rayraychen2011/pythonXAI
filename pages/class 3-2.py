import streamlit as st

st.title("點餐機")
text = st.text_input("輸入文字", value="這是預設文字")
st.write(f"你輸入的文字是：{text}")
