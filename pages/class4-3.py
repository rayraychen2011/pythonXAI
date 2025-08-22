import streamlit as st
import os
import time  # 用來模擬購買延遲

# 簡化操作 session_state
ss = st.session_state

# 設定圖片資料夾
image_folder = "image"
# 取得資料夾下所有檔案名稱
image_files = os.listdir(image_folder)

# 初始化商品資料，如果 session_state 裡還沒有 products
if "products" not in ss:
    ss.products = {}

# 將資料夾圖片建立成商品
for image_file in image_files:
    # 商品名稱取圖片檔名（去掉副檔名）
    product_name = image_file[:-4]
    # 如果 session_state.products 裡還沒有這個商品，就加入
    if product_name not in ss.products:
        ss.products[product_name] = {
            "price": 10,  # 商品價格
            "stock": 10,  # 商品庫存
            "image": f"{image_folder}/{image_file}",  # 商品圖片路徑
        }
        # 初始化特定商品資訊（覆蓋原本字典）
        ss.products = {
            "金小胖": {"price": 10, "stock": 1, "image": "image/金小胖.png"},
            "洗衣機": {"price": 10, "stock": 10, "image": "image/洗衣機.png"},
            "天堂鑰匙": {"price": 10, "stock": 10, "image": "image/天堂鑰匙.png"},
            "海尼根": {"price": 10, "stock": 10, "image": "image/海尼根.png"},
        }

# 設定網頁標題
st.title("購物網站")

# 建立三欄的版面
cols = st.columns(3)
i = 0  # 記錄欄位位置

# 顯示所有商品
for product_name, details in ss.products.items():
    # 將商品依序放入三欄中
    with cols[i % len(cols)]:
        # 顯示商品圖片，寬度自動調整為容器寬度
        st.image(details["image"], use_container_width=True)
        # 顯示商品資訊
        st.write(f"商品名: {product_name}")
        st.write(f"價格: {details['price']}")
        st.write(f"庫存: {details['stock']}")

        # 購買按鈕
        if st.button(f"購買{product_name}", key=f"{product_name}"):
            if details["stock"] > 0:
                # 庫存大於0，扣除1
                ss.products[product_name]["stock"] -= 1
            else:
                # 特殊提示，如果是獨一無二商品
                if product_name == "金小胖":
                    st.warning("金小胖是獨一無二的")
                # 庫存不足提示
                st.warning(f"{product_name} 正在補貨中...")
            time.sleep(2)  # 模擬購買延遲
            st.rerun()  # 重新執行程式，更新庫存
    i += 1  # 移到下一個欄位

# 網頁第二個標題：新增商品庫存
st.title("新增商品庫存")

# 建立三欄輸入
col_1, col_2, col_3 = st.columns(3)

with col_1:
    # 選擇要補貨的商品
    selected_product = st.selectbox("選擇商品", ss.products.keys())

with col_2:
    # 輸入補貨數量
    new_stock = st.number_input(
        "新增庫存",
        min_value=1,
        step=1,
    )

with col_3:
    # 補貨按鈕
    if st.button("補貨"):
        # 將選擇商品的庫存增加輸入的數量
        ss.products[selected_product]["stock"] += new_stock
        st.rerun()  # 重新執行程式，更新畫面
