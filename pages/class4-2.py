import streamlit as st

import os  # 用來操作檔案和資料夾路徑

# 設定網頁標題
st.title("圖片元件")

# 顯示單張圖片
# st.image(圖片路徑, width=寬度)
st.image(
    "image/金小胖.png", width=300
)  # 顯示 image 資料夾下的金小胖.png，寬度設為 300 像素

# 使用者可以透過數字輸入調整圖片大小
image_size = st.number_input(
    "圖片大小",  # 顯示在網頁上的標籤
    min_value=50,  # 最小值
    max_value=500,  # 最大值
    step=50,  # 每次增減的步進
    value=100,  # 預設值
)

# 假設你已經定義 image_folder 和 image_files
image_folder = "image"
image_files = os.listdir(image_folder)  # 取得資料夾下所有檔案

# 迴圈顯示資料夾內所有圖片，寬度為使用者設定
for image_file in image_files:
    st.image(f"{image_folder}/{image_file}", width=image_size)

# 迴圈顯示資料夾內所有圖片，寬度自動調整為容器寬度
for image_file in image_files:
    # use_container_width=True 會自動調整圖片寬度符合 Streamlit 容器
    st.image(f"{image_folder}/{image_file}", use_container_width=True)

# 建立一個下拉選單，讓使用者從 image_files 中選擇圖片
# "選擇圖片" 是顯示在網頁上的標籤
# index=0 表示預設選擇第一張圖片
selected_image = st.selectbox("選擇圖片", image_files, index=0)

# 顯示使用者選擇的圖片
# f"{image_folder}/{selected_image}" 是圖片完整路徑
# width=300 設定圖片寬度為 300 像素
st.image(f"{image_folder}/{selected_image}", width=300)
