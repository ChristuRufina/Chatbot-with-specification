import openai  #pip install openai
import gradio   #pip install gradio

openai.api_key = ""

messages = [{"role": "system", "content": "You are a dietician expert that specializes body health and keeping boy fit as well as you are a gym trainer who helps to keep body toned"}]   #here is wher you will be customizing ur chatbot

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Digital dietician/gym trainer")

demo.launch(share=True)