import os  # 載入作業系統介面模組，用來操作檔案與目錄
import streamlit as st  # 載入 Streamlit，用於建立簡單的網頁介面

# 列出 markdown 資料夾內的所有檔案
files = os.listdir("markdown")
print(files)  # 在終端機印出未排序的檔案列表，方便除錯

# 對檔案名稱做排序，讓顯示順序固定
files.sort()
print(files)  # 在終端機印出已排序的檔案列表，方便確認排序結果

# 逐一讀取每一個 markdown 檔案並在 Streamlit 的 expander 中顯示內容
for f in files:

    # 使用 UTF-8 編碼開啟檔案，確保中文可以正確讀取
    with open(f"markdown/{f}", "r", encoding="utf-8") as file:
        content = file.read()  # 將整個檔案內容讀入變數 content

    # 使用檔名（移除 .md 副檔名）作為 expander 標題，點開後顯示內容
    with st.expander(f[:-3]):
        st.write(content)  # 在 expander 裡寫出 markdown 內容
