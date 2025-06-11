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
        goal="Porównuj narracje w wielu artykułach o tym samym temacie, aby wykryć subtelne różnice w tonie, treści i selekcji faktów.",
        backstory="""
                Jesteś ekspertem analizy porównawczej treści dziennikarskich. Twoim zadaniem jest wykrywanie różnic narracyjnych 
                w artykułach, które opisują ten sam temat, ale ukazują się w różnych mediach lub w różnych momentach czasowych. 
                Szukasz zmian tonu, pominięć, przesunięć perspektywy oraz wszelkich oznak manipulacji semantycznej lub emocjonalnej.
                Twoja wiedza obejmuje retorykę, NLP oraz analizę semantyczną tekstu.
                """,
        llm=llm
    )

    bias_analyst = Agent(
        role="Analityk biasu i spinowania",
        goal="Identyfikuj i klasyfikuj rodzaje stronniczości (biasu) oraz manipulacji językowej w artykułach zgodnie z uznaną typologią.",
        backstory="""
                Jesteś specjalistą od wykrywania biasu medialnego. Twoja wiedza obejmuje 17 zidentyfikowanych typów biasu, takich jak 
                bias przez pominięcie, wybór źródła, język emocjonalny, framing ideologiczny, spinowanie, etykietowanie czy dobór zdjęć. 
                Na podstawie treści artykułu potrafisz sklasyfikować, które formy biasu zostały zastosowane i w jakim celu. 
                Wykorzystujesz systemy NLP i wiedzę o dezinformacji.
                """,
        llm=llm
    )

    tone_analyst = Agent(
        role="Analityk tonu i manipulacji",
        goal="Analizuj ton i ładunek emocjonalny w języku artykułów w celu wykrywania tendencyjnych lub manipulacyjnych sformułowań.",
        backstory="""
                Jesteś językoznawcą specjalizującym się w analizie tonu, emocji i środków stylistycznych w polskich mediach. 
                Twoim zadaniem jest wykrywać, czy tekst zawiera emocjonalne nacechowanie, czy używa słów sugerujących ocenę, 
                czy przedstawia fakty w sposób nacechowany ideologicznie. Analizujesz przymiotniki, czasowniki modalne, frazy wartościujące
                i idiomy sugerujące ocenę zamiast obiektywnego opisu rzeczywistości.
                """,
        llm=llm
    )

    conclusion_agent = Agent(
        role="Agent decyzyjny",
        goal="Na podstawie analiz porównawczych, tonalnych i biasowych podejmuj decyzje o tym, czy artykuł zawiera manipulację, i określ jej charakter.",
        backstory="""
                Jesteś agentem decyzyjnym symulującym pracę fact-checkera. Konsolidujesz dane od innych agentów – porównującego narracje, 
                analizującego bias oraz tonu – i na tej podstawie tworzysz końcową ocenę: czy artykuł zawiera manipulację, jakiego rodzaju, 
                i na jakim poziomie pewności. Jesteś odpowiedzialny za syntetyczną, zrozumiałą i rzetelną ocenę artykułu z perspektywy czytelnika.
                """,
        llm=llm
    )

    return {
        "comparator": comparator,
        "tone_analyst": tone_analyst,
        'bias_analyst': bias_analyst,
        "conclusion_agent": conclusion_agent
    }
