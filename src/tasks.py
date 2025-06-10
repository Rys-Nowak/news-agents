from crewai import Task

def build_tasks(agents, article1, article2):
    # TODO diffrent task for 1 and for multiple docs
    return [
        Task(
            description=f"\n\nARTYKUŁ 1:\n{article1}\n\nARTYKUŁ 2:\n{article2}\n\n",
            agent=agents["comparator"],
            expected_output="..."
        ),
        Task(
            description="...",
            agent=agents["tone_analyst"],
            expected_output="..."
        ),
        Task(
            description="...",
            agent=agents["bias_analyst"],
            expected_output="..."
        ),
        Task(
            description="...",
            agent=agents["conclusion_agent"],
            expected_output="..."
        )
    ]