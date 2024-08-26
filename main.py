
import tkinter as tk
from groq import Groq
client = Groq(api_key="ENTER YOUR API KEY HERE")
def ask_model_question():
    initial_prompt = "Please ask me any question."
    question_completion = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[{"role": "user", "content": initial_prompt}],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
    model_question = ""
    for chunk in question_completion:
        model_question += chunk.choices[0].delta.content or ""
    return model_question.strip()
def get_answer(user_question):
    answer_completion = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[
            {"role": "user", "content": user_question}
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
    model_answer = ""
    for chunk in answer_completion:
        model_answer += chunk.choices[0].delta.content or ""
    return model_answer.strip()
def on_ask_button_click():
    model_question = ask_model_question()
    model_question_label.config(text=model_question)
def on_submit_button_click():
    user_question = user_input.get()
    answer = get_answer(user_question)
    response_label.config(text=answer)
window = tk.Tk()
window.title("AI Chatbot")
bg_color = "#FFFFFF"  
text_color = "#0A1172" 
button_color = "#ADD8E6"  
input_color = "#F5F5F5" 
highlight_color = "#000080"  
window.configure(bg=bg_color)
ask_button = tk.Button(window, text="Ask me a question", command=on_ask_button_click, bg=button_color, fg=text_color)
ask_button.pack(pady=10)
model_question_label = tk.Label(window, text="", bg=bg_color, fg=highlight_color)
model_question_label.pack(pady=10)
user_input_label = tk.Label(window, text="Your Question:", bg=bg_color, fg=text_color)
user_input_label.pack()
user_input = tk.Entry(window, width=50, bg=input_color, fg=text_color)
user_input.pack(pady=5)
submit_button = tk.Button(window, text="Submit", command=on_submit_button_click, bg=button_color, fg=text_color)
submit_button.pack(pady=10)
response_label = tk.Label(window, text="", wraplength=400, bg=bg_color, fg=text_color)
response_label.pack(pady=20)
window.mainloop()
