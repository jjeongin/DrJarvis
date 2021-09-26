# Dr. Jarvis 💉
<p align="center"><img src="logo.gif" hweight=200 width=400></img></p>

In this project, we trained/finetuned a text classification model to predict the medical specialties based on the transcription text entered by users. The application is deployed on Streamlit. 

You can find the [Video Demonstration](https://youtu.be/FVcbAJYLKvc) and the [Presentation](https://github.com/jjeongin/StarHack-medical-classification/blob/main/Presentation%20%23Team67.pdf) here

### Installations 
Clone this repo to the ```app``` directory and run 
```
streamlit run app/app.py
```

### The steps we took to build the app:
* Downloaded the **Medical Transcriptions** Dataset from Kaggle
* Split the data into random train and test subsets
* Preprocessed the transcription column of text with **tokenization**
* Trained by SVM, KNN, Random Forest models from **scikit-learn**
* Created the application using **Streamlit** framework and deployed it 


### Output Examples (Prediction + Word Cloud)

### Important Links

- Link to Trained Models ([RandomForest](https://www.kaggle.com/kushaldev75/text-classifier-random-forest), [Support Vector Machine](https://www.kaggle.com/kushaldev75/text-classifier-svm), [K Nearest Neighbour](https://www.kaggle.com/kushaldev75/text-classifier-knn))
