import streamlit as st

# 標題：展示欄位（columns）元件使用方式
st.title("欄位元件")

# 建立兩個等寬的欄位，st.columns 傳入整數 2 會回傳兩個 column 物件
col1, col2 = st.columns(2)  # col1, col2 都是 column 物件
col1.button("按鈕1", key="btn1")  # 在 col1 放一個按鈕
col2.button("按鈕2", key="btn2")  # 在 col2 放一個按鈕

# 2 columns，可以用不同的比例設定欄位寬度，將比例放到列表中
# 這裡第一欄寬度為 1，第二欄寬度為 2（第二欄較寬）
col1, col2 = st.columns([1, 2])
col1.button("按鈕3", key="btn3")
col2.button("按鈕4", key="btn4")

# 3 columns，傳入三個比例值，回傳三個 column 物件
col1, col2, col3 = st.columns([1, 2, 3])
col1.button("按鈕5", key="btn5")
col2.button("按鈕6", key="btn6")
col3.button("按鈕7", key="btn7")
st.write("---")  # 顯示水平分隔線

# 使用 with 區塊把元件放入特定的 column 裡面
col1, col2 = st.columns([1, 2])
with col1:
    st.write("這是col1")  # 在 col1 顯示文字
    # 如果按下按鈕會顯示氣球動畫
    if st.button("按鈕8", key="btn8"):
        st.balloons()
with col2:
    st.write("這是col2")  # 在 col2 顯示文字
    st.button("按鈕9", key="btn9")  # 在 col2 放一個按鈕


# 使用 number_input 讓使用者輸入欄位數量 (int)
# min_value 最小值為 1，預設值 value=4，步進 step=1
n = st.number_input("輸入數字", min_value=1, value=4, step=1)
cols = st.columns(n)  # 根據輸入的數字建立對應數量的欄位（回傳 list）
for i in range(len(cols)):
    with cols[i]:
        # 在每個動態建立的欄位中放按鈕，按鈕 key 保持唯一
        st.button(f"for當中的按鈕{i+1}", key=f"多col{i+10}")
        # 這裡按鈕的 key 範例: 多col10, 多col11, ...

st.write("---")  # 分隔線
st.title("columns排列元件效果比較")
# 示範單一 row 下兩個 column 的排列差異
col1, col2 = st.columns(2)
with col1:
    st.button("按鈕1", key="btn10")
    st.button("按鈕2", key="btn11")
    st.button("按鈕3", key="btn12")
with col2:
    # 在另一欄放多個文字，觀察排列效果
    st.write("這是col2")
    st.write("這是col2")
    st.write("這是col2")
st.write("---")  # 分隔線

# 使用迴圈建立多組欄位來測試排版
for i in range(3):
    col1, col2 = st.columns(2)
    with col1:
        st.button(f"按鈕{i+1}", key=f"排版測試{i+4}")
    with col2:
        st.write(f"這是col2-{i+1}")
st.write("---")  # 分隔線

st.title("session_state")  # 標題：示範 session_state 用法
# 本地變數示例：按鈕觸發時 ans 會遞增，但每次重新執行腳本時會重置
ans = 1
if st.button("按下去ans+1", key="btn_ans"):
    ans = ans + 1
st.write(f"ans={ans}")  # 顯示目前 ans 的值

# 使用 st.session_state 保持跨互動的狀態（持久化）
if "ans" not in st.session_state:
    st.session_state.ans = 1  # 初始化 session_state 中的 ans
if st.button("按下去ans+1", key="btn_ans2"):
    st.session_state.ans = st.session_state.ans + 1  # 更新 session_state
st.write(f"ans={st.session_state.ans}")  # 顯示 session_state 中的 ans

# 有時候按按鈕不會自動重新整理畫面，這時可呼叫 st.rerun() 強制重新執行
if st.button("重新整理畫面", key="banana"):
    st.rerun()  # 重新執行應用以更新畫面
