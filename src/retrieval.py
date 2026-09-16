import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
class Retriever:
 def __init__(self,path='data/historical_pairs.csv'):
  self.df=pd.read_csv(path).fillna(''); self.v=TfidfVectorizer(ngram_range=(1,2),min_df=2,max_features=80000,sublinear_tf=True); self.X=self.v.fit_transform(self.df.text)
 def retrieve(self,text,intent,k=3):
  idx=self.df.index[self.df.intent.eq(intent)].tolist() or self.df.index.tolist(); s=cosine_similarity(self.v.transform([text]),self.X[idx])[0]; o=s.argsort()[::-1][:k]; return self.df.iloc[[idx[i] for i in o]][['text','intent','historical_reply']].assign(score=s[o])
