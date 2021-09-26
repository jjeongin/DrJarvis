# Dr. Jarvis 💉
<p align="center"><img src="logo.gif" hweight=200 width=400></img></p>

In this project, we trained/finetuned a text classification model to predict the medical specialties based on the transcription text entered by users. The application is deployed on Streamlit. 

You can find the [Video Demonstration](https://youtu.be/FVcbAJYLKvc) and the [Presentation](https://github.com/jjeongin/StarHack-medical-classification/blob/main/Presentation%20%23Team67.pdf) here

### Installations 
1. Clone repository and go into the directory. <br>
`git clone https://github.com/Fennec2000GH/StarHack-medical-classification.git`

2. Install required dependencies in Python. <br>
`pip install -r requirements.txt`

3. Download required classifier models as Pickle (`.pkl`) files. The links to each are given below. <br>
- [svm.pkl](http://www.kaggle.com/dataset/a3ae9d843e5998b6dd7c21cc2ab54ed56a37b6bfca6da47073906633e44e3872)
- [knn.pkl](http://www.kaggle.com/dataset/35a6e60b83ab7446241d2d1905f5fe5f97c1172836f316077c7938993f48bc66)
- [rfc.pkl](http://www.kaggle.com/dataset/e882644a6da229eb5177a9fa82bd9885e06e2ea954dbb0aa797333e1c3a2139d)

  Make sure the three (3) Pickle files are directly in the cloned repository root (`StarHack-medical-classification/`).

4. Run the app. <br>
`streamlit run app.py`

### The steps we took to build the app:
* Downloaded the **Medical Transcriptions** Dataset from Kaggle
* Split the data into random train and test subsets
* Preprocessed the transcription column of text with **tokenization**
* Trained by SVM, KNN, Random Forest models from **scikit-learn**
* Created the application using **Streamlit** framework and deployed it 


### Output Examples (Prediction + Word Cloud)

### Important Links

- Link to Trained Models ([RandomForest](https://www.kaggle.com/kushaldev75/text-classifier-random-forest), [Support Vector Machine](https://www.kaggle.com/kushaldev75/text-classifier-svm), [K Nearest Neighbour](https://www.kaggle.com/kushaldev75/text-classifier-knn))
