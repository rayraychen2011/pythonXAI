import streamlit as st

# 設定網頁標題
st.title("點餐機")

# 使用 Streamlit 的 session_state 來儲存使用者的訂單列表
# 如果 session_state 中還沒有 'order'，就初始化為空列表
if "order" not in st.session_state:
    st.session_state.order = []

# 方便用一個變數存取 session 中的訂單
ss_order = st.session_state.order

# 建立兩欄的輸入區塊：左欄輸入餐點名稱，右欄放按鈕來加入餐點
col1, col2 = st.columns(2)
with col1:
    # text_input 會顯示一個文字輸入框，使用者可以輸入餐點名稱
    dishes = st.text_input("請輸入餐點")

with col2:
    # 按下按鈕時，將輸入的餐點加入訂單列表
    if st.button("加入餐點", key="add_order"):
        ss_order.append(dishes)

# 顯示購物車標題
st.title("購物車")

# 使用迴圈列出所有已加入的餐點
for i in range(len(ss_order)):
    # 每一項使用兩欄顯示：左欄顯示餐點名稱，右欄顯示刪除按鈕
    col1, col2 = st.columns(2)
    with col1:
        # 顯示第 i 項餐點
        st.write(ss_order[i])
    with col2:
        # 如果按下刪除按鈕，就從列表中移除該項，並重新執行以更新畫面
        if st.button("刪除", key=f"{i}"):
            ss_order.pop(i)
            st.rerun()  # 刪除後重新執行以更新畫面
