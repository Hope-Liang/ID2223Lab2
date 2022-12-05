# ID2223Lab2
Authors: (GROUP 31) Khalid El Yaacoub, Xinyu Liang

## Introduction

In this project, the goal is to fine-tune a pre-trained transformer model (Whisper) for Swedish language translation, refactor it into a feature pipeline and a training pipeline and build a serverless UI for using the fine-tuned model. The pipeline structure uses Hopsworks/Google Drive/KTH OneDrive as feature store, Google Drive/Hugging face as model store and Hugging face as interactive UI to build applications. The interactive UI takes user's speech record as input and prints the recognized spoken sentence.


## Whisper

The pretrained model we used in the lab is from [Whisper](https://huggingface.co/blog/fine-tune-whisper) and a modified version by Professor Jim Dowling from his [github repo](https://github.com/ID2223KTH/id2223kth.github.io/tree/master/assignments/lab2) to fine-tune on Swedish language.

Whisper is a multilingual pre-trained model for Automatic Speech Recognition (ASR) task that can be applied to over 96 languages. It has a Transformer-based encoder-decoder architecture that does sequence-to-sequence mapping from spectogram features to text tokens. The model veries in sizes such as number of layers and we selected the small-sized model with 244M parameters to fine-tune on in this lab.


## Feature Pipeline

The [feature pipeline](https://github.com/Hope-Liang/ID2223Lab2/blob/main/whisper_feature_pipeline.ipynb) is downloaded from Google Colab and only CPU is used when extracting the features. The data is obtained from [Common Voice](https://huggingface.co/datasets/mozilla-foundation/common_voice_11_0) and `Subset = sv-SE` for Swedish language. Irrelavent columns are removed and a feature extractor and a tokenizer are used for extracting the spectrogram features and preprocessing the labels respectively. The feature extractor will first pad/truncate audio samples to 30s long and then convert them to log-Mel spectrograms.

The preprocessing of the feature pipeline takes around half an hour each time, making feature storage essential in our case. However, the generated features are quite huge (roughly 16.7GB) in total, and thus we tested using both Google Drive and Hopsworks for storing the feature data as shown in the code. 

To simplify the data-loading procedure in the training pipeline, we then combined the stored data from the two places, made a folder as its original structure and compressed it. We uploaded the zipped folder (roughly 1.6GB) to KTH OneDrive and obtained a [publicly-accessible link](https://kth-my.sharepoint.com/:u:/g/personal/xinyulia_ug_kth_se/EWiFiRGIjLVOoOvs6aKbetYBms635pOLGO_-hY74mgulxg?e=hxkUgg).


## Training Pipeline

In the [training pipeline](https://github.com/Hope-Liang/ID2223Lab2/blob/main/whisper_training_pipeline.ipynb), we utilized free GPU on Colab and downloaded the data from KTH OneDrive with wget command. The data is downloaded and unzipped to Colab local environment, and then read by DatasetDict.load_from_disk function.

The data is then processed to replace padded labels with -100 to ignore the loss correctly. Evaluation metric is configured as word error rate (WER) and the pretrained "whisper-small" model is loaded. Our model saves checkpoints to Google Drive (in this case we also have to set `push_to_hub=False`). We trained for 4000 steps and saves the checkpoints every 1000 steps. After the training completes, which took roughly 8 hours in total, we reached a WER of 19.89%.


## Interactive UI





## Link to App

The link to the Application webpage on Hugging Face is [Interactive UI](https://huggingface.co/spaces/khalidey/ID2223-Lab2-Whisper).


## How to Improve Model Performance

### Model-centric Approaches


### Data-centric Approaches

