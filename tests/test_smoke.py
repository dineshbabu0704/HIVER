import sys
sys.path.insert(0,'src')
from joblib import load
from intent_classifier import predict
from escalation import decide
def test_model():
 m=load('outputs/intent_model.joblib'); i,c=predict(m,'my iphone battery drains quickly'); assert i in m.classes_; assert 0<=c<=1
def test_escalate(): assert decide('my account was hacked',.9)['decision']=='escalate_to_human'
