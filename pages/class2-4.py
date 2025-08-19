# 引入 Streamlit 套件，方便建立互動式網頁介面
import streamlit as st

# 在網頁上顯示標題文字
st.write("數字金字塔")

# 建立數字輸入框，讓使用者輸入要顯示到哪個數字 (1-9)
# 參數說明:
# "請輸數字1-9" -> 顯示給使用者的提示訊息
# step=1 -> 每次增減的步幅為 1
# min_value=1, max_value=9 -> 限制輸入範圍為 1 到 9
# value=1 -> 預設值為 1
number = st.number_input("請輸數字1-9", step=1, min_value=1, max_value=9, value=1)

# 使用 for 迴圈從 1 迭代到使用者輸入的數字 (包含 number)
# range(1, number + 1) 右側要 +1 才會包含 number 本身
for i in range(1, number + 1):
    # 將整數 i 轉為字串後重複 i 次，例如 i=3 -> "3" * 3 = "333"
    # st.write 會在網頁上顯示每一列的字串，依序顯示出金字塔狀
    st.write(str(i) * i)
