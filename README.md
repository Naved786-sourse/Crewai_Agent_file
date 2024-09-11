# Crewai_Agent_file

# Academic Content Research and Writing Tool

## Overview

This project provides a tool for academic content research and writing using CrewAI and LangChain. The tool includes two main functionalities:
1. Researching academic content based on a given topic.
2. Creating engaging content such as summaries and blog posts based on the researched information.

## Components

1. **`requirements.txt`**: Lists the necessary Python packages for the project.
2. **`agent.py`**: Defines the agents used for research and writing.
3. **`task.py`**: Contains the tasks for research and writing.
4. **`crew.py`**: Integrates the agents and tasks with a Streamlit user interface.

## Installation

1. **Create a virtual environment** (if not already created):
    ```bash
    python -m venv venv
    ```

2. **Activate the virtual environment**:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    - Create a `.env` file in the root directory of the project with the following content:
      ```
      OPENAI_API_KEY=your_openai_api_key
      ```

## Usage

1. **Run the Streamlit app**:
    ```bash
    streamlit run crew.py
    ```

2. **Interact with the app**:
    - Open your browser and go to `http://localhost:8501`.
    - Enter a topic and click "Run Research" to start the research and writing process.
    - View the results displayed on the page.

## Files

- **`requirements.txt`**: Contains the list of required packages.
- **`agent.py`**: Contains the definitions for the `researcher` and `writer` agents.
- **`task.py`**: Defines the `research` and `write` tasks.
- **`crew.py`**: The Streamlit interface and Crew setup for running the application.

## Contributing

Feel free to contribute to the project by submitting issues or pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or support, please contact:

- **Email**: muhammadadeeb65@gmail.com


