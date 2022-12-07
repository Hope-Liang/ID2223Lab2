from transformers import pipeline
import gradio as gr

pipe1 = pipeline(model="khalidey/ID2223_Lab2_Whisper_SV")  # change to "your-username/the-name-you-picked"
pipe2 = pipeline('text-generation', model='birgermoell/swedish-gpt')

def transcribe(audio):
    text = pipe1(audio)["text"]
    generated_text = pipe2(text, max_length=50, num_return_sequences=2)[0]['generated_text']
    return text, generated_text

with gr.Blocks() as demo:
    gr.Markdown("#Whisper Small Swedish + Swedish GPT")
    gr.Markdown("Realtime demo for Swedish speech recognition using a fine-tuned Whisper small model & text generation with Swedish GPT.")
    with gr.TabItem("Upload from disk"):
        upload_file = gr.Audio(source="upload", type="filepath",label="Upload from disk")
        upload_button = gr.Button("Submit for recognition")
        upload_outputs = [
            gr.Textbox(label="Recognized speech from uploaded file"),
            gr.Textbox(label="Swedish-gpt generated speech from uploaded file")
        ]
    with gr.TabItem("Record from microphone"):
        record_file = gr.Audio(source="microphone", type="filepath",label="Record from microphone")
        record_button = gr.Button("Submit for recognition")
        record_outputs = [
            gr.Textbox(label="Recognized speech from recordings"),
            gr.Textbox(label="Swedish-gpt generated speech from recordings")
        ]
    upload_button.click(
        fn=transcribe,
        inputs=upload_file,
        outputs=upload_outputs,
    )
    record_button.click(
        fn=transcribe,
        inputs=record_file,
        outputs=record_outputs,
    )
        
demo.launch()