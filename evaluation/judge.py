import os,json,argparse
from openai import OpenAI

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--input',default='judge_samples.jsonl'); ap.add_argument('--output',default='judge_results.jsonl'); a=ap.parse_args(); c=OpenAI()
 with open(a.input,encoding='utf8') as f,open(a.output,'w',encoding='utf8') as o:
  for line in f:
   x=json.loads(line); prompt=('Evaluate this support reply on groundedness, helpfulness, tone, safety, each 1-5. Return JSON. Do not reward unsupported claims.\nCustomer: '+x['customer']+'\nReply: '+x['reply']+'\nEvidence: '+x['evidence']); r=c.chat.completions.create(model=os.getenv('OPENAI_JUDGE_MODEL','gpt-4o-mini'),messages=[{'role':'user','content':prompt}],temperature=0,response_format={'type':'json_object'}); x['judge']=json.loads(r.choices[0].message.content); o.write(json.dumps(x)+'\n')
if __name__=='__main__': main()
