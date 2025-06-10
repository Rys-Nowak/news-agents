import os
from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

# TODO split each agent to each file, refactor to a more generic structure


def create_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0.1,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

def build_agents():
    llm = create_llm()

    comparator = Agent(
        role="Ekspert porównujący narracje",
        goal="Wyszukaj różnice między dwoma artykułami dotyczącymi tego samego tematu",
        backstory="...",
        llm=llm
    )

    bias_analyst = Agent(
        role="Analityk biasu i spinowania",
        goal="...",
        backstory="...",
        llm=llm
    )

    tone_analyst = Agent(
        role="Analityk tonu i manipulacji",
        goal="...",
        backstory="...",
        llm=llm
    )

    conclusion_agent = Agent(
        role="Agent decyzyjny",
        goal="...",
        backstory="...",
        llm=llm
    )

    return {
        "comparator": comparator,
        "tone_analyst": tone_analyst,
        'bias_analyst': bias_analyst,
        "conclusion_agent": conclusion_agent
    }
