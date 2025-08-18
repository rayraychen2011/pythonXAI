import streamlit as st

# 小朋友的程式手冊
# 我們只會用今天上課學到的指令與概念，像是：
# - 印出內容：print (在 streamlit 我們用 st.write/st.text)
# - 變數（a = 10）與基本型態：int, float, str, bool
# - 簡單運算：+, -, *, /, //, %, **
# - 字串格式 f"{ }"
# - 型態查看與轉換：type(), int(), float(), str(), bool()
# - 文字長度：len()
# - streamlit 的簡單元件：st.title, st.write, st.text, st.markdown


st.title("程式小技巧手冊")

st.write("下面是今天學到的簡單用法，用很簡單的話說明，方便在網頁上閱讀。")

st.markdown("## 1 — 變數（把東西放進小盒子裡）")
st.write("說明：變數就像一個小盒子，我們可以把數字或文字放進去，日後再拿出來用。")
st.markdown("**程式範例（示範用）**")
st.write("num = 10\nword = 'apple'\nflag = True")
st.write("執行結果：")

# 範例：變數
num = 10
word = "apple"
flag = True
st.write(f"數字放在 num 裡面：{num}")
st.write(f"文字放在 word 裡面：{word}")
st.write(f"布林值放在 flag 裡面：{flag}")

# 使用 st.markdown（課堂有教）來顯示標題
st.markdown("## 2. 常見的數學運算")
st.write("加、減、乘、除還有次方等：")

# 範例：運算
st.write(f"1 + 1 = {1 + 1}")
st.write(f"2 * 3 = {2 * 3}")
st.write(f"2 ** 3 = {2 ** 3}")


st.markdown("## 3 — 字串可以相加或重複顯示")
st.write("說明：兩個字串可以用 + 連接；字串乘法會重複內容。")
st.markdown("**程式範例**")
st.write('"apple" + "pen"')
st.write('"apple" * 3')
st.write("執行結果（示範）：" + ("apple" + "pen"))
st.write("重複 3 次 的結果（示範）：" + ("apple" * 3))

st.markdown("## 4 — 看東西的長度和型態")
st.write("說明：用 len() 看長度；用 type() 看東西是什麼型態。")
st.markdown("**程式範例**")
st.write("len('apple') → 結果：" + str(len("apple")))
st.write("type(1) → 結果：" + str(type(1)))
st.write("type('a') → 結果：" + str(type("a")))


st.markdown("## 5 — 把東西換型態（像換衣服一樣）")
st.write("說明：有時候我們要把東西換一種型態，例如把字串變成數字，或把數字變成字串。")
st.markdown("**程式範例**")
st.write("int(1.234) → " + str(int(1.234)))
st.write("float('1.234') → " + str(float("1.234")))
st.write("str(123) → " + str(str(123)))

# 因為課堂有教 input()（是在終端機中），但網頁的互動元件在本堂範例中沒有出現，
# 所以這裡我們用變數來模擬使用者輸入，並用 st.write 顯示結果（st.write 在課堂有出現）
st.markdown("## 6 — 簡單示範（終端機的輸入範例）")
st.write(
    "說明：課堂中學過用 input() 在終端機輸入；在網頁上我們先用變數模擬，下面會顯示範例程式和模擬結果。"
)
st.markdown("**範例程式（終端機）**")
st.write("name = input('請輸入你的名字: ')")
name = "小明"  # 模擬輸入
st.write("模擬結果：你好，" + name + "！")

st.markdown("## 7 — 小範例：計算圓的面積（模擬輸入）")
st.write("說明：原本課堂會用 input() 讀半徑，這裡用字串模擬然後換成數字計算面積。")
st.markdown("**範例程式（終端機）**")
st.write("r = input('請輸入圓的半徑: ')")
radius = "5"  # 用字串模擬使用者輸入
r = float(radius)
area = 3.14 * r * r
st.write("模擬結果：當半徑是 " + str(r) + "，圓面積是 " + str(area))

st.markdown("---")
st.write("以上就是今天學到的簡單程式技巧，祝學習愉快！")
