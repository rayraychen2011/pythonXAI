import openai
from dotenv import load_dotenv
import os

load_dotenv()
# 設定API金鑰
openai.api_key = os.getenv("OPENAI_API_KEY")
history = [{"role": "system", "content": "請用繁體中文進行後續對話"}]
while True:
    user_input = input("你：")
    if user_input == "exit":
        break
    history.append({"role": "user", "content": user_input})
    response = openai.chat.completions.create(model="gpt-5-mini", messages=history)

    assistant_message = response.choices[0].message.content
    history.append({"role": "assistant", "content": assistant_message})
    print(f"AI：{assistant_message}")
