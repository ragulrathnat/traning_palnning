import pandas 
import numpy
from nltk.translate.bleu_score import sentence_bleu
from jiwer import wer, cer 

filename = "data.csv"

df = pandas.read_csv(filename)

df["df_prec_ran"] = (df["y_pred_random_forest"]>=0.5).astype(int)
df["df_prec_loc"] = (df["y_pred_logistic"] >= 0.5).astype(int)

def computed_value(acc,y_prec):

    tp = sum((acc == 1) & (y_prec == 1))
    tn = sum((acc == 0) & (y_prec == 0))
    fp = sum((acc == 0 ) & (y_prec == 1))
    fn = sum((acc == 1 ) & (y_prec == 0))

    return tp,tn,fp,fn

tp,tn,fp,fn = computed_value(df.y_act,df.df_prec_ran)
print("true positive is ",tp)
print("true negative is ",tn)
print("false positive is ",fp)
print("false negative is ",fn)



def compute_accuracy(tp,tn,fp,fn):
    acc = ((tp+tn)*100 )/ float((tp+tn+fp+fn))
    return acc

print(" accuray",compute_accuracy(tp,tn,fp,fn))

def compute_recall(tp,fn):
    recall = (tp*100)//float(tp+fn)
    return recall

recall = compute_recall(tp,fn)

print("recall is",recall)

def compute_precision(tp,fp):
    precision = (tp*100)//float(tp+fp)
    return precision

precision = compute_precision(tp,fp)
print("precision is", precision)


def f1_score(pre,rec):
    pre = pre/100
    rec = rec/100 
    f1 = (2*pre*rec)/(pre+rec)
    return f1

f1score = f1_score(precision,recall)

print("f1_score is",f1score)

reference = [['this','is','a','test'],[ 'this','is','test']]
precision = ['this','is','a','test']

bleuscore = sentence_bleu(reference, precision)
print("blue score",bleuscore)

spoken = ["hello world"]
prediction = ["hello duck"]

error = wer(spoken,prediction)
print("word error rate",error)

cerror = cer(spoken,prediction)
print("character error rate ",cerror)
