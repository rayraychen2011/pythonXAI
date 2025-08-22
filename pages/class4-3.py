import streamlit as st
import os
import time

# 簡化操作 session_state
ss = st.session_state

# 設定圖片資料夾
image_folder = "image"

# 初始化商品資料（只跑一次）
if "products" not in ss:
    ss.products = {
        "金小胖": {
            "price": 10000000000,
            "stock": 1,
            "image": f"{image_folder}/金小胖.png",
        },
        "洗衣機": {"price": 70000, "stock": 10, "image": f"{image_folder}/洗衣機.png"},
        "天堂鑰匙": {"price": 1, "stock": 10, "image": f"{image_folder}/天堂鑰匙.png"},
        "海尼根": {"price": 70, "stock": 10, "image": f"{image_folder}/海尼根.png"},
    }

# 設定網頁標題
st.title("購物網站")

# 建立三欄的版面
cols = st.columns(3)
i = 0  # 記錄欄位位置

# 顯示所有商品
for product_name, details in ss.products.items():
    with cols[i % len(cols)]:
        st.image(details["image"], use_container_width=True)
        st.write(f"商品名: {product_name}")
        st.write(f"價格: {details['price']}")
        st.write(f"庫存: {details['stock']}")

        # 購買按鈕
        if st.button(f"購買 {product_name}", key=f"buy_{product_name}"):
            if details["stock"] > 0:
                ss.products[product_name]["stock"] -= 1
            else:
                if product_name == "金小胖":
                    st.warning("金小胖是獨一無二的")
                else:
                    st.warning(f"{product_name} 正在補貨中...")
            time.sleep(2)  # 模擬延遲
            st.rerun()
    i += 1

# 新增商品庫存
st.title("新增商品庫存")

col_1, col_2, col_3 = st.columns(3)

with col_1:
    selected_product = st.selectbox("選擇商品", list(ss.products.keys()))

with col_2:
    new_stock = st.number_input("新增庫存", min_value=1, step=1)

with col_3:
    if st.button("補貨"):
        ss.products[selected_product]["stock"] += new_stock
        st.rerun()
