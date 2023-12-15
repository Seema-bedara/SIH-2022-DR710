def gimme_result(data):
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


    dict_job = {32: 'HR',
                22: 'DESIGNER',
                44: 'SDE',
                45: 'TEACHER',
                2: 'ADVOCATE',
                15: 'BUSINESS-DEVELOPMENT',
                31: 'HEALTHCARE',
                30: 'FITNESS',
                3: 'AGRICULTURE',
                12: 'BPO',
                14: 'BUSINESS ANALYST AND SALES AND SALES',
                19: 'CONSULTANT',
                23: 'DIGITAL-MEDIA',
                6: 'AUTOMOBILE',
                16: 'CHEF',
                29: 'FINANCE',
                4: 'APPAREL',
                36: 'MECHANICAL ENGINEERING',
                0: ' SDE',
                17: 'CIVIL ENGINEERING',
                26: 'ELECTRICAL ENGINEERING',
                10: 'BIO MEDICAL ENGINEERING',
                28: 'ENVIRONMENTAL ENGINEERING',
                41: 'PRODUCT MANAGER',
                40: 'PRODUCCT MANAGER',
                27: 'ENGINEERING',
                1: 'ACCOUNTANT',
                18: 'CONSTRUCTION',
                42: 'PUBLIC-RELATIONS',
                9: 'BANKING',
                5: 'ARTS',
                7: 'AVIATION',
                21: 'DATA SCIENCE',
                8: 'Arts',
                46: 'WEB DEVELOPER',
                35: 'MECHANICAL ENGINEER',
                33: 'Health and fitness',
                20: 'Civil Engineer',
                34: 'Java Developer',
                13: 'BUSINESS ANALYST AND SALES',
                38: 'Operations Manager',
                43: 'Python Developer',
                25: 'DevOps Engineer',
                37: 'NETWORK SECURITY ENGINEER',
                39: 'PMO',
                24: 'Database',
                11: 'BLOCKCHAIN'}





    inp_data = data
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


    # wordfrequencydist = nltk.FreqDist(total_Words)
    # mostCommon = wordfrequencydist.most_common(50)
    required_Text = dataf['structured_resume'].values
    word_vectorizer = joblib.load('C:\\Users\\HP\\prosol\\survey\\model1_vec.pkl')
    required_Text = required_Text[~pd.isnull(required_Text)]
    WordFeatures = word_vectorizer.transform(required_Text)

    clf = joblib.load('C:\\Users\\HP\\prosol\\survey\\model.pkl')
    predicted = clf.predict(WordFeatures)
    print(predicted)
    new_val = predicted[0]
    # result = [new_k for new_k in dict_job.items() if new_k[1] == new_val][0][0]
    result = dict_job[new_val]
    # result = le.inverse_transform([27])
    print("------------------------------------------------------------------------")
    print("                    ", result, "(Best option)")
    print("------------------------------------------------------------------------")

    prob = clf.predict_proba(WordFeatures)
    print(prob)
    return result,prob
