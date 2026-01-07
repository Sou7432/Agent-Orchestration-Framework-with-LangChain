# Agent-Orchestration-Framework-with-LangChain

This repository presents a lightweight Agent Orchestration Framework built using LangChain and OpenAI’s gpt-4o-mini model. The project demonstrates how a conversational AI agent can be designed using modular components such as custom tools, memory management, and a command-line interaction loop.

The primary objective of this project is to showcase the fundamentals of building an extensible, tool-enabled AI agent capable of maintaining conversational context and dynamically selecting actions.

# Overview
The agent is designed to:

  1.Understand and respond to natural language queries

  2.Maintain conversational context across multiple interactions

  3.Invoke external tools dynamically when required

The framework follows a clean, modular architecture to ensure ease of understanding, scalability, and experimentation.

# Key Implementation Highlights

1.Utilizes LangChain’s agent orchestration capabilities

2.Integrates custom tools for task-specific actions

3.Manages conversational state using memory components

4.Provides a simple and intuitive command-line interface
# Features
Custom Tools
A greeting tool that responds with a personalized message A weather tool that retrieves live temperature data using the wttr.in API

# Agent Capabilities
Dynamically selects tools when appropriate Generates natural language responses using the chosen model Maintains conversation history for context-aware interaction

# Console Interface
Allows continuous back-and-forth communication Accepts user queries until an explicit exit command is given

# Setup Instructions
1.Install Dependencies :

pip install -r requirements.txt


2.Configure Environment Variables
Create a .env file in the project root and add:

OPENAI_API_KEY=your_api_key_here


3.Run the Application

python src/main.py

# Technologies Used
Python 3.12

LangChain

OpenAI gpt-4o-mini

Requests (for external API calls)

python-dotenv (for environment variable management)
# License
This project is released under the MIT License.
