import sys
import unittest
sys.path.insert(0,'src')
from agent import run_agent, evaluate_case

class AgentTests(unittest.TestCase):
    def test_agent_is_bounded(self):
        self.assertLessEqual(run_agent('What is shipping?').steps, 3)

    def test_evaluation_catches_tool_path(self):
        trace=run_agent('What is the refund policy?')
        result=evaluate_case({'id':'x','expected':{'topic':'refund'}},trace)
        self.assertTrue(result['answer_correct'] and result['tool_path_correct'])

if __name__ == '__main__': unittest.main()
