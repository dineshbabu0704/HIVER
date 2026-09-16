import re
HIGH_RISK=['fraud','scam','stolen','hacked','unauthorized','chargeback','legal','lawsuit','police','court','suicide','self harm','threat','discrimination']
PERSONAL=[r'\bssn\b',r'\bsocial security\b',r'\bcredit card number\b',r'\bcard number\b']
ABUSE=['fuck','fucking','idiot','useless','hate you']
def decide(text,confidence):
 s=text.lower(); reasons=[]
 if any(k in s for k in HIGH_RISK): reasons.append('high-risk or sensitive issue')
 if any(re.search(p,s) for p in PERSONAL): reasons.append('sensitive personal/payment information')
 if any(k in s for k in ABUSE): reasons.append('severe customer frustration/abuse')
 if confidence<0.55: reasons.append('low intent confidence')
 return {'decision':'escalate_to_human' if reasons else 'auto_handle','reason':'; '.join(reasons) if reasons else 'routine support issue with sufficient intent confidence'}
