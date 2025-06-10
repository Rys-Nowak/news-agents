from crewai import Crew

def run_crew_pipeline(agents, tasks):

    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        verbose=True # dla debug
    )

    results = crew.run()
    for idx, result in enumerate(results, 1):
        print(f"Task {idx}: {result}\n")

    return results
