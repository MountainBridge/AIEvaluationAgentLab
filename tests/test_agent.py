import sys
sys.path.insert(0,'src')
from agent import run_agent, evaluate_case

def test_agent_is_bounded():
    assert run_agent('What is shipping?').steps <= 3

def test_evaluation_catches_tool_path():
    trace=run_agent('What is the refund policy?')
    result=evaluate_case({'id':'x','expected':{'topic':'refund'}},trace)
    assert result['answer_correct'] and result['tool_path_correct']
