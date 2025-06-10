from src.agents import build_agents
from src.tasks import build_tasks
from src.run import run_crew_pipeline
from utils.io import FileReader
from dotenv import load_dotenv

load_dotenv()

def main():
    reader = FileReader()
    article1 = reader.load_json("data/article_1.json")
    article2 = reader.load_json("data/article_2.json")

    agents = build_agents()
    #TODO multiple docs, prolly in dict
    tasks = build_tasks(agents, article1, article2)
    run_crew_pipeline(agents, tasks)


if __name__ == "__main__":
    main()
