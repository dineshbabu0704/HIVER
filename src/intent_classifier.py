from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from joblib import dump

def build_model(df):
    m=Pipeline([('tfidf',TfidfVectorizer(ngram_range=(1,2),min_df=2,max_features=60000,sublinear_tf=True)),('clf',LogisticRegression(max_iter=1000,class_weight='balanced'))])
    return m.fit(df.text.fillna(''),df.intent)
def train(path='data/historical_pairs.csv',out='outputs/intent_model.joblib'):
    import pandas as pd
    dump(build_model(pd.read_csv(path)),out)
def predict(model,text):
    p=model.predict_proba([text])[0]; i=p.argmax(); return model.classes_[i],float(p[i])
