import sys,json
sys.path.insert(0,'src')
from pipeline import SupportAgent
print(json.dumps(SupportAgent().run(' '.join(sys.argv[1:])),indent=2,ensure_ascii=False))
