import json
from pathlib import Path
from agent import run_agent, evaluate_case

def main():
    cases=json.loads(Path('evals/dataset.json').read_text())
    results=[]
    for case in cases:
        trace=run_agent(case['input'])
        results.append(evaluate_case(case,trace))
    passed=sum(r['pass'] for r in results)
    report={'total':len(results),'passed':passed,'pass_rate':passed/len(results),'results':results}
    Path('evals/report.json').write_text(json.dumps(report,indent=2))
    print(json.dumps(report,indent=2))
    if passed != len(results): raise SystemExit(1)
if __name__=='__main__': main()
