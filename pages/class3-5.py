# 導入 random 模組，用於產生隨機數
import random

# 導入 streamlit 函式庫，用於建立網頁應用程式，並使用 st 作為簡稱
import streamlit as st

# 從 streamlit 中導入 session_state，用於在多次互動之間保存變數狀態，並使用 ss 作為簡稱
from streamlit import session_state as ss

# --- 狀態初始化 ---
# 檢查 session_state 中是否已經有 'ans' (答案) 這個變數
# 如果沒有 (通常是遊戲剛開始時)，就執行以下程式碼
if "ans" not in ss:
    # 產生一個 1 到 100 之間的隨機整數作為答案，並存入 session_state
    ss.ans = random.randint(1, 100)

# 檢查 session_state 中是否已經有 'max_num' (猜測範圍的最大值)
if "max_num" not in ss:
    # 如果沒有，就將最大值初始化為 100
    ss.max_num = 100

# 檢查 session_state 中是否已經有 'min_num' (猜測範圍的最小值)
if "min_num" not in ss:
    # 如果沒有，就將最小值初始化為 1
    ss.min_num = 1

# --- 網頁介面 ---
# 在網頁上顯示主標題 "猜數字遊戲"
st.title("猜數字遊戲")

# 建立一個數字輸入框，提示文字會動態顯示目前的猜測範圍
# f-string 會將 ss.min_num 和 ss.max_num 的值放入字串中
# 使用者輸入的數字會被儲存在 num 變數中
num = st.number_input(f"請輸入一個介於 {ss.min_num} 和 {ss.max_num} 之間的數字: ")

# --- 遊戲邏輯 ---
# 建立一個名為 "猜測" 的按鈕
# 只有當使用者點擊此按鈕時，下面的程式碼才會執行
if st.button("猜測"):
    # 判斷使用者輸入的數字 (num) 是否大於答案 (ss.ans)
    if num > ss.ans:
        # 如果是，在網頁上顯示提示訊息
        st.write("你猜的數字太大了！")
        # 為了縮小範圍，檢查使用者輸入的數字是否比目前的上限小
        if num < ss.max_num:
            # 如果是，就更新上限為使用者這次猜的數字
            ss.max_num = int(num)
    # 如果不大於，就判斷是否小於答案
    elif num < ss.ans:
        # 如果是，在網頁上顯示提示訊息
        st.write("你猜的數字太小了！")
        # 為了縮小範圍，檢查使用者輸入的數字是否比目前的下限大
        if num > ss.min_num:
            # 如果是，就更新下限為使用者這次猜的數字
            ss.min_num = int(num)
    # 如果既不大於也不小於，就表示猜對了
    else:
        # 在網頁上顯示恭喜訊息
        st.write("恭喜你猜對了！")
        # 觸發 Streamlit 的氣球慶祝特效
        st.balloons()
