# trans-crewai

## CrewAI Translation Application

This application is a translation workflow management system built using the CrewAI framework. It allows users to define custom agents and tasks to perform linguistic review, cross-checking, and final review of translated documents.

## Installation

1. Clone the repository:
bash
```
git clone 
```

2. Install the required dependencies:

python
```
pip install -r requirements.txt
```

3. Set up the environment variables:
- Create a `.env` file in the project root directory.
- Add the following variables to the `.env` file:
  ```
  OPENAI_API_KEY=<your-openai-api-key>
  ```

## Customizing Tasks and Agents

The application allows you to define custom tasks and agents in the `tasks.py` and `agents.py` files, respectively.

### Defining Custom Tasks

1. Open the `tasks.py` file.
2. Create a new method within the `CustomTasks` class for each custom task you want to define.
3. Inside the method, create and return a `Task` object with the following parameters:
- `description`: A detailed description of the task.
- `agent`: The agent assigned to perform the task.
- `output_file`: The file path where the task output will be saved.
- `expected_output`: A description of the expected output format.

### Defining Custom Agents

1. Open the `agents.py` file.
2. Create a new method within the `CustomAgents` class for each custom agent you want to define.
3. Inside the method, create and return an `Agent` object with the following parameters:
- `role`: The role or name of the agent.
- `backstory`: A brief background story or description of the agent's expertise.
- `goal`: The specific goal or objective of the agent.
- `tools`: A list of tools available to the agent (e.g., `file_tool`, `docs_tool`).
- `allow_delegation`: A boolean indicating whether the agent is allowed to delegate tasks.
- `verbose`: A boolean indicating whether to enable verbose output.
- `llm`: The language model to be used by the agent (e.g., `self.OpenAIGPT4`).

## Running the Application

1. Open the `main.py` file.
2. Modify the `CustomCrew` class to define your custom crew:
- Instantiate the custom agents and tasks defined in `agents.py` and `tasks.py`.
- Create a `Crew` object with the desired agents and tasks.
3. Run the application:

python
```
python main.py
```

4. Follow the prompts to enter the required variables.
5. The application will execute the defined tasks and agents, and the results will be displayed in the console.

## Customizing the Workflow

You can customize the translation workflow by modifying the `CustomCrew` class in the `main.py` file:

- Add or remove custom agents and tasks as needed.
- Modify the order of tasks to suit your workflow requirements.
- Adjust the input variables and prompts to match your specific use case.

Feel free to explore and extend the functionality of the application to meet your translation workflow needs.

