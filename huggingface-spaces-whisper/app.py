from transformers import pipeline
import gradio as gr

pipe1 = pipeline(model="khalidey/ID2223_Lab2_Whisper_SV")  # change to "your-username/the-name-you-picked"
pipe2 = pipeline('text-generation', model='birgermoell/swedish-gpt')

def transcribe(audio):
    text = pipe1(audio)["text"]
    generated_text = pipe2(text, max_length = 30, num_return_sequences=2)[0]['generated_text']
    return text, generated_text

iface = gr.Interface(
    fn=transcribe, 
    inputs=gr.Audio(source="microphone", type="filepath"), 
    outputs=['text', 'text'],
    title="Whisper Small Swedish + Swedish GPT",
    description="Realtime demo for Swedish speech recognition using a fine-tuned Whisper small model and text generation with Swedish GPT.",
)

iface.launch()