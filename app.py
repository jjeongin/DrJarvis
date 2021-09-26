import numpy as np, pickle, streamlit as st
from pprint import pprint
from transformers import DistilBertModel, DistilBertTokenizer
from wordcloud import WordCloud

# aesthetics
st.set_page_config(
    page_title='Team Legion',
    page_icon='💉',
    layout='centered',
    initial_sidebar_state='expanded'
)

# global variables
model_path = '/mnt/d/share/StarHack-medical-classification/model/'
logo = st.image(image='logo.gif')
title = st.title(body='Dr. Jarvis')
st.markdown(body='## Medical Specialty Classifier')

model_version = 'distilbert-base-uncased'
do_lower_case = True
model = DistilBertModel.from_pretrained(model_version, output_attentions=True)
tokenizer = DistilBertTokenizer.from_pretrained(model_version, do_lower_case=do_lower_case)

abstract1 = st.text_area(
	label='Text to Classify',
	help='Paste text with medical jargon.'
)

classifier = st.selectbox(
	label='Classifier',
	options=np.asarray(a=list([
		'Support Vector Machine',
		'K-Nearest Neighbors',
		'Random Forest'
	]))
)

if st.button(label='Classify'):
	if classifier == 'Support Vector Machine':
		svm = pickle.load(file=open(file='svc.pkl', mode='rb'))
		pprint(type(svm))
		st.write(svm.predict(list([abstract1])))
	elif classifier == 'K-Nearest Neighbors':
		knn = pickle.load(file=open(file='knn.pkl', mode='rb'))
		pprint(type(knn))
		st.write(knn.predict(list([abstract1])))
	elif classifier == 'Random Forest':
		rfc = pickle.load(file=open(file='rfc.pkl', mode='rb'))
		pprint(type(rfc))
		st.write(rfc.predict(list([abstract1])))

	# word cloud 
	st.markdown(body='### Word Cloud')
	wc = WordCloud().generate(text=abstract1)
	wc.to_file(filename='wordcloud.png')
	wc_image = st.image(
		image='wordcloud.png',
		caption='Word cloud of medical abstract.',
		use_column_width=True
	)
