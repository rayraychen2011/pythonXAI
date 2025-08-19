import streamlit as st  # 匯入 Streamlit 模組並重新命名為 st，方便後續呼叫 streamlit 的函式

# st.number_input() 可以讓使用者在網頁上輸入數字
# 參數說明:
# - 第一個參數為顯示在介面的提示字串
# - step=1 表示步進為 1，使用者每次增減為整數，適合限制為整數輸入
# - min_value=0 設定可輸入的最小值為 0
# - max_value=100 設定可輸入的最大值為 100
# - value=50 設定預設值為 50
number = st.number_input("請輸入一個數字", step=1, min_value=0, max_value=100, value=50)

# st.write() 可以在網頁上顯示文字，支援基本的 Markdown 語法
# 根據輸入的分數範圍輸出對應的等級。
# 分數到等級對應規則:
# - 小於 60 -> F
# - 60 至 69 -> D
# - 70 至 79 -> C
# - 80 至 89 -> B
# - 90 以上 -> A
if number < 60:
    st.write("F")  # 分數 < 60 顯示 F
elif number < 70:
    st.write("D")  # 60 <= 分數 < 70 顯示 D
elif number < 80:
    st.write("C")  # 70 <= 分數 < 80 顯示 C
elif number < 90:
    st.write("B")  # 80 <= 分數 < 90 顯示 B
else:
    st.write("A")  # 90 <= 分數 顯示 A


st.write("---")
st.write("### 按鈕練習")
# 使用 st.button() 在網頁上顯示一個按鈕，使用者可以點擊
# 說明：
# - 第一個參數為按鈕上顯示的文字
# - key 用來指定按鈕的識別名稱，可區分多個按鈕
# - st.button() 在按下時會回傳 True，否則回傳 False
# 範例使用：先建立一個按鈕（此按鈕無回傳處理），僅示範按鈕外觀
st.button("按我一下", key="button1")

# 當按下按鈕並回傳 True 時，可在條件內呼叫動畫或其他函式
# 範例：按下後顯示氣球動畫
if st.button("按我一下", key="balloons"):
    st.balloons()  # 按下後觸發氣球動畫

# 範例：按下後顯示雪花動畫
if st.button("按我一下", key="snow"):
    st.snow()  # 按下後觸發雪花動畫
st.write("---")
