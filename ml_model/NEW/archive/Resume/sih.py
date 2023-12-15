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


resumeData = pd.read_csv('UpdatedResumeDataSet.csv', encoding='utf-8')

dict_job = {'HR': 30, 'DESIGNER': 19, 'INFORMATION-TECHNOLOGY': 33, 'TEACHER': 44, 'ADVOCATE': 1, 'nan': 47, 'BUSINESS-DEVELOPMENT': 12, 'HEALTHCARE': 29, 'FITNESS': 28, 'AGRICULTURE': 2, 'BPO': 11, 'SALES': 41, 'CONSULTANT': 17, 'DIGITAL-MEDIA': 20, 'AUTOMOBILE': 5, 'CHEF': 15, 'FINANCE': 27, 'APPAREL': 3, 'ACCOUNTANT': 0, 'CONSTRUCTION': 16, 'PUBLIC-RELATIONS': 39, 'BANKING': 10, 'ARTS': 4, 'AVIATION': 6, 'Data Science': 21, 'Advocate': 7, 'Arts': 8,
            'Web Designing': 46, 'Mechanical Engineer': 35, 'Sales': 43, 'Health and fitness': 32, 'Civil Engineer': 18, 'Software Engineer 1': 34, 'Business Analyst': 14, 'SAP Developer': 42, 'Automation Testing': 9, 'Electrical Engineering': 26, 'Operations Manager': 37, 'Software Engineer': 40, 'Software Engineer': 23, 'Network Security Engineer': 36, 'PMO': 38, 'Database': 22, 'Hadoop': 31, 'ETL Developer': 25, 'DotNet Developer': 24, 'Blockchain': 13, 'Testing': 45}


var_mod = ['Category']
le = LabelEncoder()
for i in var_mod:
    resumeData[i] = le.fit_transform(resumeData[i])


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


wordfrequencydist = nltk.FreqDist(total_Words)
mostCommon = wordfrequencydist.most_common(50)
required_Text = dataf['structured_resume'].values
word_vectorizer = joblib.load('model1_vec.pkl')
required_Text = required_Text[~pd.isnull(required_Text)]
WordFeatures = word_vectorizer.transform(required_Text)

clf = joblib.load('model.pkl')
predicted = clf.predict(WordFeatures)
print(predicted)
new_val = predicted[0]
result= [new_k for new_k in dict_job.items() if new_k[1] == new_val][0][0]
print("------------------------------------------------------------------------")
print("                    ",result,"(Best option)")
print("------------------------------------------------------------------------")

prob = clf.predict_proba(WordFeatures)
print(prob)