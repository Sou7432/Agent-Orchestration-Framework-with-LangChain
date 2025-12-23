from orchestrator import run_pipeline

if __name__ == "__main__":
    query = input("Enter your task: ")
    plan, execution = run_pipeline(query)

print("\n--- FINAL OUTPUT ---\n")
print("PLAN:\n", plan)
print("\nEXECUTION RESULT:\n", execution)
