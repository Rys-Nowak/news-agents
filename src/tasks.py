from crewai import Task

def build_tasks(agents, article1, article2):
    # TODO diffrent task for 1 and for multiple docs
    return [
        Task(
            description=f"""
                Porównaj narrację i strukturę artykułów opisujących ten sam temat, ale pochodzących z różnych źródeł lub dat. Skoncentruj się na różnicach w tonie, selekcji faktów,
                emocjonalnym nacechowaniu, pominięciach lub przesunięciach w akcentach.
                Zidentyfikuj zmiany, które mogą świadczyć o subtelnej manipulacji treścią.
                --- Artykuł A ---
                Tytuł: {article1['title']}
                Treść: {article1['content']}
    
                --- Artykuł B ---
                Tytuł: {article2['title']}
                Treść: {article2['content']}
                """,
            agent=agents["comparator"],
            expected_output="""
                Szczegółowe porównanie narracji artykułów, zawierające:
                - Kluczowe różnice w tonie i doborze informacji
                - Możliwe pominięcia lub przesunięcia akcentów
                - Fragmenty tekstu ilustrujące różnice
                - Wnioski: czy różnice wskazują na potencjalną manipulację
                """
        ),
        Task(
            description=f"""
                Przeanalizuj ton i język artykułu lub jego fragmentów.
                Zidentyfikuj elementy wskazujące na nacechowanie emocjonalne, 
                manipulacyjny dobór słów, wartościujące przymiotniki lub inne środki wpływające na odbiór.
                Uwzględnij użycie retoryki, eufemizmów, pejoratywów, modalności i idiomów.
                --- Artykuł A ---
                Tytuł: {article1['title']}
                Treść: {article1['content']}
                """,
            agent=agents["tone_analyst"],
            expected_output="""
                Raport analizy tonu zawierający:
                - Identyfikację fragmentów nacechowanych emocjonalnie
                - Opis użycia języka sugerującego opinię zamiast faktów
                - Kategorie użytych środków stylistycznych (np. clickbait, dramatyzacja, sugestywność)
                - Ocena ogólnego tonu: neutralny / emocjonalny / perswazyjny / dramatyczny
                """
        ),
        Task(
            description=f"""
                Przeanalizuj artykuł i sklasyfikuj obecne formy stronniczości (biasu) zgodnie z uznaną typologią.
                Uwzględnij m.in.: bias przez pominięcie, dobór źródeł, framing ideologiczny, spin, 
                ad hominem, błędy logiczne, dobór zdjęć i opisów, oraz przedstawianie opinii jako faktów.

                --- Artykuł B ---
                Tytuł: {article2['title']}
                Treść: {article2['content']}
                """,
            agent=agents["bias_analyst"],
            expected_output="""
                Lista wykrytych form biasu z przypisanymi fragmentami artykułu:
                - Typy biasu wg klasyfikacji (np. spin, gatekeeping, labeling, omission)
                - Kontekst użycia i jego interpretacja
                - Wskaźnik pewności (np. 0–1)
                - Możliwa intencja stojąca za zastosowaną stronniczością
                """
        ),
        Task(
            description="""
                Na podstawie raportów od pozostałych agentów (porównującego narracje, analizującego ton i bias),
                przygotuj końcową ocenę artykułu. Określ, czy zawiera on manipulację i w jakim stopniu.
                Podaj uzasadnienie decyzji, wskazując na kluczowe elementy manipulacyjne oraz ich znaczenie.
                """,
            agent=agents["conclusion_agent"],
            expected_output="""
                Końcowa decyzja dotycząca artykułu:
                - Czy występuje manipulacja: tak / nie
                - Rodzaj manipulacji (np. emocjonalna, informacyjna, ideologiczna)
                - Poziom intensywności (np. subtelna / umiarkowana / silna)
                - Argumentacja na podstawie danych od pozostałych agentów
                - Wnioski końcowe do przedstawienia użytkownikowi lub ewaluatorowi
                """
        )
    ]