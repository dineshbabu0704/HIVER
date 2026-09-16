import pandas as pd,sys
from sklearn.metrics import accuracy_score,f1_score,classification_report
sys.path.insert(0,'../src'); from joblib import load; from intent_classifier import predict
if __name__=='__main__':
 d=pd.read_csv('golden_set.csv'); m=load('../outputs/intent_model.joblib'); p=[predict(m,x)[0] for x in d.text.fillna('')]; tr=pd.read_csv('../data/historical_pairs.csv'); maj=tr.intent.mode()[0]
 print('System accuracy:',round(accuracy_score(d.gold_intent,p),4)); print('System macro-F1:',round(f1_score(d.gold_intent,p,average='macro'),4)); print('Majority baseline accuracy:',round(accuracy_score(d.gold_intent,[maj]*len(d)),4)); print(classification_report(d.gold_intent,p,zero_division=0)); print('CAVEAT: gold labels are pre-labeled with the same rubric used for training; human verification and leakage-safe evaluation are required before reporting these as final results.')
