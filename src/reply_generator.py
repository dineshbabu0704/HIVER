import re
def generate(text,intent,hits,esc):
 if esc['decision']=='escalate_to_human': return 'Thanks for reaching out. This needs a closer look by our support team. Please continue in DM so a specialist can review the details securely.'
 if hits is None or len(hits)==0: return 'Thanks for reaching out. Please send us a DM with more details about the issue and your device/iOS version so we can help.'
 r=re.sub(r'https?://\S+','',str(hits.iloc[0].historical_reply)); return re.sub(r'\s+',' ',r).strip() or 'Thanks for reaching out. Please send us a DM with more details so we can help.'
