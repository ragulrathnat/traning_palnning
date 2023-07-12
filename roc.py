import pandas
import numpy
import matplotlib.pyplot as plot
from numpy import trapz
from sklearn import metrics

filename = "da.csv"

file = pandas.read_csv(filename)

file["prec"] =(file["y_pred_random_forest"] >= 0.5).astype(int)
file.to_csv("da1.csv")

theshold = list(numpy.array(list(range(0,105,5)))/100)
roc_list = []
for thes in theshold:
   file["prec"] =(file["y_pred_random_forest"] >= thes).astype(int)

   tp = sum((file["y_act"] == 1) & (file["prec"] == 1))
   tn = sum((file["y_act"] == 0) & (file["prec"] == 0))
   fp = sum((file["y_act"] == 0 ) & (file["prec"] == 1))
   fn = sum((file["y_act"] == 1) & (file["prec"] == 0))

   tpr = tp / (tp +fn)

   fpr = fp / (tn+fp)
   roc_list.append([tpr,fpr])

df = pandas.DataFrame(roc_list,columns=["x","y"])

auc = trapz(df.x,df.y)
print("AUC score",auc)

plot.scatter(df.y,df.x)
plot.plot([0,1])

plot.xlabel("True prediction ")
plot.ylabel("Flase prediction")

print("ROC graph successfully drawn")
plot.show()


# mean absolute Error 

file1 = pandas.read_csv("da1.csv")
value =0
le = len(file1)

for ind,val in file1.iterrows():

   dat = val["y_act"] - val["y_pred_random_forest"]
   value +=dat

value = value/le

print("mean Absolute error(MAE)is",value)

# means Square error
tot = 0 
for index,val in file1.iterrows():
   dat = val["y_act"]-val["y_pred_random_forest"]
   dat = dat*dat
   tot += dat

tot = tot/le
print("mean square error(MSE) is ",tot)


#prc rate 

prc_rate = metrics.average_precision_score(file1["y_act"],file1["y_pred_random_forest"])
print("prc rate is ",prc_rate)
