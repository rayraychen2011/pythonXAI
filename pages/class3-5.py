import streamlit as st
import random  # 導入 random 模組以產生隨機數

# 產生一個 1 到 100 的隨機整數作為答案
ans = random.randint(1, 100)

# 最大值與最小值的範圍限制，初始為 1 到 100
max_num = 100
min_num = 1
num = st.number_input("輸入數字", min_num=1, max_num=100, step=1)
while True:
    # 讓使用者輸入一個介於 min_num 和 max_num 之間的整數
    # input() 會回傳字串，使用 int() 轉換為整數
    num = int(input(f"請輸入一個介於 {min_num} 和 {max_num} 之間的數字: "))

    # 當使用者猜的數字比答案大時
    if num > ans:
        st.write("猜的數字太大了")
        # 若猜的數字小於目前的最大值，則更新最大值為猜的數字
        if num < max_num:
            max_num = num
    # 當使用者猜的數字比答案小時
    elif num < ans:
        st.write("猜的數字太小了")
        # 若猜的數字大於目前的最小值，則更新最小值為猜的數字
        if num > min_num:
            min_num = num
    else:
        # 相等代表猜對了，結束迴圈
        st.write("恭喜你猜對了！")
        break
