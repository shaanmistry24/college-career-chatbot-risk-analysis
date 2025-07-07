from gradio.components import chatbot
import gradio as gr
import openai

# Set OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Initial message history to begin the conversation
message_history = [{"role": "user", "content": "You are a college and career advisor bot. Before I ask any questions, I will give you information about myself that you can use to provide advice including my demographics and preferences. You will give me a complete, detailed potential college and career path based on my demographics and preferences. Make sure to provide specific recommendations for colleges, majors, jobs, internships, summer programs, etc. At the end, provide ten websites based on the recommendations given that I can visit to learn more. Take test scores and extracurriculars into account and inform me what the likelihood of getting into the recommended schools are based on my statistics. After, I will ask questions about the path you have planned for me and potentially ask you to revise it. If you understand, say OK."},
                   {"role": "assistant", "content": "OK"}]

def predict(input):
    global message_history
    message_history.append({"role": "user", "content": input})
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=message_history
    )
    reply_content = completion.choices[0].message['content']
    message_history.append({"role": "assistant", "content": reply_content})
    response = [(message_history[i]["content"], message_history[i + 1]["content"]) for i in range(2, len(message_history) - 1, 2)]
    return response

# Create chatbot interface using Gradio
with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    with gr.Row():
        txt = gr.Textbox(show_label=False, placeholder="List your name, age, interests, extracurriculars, test scores, current location of residency, and other college or career preferences: ").style(container=False)
        txt.submit(predict, txt, chatbot)
        txt.submit(None, None, txt, _js="() => {''}")
demo.launch()
