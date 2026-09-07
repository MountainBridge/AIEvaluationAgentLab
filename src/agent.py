from dataclasses import dataclass, asdict
from typing import Any

@dataclass
class Trace:
    input: str
    tool_calls: list[dict[str, Any]]
    output: dict[str, Any]
    steps: int

def lookup_policy(topic: str) -> str:
    return {"refund": "Refunds require an order id and are limited to eligible orders.", "shipping": "Standard shipping takes 3-5 business days."}.get(topic, "No policy found.")

def run_agent(question: str, max_steps: int = 3) -> Trace:
    calls=[]
    topic = "refund" if "refund" in question.lower() else "shipping" if "shipping" in question.lower() else "unknown"
    if max_steps < 1: raise ValueError("max_steps must be positive")
    calls.append({"tool":"lookup_policy","input":{"topic":topic}})
    answer=lookup_policy(topic)
    return Trace(question,calls,{"answer":answer,"topic":topic},1)

def evaluate_case(case: dict[str, Any], trace: Trace) -> dict[str, Any]:
    expected=case["expected"]
    answer_ok=expected["topic"] == trace.output["topic"]
    tool_ok=trace.tool_calls and trace.tool_calls[0]["tool"] == "lookup_policy"
    return {"id":case["id"],"answer_correct":answer_ok,"tool_path_correct":tool_ok,"pass":answer_ok and tool_ok}
