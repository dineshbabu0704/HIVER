from joblib import load
from intent_classifier import predict
from retrieval import Retriever
from escalation import decide
from reply_generator import generate
class SupportAgent:
 def __init__(self,model_path='outputs/intent_model.joblib',pairs_path='data/historical_pairs.csv'):
  self.model=load(model_path); self.r=Retriever(pairs_path)
 def run(self,text):
  intent,conf=predict(self.model,text); esc=decide(text,conf); hits=self.r.retrieve(text,intent,3); reply=generate(text,intent,hits,esc)
  ev=[{'customer_example':x.text,'historical_reply':x.historical_reply,'similarity':float(x.score)} for _,x in hits.iterrows()]
  return {'intent':intent,'confidence':conf,'decision':esc['decision'],'reason':esc['reason'],'reply':reply,'evidence':ev}
