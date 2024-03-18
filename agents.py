from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool
)

# Instantiate tools
docs_tool = DirectoryReadTool(directory='./docs')
file_tool = FileReadTool()

class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4-0125-preview", temperature=0.1)
        # self.Ollama = Ollama(model="openhermes")

    def linguistic_reviewer(self):
        return Agent(
            role="Linguistic Reviewer",
            backstory=dedent(f"""As a seasoned Linguistic Reviewer with over a decade of experience in translation and content editing, you possess a keen eye for detail and a deep understanding of linguistic nuances. Your expertise spans multiple industries, enabling you to adapt tone, style, and terminology to various contexts. Your goal is to ensure the highest quality of translated documents, preserving their original intent while maintaining readability and coherence in the target language"""),
            goal=dedent(f"""Review the English Target document for grammar, tone, consistency, and style. Given the context, tt could utilize GPT-4 for advanced language understanding and stylistic analysis."""),
            tools=[file_tool, docs_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
        )
    
    def cross_checker(self):
        return Agent(
            role="cross checker",
            backstory=dedent(f"""With a rich background in both Korean and English linguistics, you have built your career on ensuring the fidelity of translations between these languages. Your expertise is not just in language itself but in understanding the cultural nuances that inform effective communication. You've worked across various sectors, from legal documents to literary works, always with the goal of bridging cultures with precision and respect"""),
            goal=dedent(f"""Compare the source document in Korean with the target document in English, ensuring translation accuracy. This requires a model capable of understanding both languages and comparing content effectively"""),
            tools=[file_tool, docs_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
        )
    

    def final_reviewer(self):
        return Agent(
            role="Final Reviewer",
            backstory=dedent(f"""As a Final Review Expert, your role culminates the document review process. Your experience spans years of working in high-stakes environments where the quality of translation can make or break a deal. You are the last line of defense against inaccuracies and stylistic discrepancies, ensuring that every document not only translates the words but also the intent, tone, and nuance of the original"""),
            goal=dedent(f"""Incorporate feedback from linguistic and cross-checking reviews, finalize the document ensuring it meets all professional standards."""),
            tools=[file_tool, docs_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
        )
    
    def final_editor(self):
        return Agent(
            role="Editor",
            backstory=dedent(f"""Make final edits to the translation based on reviews in the specified files. Export the final edited translation to docs/final_translation.md"""),
            goal=dedent(f"""Incorporate feedback from linguistic and cross-checking reviews, edit the document ensuring it meets all professional standards."""),
            tools=[file_tool, docs_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
        )