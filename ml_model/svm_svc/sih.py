import joblib
from scipy.sparse import hstack
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import re
from sklearn.preprocessing import LabelEncoder
from wordcloud import WordCloud
import string
from nltk.corpus import stopwords
import nltk
from sklearn.multiclass import OneVsRestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from pandas.plotting import scatter_matrix
from sklearn.metrics import accuracy_score
from sklearn import metrics
import pandas as pd
import numpy as np
import pandas as pd
import os
import seaborn as sns
import warnings

dict_job = {
    "Data Science":  6,
    "HR": 12,
    "Advocate":  0,
    "Arts":  1,
    "Web Designing": 24,
    "Mechanical Engineer": 16,
    "Sales": 22,
    "Health and fitness": 14,
    "Civil Engineer":  5,
    "Software Engineer": 15,
    "Business Analyst":  4,
    "SAP Developer": 21,
    "Automation Testing":  2,
    "Electrical Engineering": 11,
    "Operations Manager": 18,
    "Python Developer": 20,
    "DevOps Engineer":  8,
    "Network Security Engineer": 17,
    "PMO": 19,
    "Database":  7,
    "Hadoop": 13,
    "ETL Developer": 10,
    "DotNet Developer":  9,
    "Blockchain":  3,
    "Testing": 23

}


inp_data = input("Enter resume: ")
data = {"Resume": [inp_data]}
dataf = pd.DataFrame(data)
dataf['structured_resume'] = ''


def clean_resume(Text):
    Text = re.sub('http\S+\s*', ' ', Text)
    Text = re.sub('@\S+', '  ', Text)
    Text = re.sub('[%s]' % re.escape(
        """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', Text)
    Text = re.sub('RT|cc', ' ', Text)
    Text = re.sub('#\S+', '', Text)
    Text = re.sub(r'[^\x00-\x7f]', r' ', Text)
    Text = re.sub('\s+', ' ', Text)
    return Text


dataf['structured_resume'] = dataf.Resume.apply(lambda x: clean_resume(x))

Set_Of_StopWords = set(stopwords.words('english')+['``', "''"])
total_Words = []
Sentences = dataf['Resume'].values
cleaned_Sentences = ""
for i in range(0, len(Sentences)):
    cleanedText = clean_resume(Sentences[i])
    cleaned_Sentences += cleanedText
    requiredWords = nltk.word_tokenize(cleanedText)
    for word in requiredWords:
        if word not in Set_Of_StopWords and word not in string.punctuation:
            total_Words.append(word)


required_Text = dataf['structured_resume'].values
word_vectorizer = joblib.load('model1_vec.pkl')
required_Text = required_Text[~pd.isnull(required_Text)]
WordFeatures = word_vectorizer.transform(required_Text)

clf = joblib.load('model.pkl')
predicted = clf.predict(WordFeatures)

new_val = predicted
result= [new_k for new_k in dict_job.items() if new_k[1] == new_val][0][0]
print("------------------------------------------------------------------------")
print("                    ",result,"(Best option)")
print("------------------------------------------------------------------------")


prob = clf.predict_proba(WordFeatures)
print(prob)