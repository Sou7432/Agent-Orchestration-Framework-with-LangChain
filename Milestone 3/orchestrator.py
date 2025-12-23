from agents.planner_agent import create_planner_agent
from agents.execution_agent import create_execution_agent
from memory.shared_memory import create_shared_memory

shared_memory = create_shared_memory()

def run_pipeline(user_query):
    planner = create_planner_agent()
    executor = create_execution_agent()

    plan = planner.run({"task": user_query})

    shared_memory.save_context(
        {"input": user_query},
        {"output": plan}
    )

    result = executor.run({"plan": plan})

    return plan, result
