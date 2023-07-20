from sklearn.datasets import fetch_20newsgroups
import pandas 
import numpy
from nltk.tokenize import sent_tokenize,word_tokenize
import nltk
nltk.download('punkt')
nltk.download("stopwords")
from nltk.corpus import stopwords
import re 
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
nltk.download('wordnet')




text_data = fetch_20newsgroups()
raw_data = text_data.data

#stage 1 ->lower text 
clean_text = []
def lower_text():
    for i in raw_data:
        clean_text.append(str.lower(i))
    #print(clean_text[:4])

lower_text()

#stage 2 ->tokenizer
clean_text_1 = []
def token():
    for sent in clean_text:
        sentence = word_tokenize(sent)
        clean_text_1.append(sentence)

token()

#regular experssion as re 
clean_text_3 = []
for word in clean_text_1:
    array_data = []
    for i in word:
        reg = re.sub(r'[^\w\s]',"",i)
        array_data.append(reg)
    clean_text_3.append(array_data)



# stage stop and removel 
 
clean_text_4 = []
for words in clean_text_3:
    clean = []
    for wor in words:
        if not wor in stopwords.words("english"):
            clean.append(wor)
        clean_text_4.append(clean)


#stage 5 stemming 
port = PorterStemmer()
clean_text_5 = []
for words in clean_text_4:
    clean1 = []
    for word in words:
       wor = port.stem(word)
       clean1.append(wor)
    clean_text_5.append(clean1)

print(clean_text_5[:4])


#lemmation 
wnet = WordNetLemmatizer()

len = []
for words in clean_text_5:
    cla = []
    for wor in words:
        cla.append(wnet.lemmatize(wor))
    len.append(cla)