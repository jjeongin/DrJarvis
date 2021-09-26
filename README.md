# StarHack Medical Classification Project 💉
In this project, we trained/finetuned a text classification model to predict the medical specialties based on the transcription text entered by users. The application is deployed on Streamlit. 

You can find the [Video Demonstration]() and the [Presentation]() here

### Installations 
**Note: You only need to install if you want to run it locally on your machine**

Clone this repo to the ```app``` directory and run 
```
streamlit run app/main.py
```

### The steps we took to build the app:
* Downloaded the **Medical Transcriptions** Dataset from Kaggle
* Split the data into random train and test subsets
* Preprocessed the transcription column of text with **tokenization**
* Finetuned pre-trained **distilBert** model from **HuggingFace PyTorch**
* Created the application using **Streamlit** framework and deployed it 


### Output Examples (Prediction + VizBert + Word Cloud)
