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
warnings.filterwarnings('ignore')
nltk.download('stopwords')
nltk.download('punkt')


resumeData = pd.read_csv('UpdatedResumeDataSet.csv', encoding='utf-8')
# resumeData.head()


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

# clean_input = inp_data(lambda x: clean_input(x))
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
print(mostCommon)
required_Text = dataf['structured_resume'].values
# required_Target = resumeData['Category'].values
word_vectorizer = joblib.load('model1_vec.pkl')
# word_vectorizer = TfidfVectorizer(sublinear_tf=True, stop_words='english', max_features=1500)
required_Text = required_Text[~pd.isnull(required_Text)]
WordFeatures = word_vectorizer.transform(required_Text)
print(WordFeatures.shape)   

clf = joblib.load('model.pkl')
predicted = clf.predict(WordFeatures)
print(predicted)
