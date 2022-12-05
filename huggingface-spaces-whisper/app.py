from transformers import pipeline
import gradio as gr

pipe = pipeline(model="khalidey/ID2223_Lab2_Whisper_SV")  # change to "your-username/the-name-you-picked"

def transcribe(audio):
    text = pipe(audio)["text"]
    return text

iface = gr.Interface(
    fn=transcribe, 
    inputs=gr.Audio(source="microphone", type="filepath"), 
    outputs="text",
    title="Whisper Small Swedish",
    description="Realtime demo for Swedish speech recognition using a fine-tuned Whisper small model.",
)

iface.launch()
