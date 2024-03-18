import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from decouple import config

from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks

# Install duckduckgo-search for this example:
# !pip install -U duckduckgo-search

# from langchain.tools import DuckDuckGoSearchRun

# search_tool = DuckDuckGoSearchRun()

os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
# os.environ["OPENAI_ORGANIZATION"] = config("OPENAI_ORGANIZATION_ID")

# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class CustomCrew:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        custom_agent_1 = agents.linguistic_reviewer()
        custom_agent_2 = agents.cross_checker()
        custom_agent_3 = agents.final_reviewer()
        custom_agent_4 = agents.final_editor()

        # Custom tasks include agent name and variables as input
        custom_task_1 = tasks.linguistic_review_task(
            custom_agent_1,
            self.var1,
        )

        custom_task_2 = tasks.cross_checking_task(
            custom_agent_2,
            self.var1,
            self.var2,
        )

        custom_task_3 = tasks.final_review_task(
            custom_agent_3,
            self.var1,
            self.var2,
        )

        custom_task_4 = tasks.final_edit(
            custom_agent_4,
            self.var1,
            self.var2,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[custom_agent_1, custom_agent_2, custom_agent_3, custom_agent_4],
            tasks=[custom_task_1, custom_task_2, custom_task_3, custom_task_4],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    var1 = input(dedent("""Enter variable 1: """))
    var2 = input(dedent("""Enter variable 2: """))

    custom_crew = CustomCrew(var1, var2)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)